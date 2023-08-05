"""Individual road time trial handler for roadmeet."""

import gtk
import glib
import gobject
import os
import logging
import threading

import metarace
from metarace import tod
from metarace import eventdb
from metarace import riderdb
from metarace import strops
from metarace import uiutil
from metarace import timerpane
from metarace import report
from metarace import jsonconfig

LOG = logging.getLogger(u'metarace.irtt')
LOG.setLevel(logging.DEBUG)

# rider commands
RIDER_COMMANDS_ORD = [
    u'add', u'del', u'que', u'onc', u'dns', u'otl', u'dnf', u'dsq', u'com', ''
]
RIDER_COMMANDS = {
    u'dns': u'Did not start',
    u'dnf': u'Did not finish',
    u'add': u'Add starters',
    u'del': u'Remove starters',
    u'que': u'Query riders',
    u'com': u'Add comment',
    u'otl': u'Outside time limit',
    u'dsq': u'Disqualify',
    u'onc': u'Riders on course',
    u'': u'',
}

RESERVED_SOURCES = [
    u'fin',  # finished stage
    u'reg',  # registered to stage
    u'start'
]  # started stage

DNFCODES = [u'otl', u'dsq', u'dnf', u'dns']
STARTFUDGE = tod.tod(30)
ARRIVALTIMEOUT = tod.tod(u'2:30')

# startlist model columns
COL_BIB = 0
COL_SERIES = 1
COL_NAMESTR = 2
COL_CAT = 3
COL_COMMENT = 4
COL_WALLSTART = 5
COL_TODSTART = 6
COL_TODFINISH = 7
COL_TODPENALTY = 8
COL_PLACE = 9
COL_SHORTNAME = 10
COL_INTERA = 11
COL_INTERB = 12
COL_INTERC = 13
COL_INTERD = 14
COL_INTERE = 15
COL_LASTSEEN = 16
COL_ETA = 17
COL_PASS = 18

# scb function key mappings
key_startlist = u'F6'  # clear scratchpad (FIX)
key_results = u'F4'  # recalc/show results in scratchpad
key_starters = u'F3'  # show next few starters in scratchpad

# timing function key mappings
key_armsync = u'F1'  # arm for clock sync start
key_armstart = u'F5'  # arm for start impulse
key_armfinish = u'F9'  # arm for finish impulse
key_raceover = u'F10'  # flag race completion/not provisional

# extended function key mappings
key_reset = u'F5'  # + ctrl for clear/abort
key_falsestart = u'F6'  # + ctrl for false start
key_abort_start = u'F7'  # + ctrl abort A
key_abort_finish = u'F8'  # + ctrl abort B

# config version string
EVENT_ID = u'roadtt-3.0'


def jsob(inmap):
    """Return a json'able map."""
    ret = None
    if inmap is not None:
        ret = {}
        for key in inmap:
            if key in [u'minelap', u'maxelap']:
                ret[key] = inmap[key].rawtime()
            else:
                ret[key] = inmap[key]
    return ret


def unjsob(inmap):
    """Un-jsob the provided map."""
    ret = None
    if inmap is not None:
        ret = {}
        for key in inmap:
            if key in [u'minelap', u'maxelap']:
                ret[key] = tod.mktod(inmap[key])
            else:
                ret[key] = inmap[key]
    return ret


def sort_tally(x, y):
    """Points tally sort using countback struct."""
    if x[0] == y[0]:
        return cmp(y[3], x[3])
    elif y[0] < x[0]:
        return -1
    else:
        return 1


def sort_dnfs(x, y):
    """Sort dnf riders by code and riderno."""
    if x[2] == y[2]:  # same code
        if x[2]:
            return cmp(strops.bibstr_key(x[1]), strops.bibstr_key(y[1]))
        else:
            return 0  # don't alter order on unplaced riders
    else:
        return strops.cmp_dnf(x[2], y[2])


class irtt(object):
    """Data handling for road time trial."""

    def key_event(self, widget, event):
        """Race window key press handler."""
        if event.type == gtk.gdk.KEY_PRESS:
            key = gtk.gdk.keyval_name(event.keyval) or u'None'
            if event.state & gtk.gdk.CONTROL_MASK:
                if key == key_reset:  # override ctrl+f5
                    return True
                elif key == key_falsestart:  # false start both lanes
                    return True
                elif key == key_abort_start:  # abort start line
                    return True
                elif key == key_abort_finish:  # abort finish line
                    return True
            if key[0] == 'F':
                if key == key_armstart:
                    self.armstart()
                    return True
                elif key == key_armfinish:
                    self.armfinish()
                    return True
                elif key == key_startlist:
                    self.meet.cmd_announce(u'clear', u'all')
                    self.doannounce = True
                    return True
                elif key == key_raceover:
                    self.set_finished()
                    return True
                elif key == key_results:
                    return True
        return False

    def resetall(self):
        """Reset timers."""
        self.fl.toidle()
        self.fl.disable()

    def set_finished(self):
        """Update event status to finished."""
        if self.timerstat == u'finished':
            self.timerstat = u'running'
            self.meet.stat_but.buttonchg(uiutil.bg_armstart, u'Running')
            self.meet.stat_but.set_sensitive(True)
        else:
            self.timerstat = u'finished'
            self.meet.stat_but.buttonchg(uiutil.bg_none, u'Finished')
            self.meet.stat_but.set_sensitive(False)

    def armfinish(self):
        if self.timerstat == u'running':
            if self.fl.getstatus() != u'finish' and self.fl.getstatus(
            ) != u'armfin':
                self.fl.toarmfin()
            else:
                self.fl.toidle()
                self.announce_rider()

    def armstart(self):
        if self.timerstat == u'idle':
            LOG.info(u'Armed for timing sync')
            self.timerstat = u'armstart'
        elif self.timerstat == u'armstart':
            self.resetall()
        elif self.timerstat == u'running':
            if self.sl.getstatus() in [u'armstart', u'running']:
                self.sl.toidle()
            elif self.sl.getstatus() != u'running':
                self.sl.toarmstart()

    def delayed_announce(self):
        """Re-announce all riders from the nominated category."""
        self.meet.cmd_announce(u'clear', u'all')
        heading = u''
        if self.timerstat == u'finished':
            heading = u': Result'
        else:
            if self.racestat == u'prerace':
                heading = u''  # anything better?
            else:
                heading = u': Standings'
        self.meet.cmd_announce(u'title',
                               self.title_namestr.get_text() + heading)
        self.meet.cmd_announce(u'finstr', self.meet.get_short_name())
        cat = self.ridercat(self.curcat)
        for t in self.results[cat]:
            r = self.getiter(t[0].refid, t[0].index)
            if r is not None:
                et = self.getelapsed(r)
                bib = t[0].refid
                rank = self.riders.get_value(r, COL_PLACE)
                cat = self.riders.get_value(r, COL_CAT)
                namestr = self.riders.get_value(r, COL_NAMESTR)
                self.meet.rider_announce(
                    [rank, bib, namestr, cat,
                     et.rawtime(2)])
        arrivalsec = self.arrival_report(0)  # fetch all arrivals
        if len(arrivalsec) > 0:
            arrivals = arrivalsec[0].lines
            for a in arrivals:
                # announce arrival
                pass
        return False

    def edit_event_properties(self, window, data=None):
        """Edit event specifics."""
        LOG.warning(u'Edit event properties not implemented')

    def wallstartstr(self, col, cr, model, iter, data=None):
        """Format start time into text for listview."""
        st = model.get_value(iter, COL_TODSTART)
        if st is not None:
            cr.set_property(u'text', st.timestr(2))  # time from tapeswitch
            cr.set_property(u'style', uiutil.STYLE_NORMAL)
        else:
            cr.set_property(u'style', uiutil.STYLE_OBLIQUE)
            wt = model.get_value(iter, COL_WALLSTART)
            if wt is not None:
                cr.set_property(u'text', wt.timestr(0))  # adv start
            else:
                cr.set_property(u'text', u'')  # no info on start time

    def announce_rider(self,
                       place=u'',
                       bib=u'',
                       namestr=u'',
                       shortname=u'',
                       cat=u'',
                       rt=None,
                       et=None):
        """Emit a finishing rider to announce."""
        rts = u''
        if et is not None:
            rts = et.rawtime(2)
        elif rt is not None:
            rts = rt.rawtime(0)
        # Announce rider
        ##self.meet.scb.add_rider([place, bib, shortname, cat, rts], 'finpanel')
        ##self.meet.scb.add_rider([place, bib, namestr, cat, rts], 'finish')

    def geteta(self, iter):
        """Return a best guess rider's ET."""
        ret = self.getelapsed(iter)
        if ret is None:
            # scan each inter from farthest to nearest
            for ipt in [
                    COL_INTERE, COL_INTERD, COL_INTERC, COL_INTERB, COL_INTERA
            ]:
                if ipt in self.ischem and self.ischem[ipt] is not None:
                    dist = self.ischem[ipt][u'dist']
                    inter = self.riders.get_value(iter, ipt)
                    if inter is not None and dist is not None:
                        totdist = 1000.0 * self.meet.distance
                        st = self.riders.get_value(iter, COL_TODSTART)
                        if st is None:  # defer to start time
                            st = self.riders.get_value(iter, COL_WALLSTART)
                        if st is not None:  # still none is error
                            et = inter - st
                            spd = (1000.0 * dist) / float(et.timeval)
                            ret = tod.tod(str(totdist / spd))
                            self.riders.set_value(iter, COL_PASS, int(dist))
                            break
        return ret

    def getelapsed(self, iter, runtime=False):
        """Return a tod elapsed time."""
        ret = None
        ft = self.riders.get_value(iter, COL_TODFINISH)
        if ft is not None:
            st = self.riders.get_value(iter, COL_TODSTART)
            if st is None:  # defer to start time
                st = self.riders.get_value(iter, COL_WALLSTART)
            if st is not None:  # still none is error
                pt = self.riders.get_value(iter, COL_TODPENALTY)
                # penalties are added into stage result - for consistency
                ret = (ft - st) + pt
        elif runtime:
            st = self.riders.get_value(iter, COL_TODSTART)
            if st is None:  # defer to start time
                st = self.riders.get_value(iter, COL_WALLSTART)
            if st is not None:  # still none is error
                ret = tod.now() - st  # runtime increases!
        return ret

    def stat_but_clicked(self, button=None):
        """Deal with a status button click in the main container."""
        LOG.debug(u'Stat button clicked')

    def ctrl_change(self, acode=u'', entry=None):
        """Notify change in action combo."""
        pass
        # TODO?
        if acode == u'fin':
            pass
        else:
            if entry is not None:
                entry.set_text(u'')

    def race_ctrl(self, acode=u'', rlist=u''):
        """Apply the selected action to the provided bib list."""
        if acode in self.intermeds:
            rlist = strops.reformat_bibserplacelist(rlist)
            if self.checkplaces(rlist, dnf=False):
                self.intermap[acode][u'places'] = rlist
                self.placexfer()
                LOG.info(u'Intermediate %r == %r', acode, rlist)
            else:
                LOG.error('Intermediate %r not updated', acode)
                return False
        elif acode == u'que':
            LOG.debug(u'Query rider not implemented - reannounce ridercat')
            self.curcat = self.ridercat(rlist.strip())
            self.doannounce = True
        elif acode == u'del':
            rlist = strops.reformat_bibserlist(rlist)
            for bibstr in rlist.split():
                bib, ser = strops.bibstr2bibser(bibstr)
                self.delrider(bib, ser)
            return True
        elif acode == u'add':
            LOG.info(u'Add starter deprecated: Use startlist import')
            rlist = strops.reformat_bibserlist(rlist)
            for bibstr in rlist.split():
                bib, ser = strops.bibstr2bibser(bibstr)
                self.addrider(bib, ser)
            return True
        elif acode == u'onc':
            LOG.info(u'on-course ignored')
            return True
        elif acode == u'dnf':
            self.dnfriders(strops.reformat_bibserlist(rlist))
            return True
        elif acode == u'dsq':
            self.dnfriders(strops.reformat_bibserlist(rlist), u'dsq')
            return True
        elif acode == u'otl':
            self.dnfriders(strops.reformat_bibserlist(rlist), u'otl')
            return True
        elif acode == u'dns':
            self.dnfriders(strops.reformat_bibserlist(rlist), u'dns')
            return True
        elif acode == u'com':
            self.add_comment(rlist)
            return True
        else:
            LOG.error(u'Ignoring invalid action %r', acode)
        return False

    def add_comment(self, comment=u''):
        """Append a commissaires comment."""
        self.comment.append(comment.strip())
        LOG.info(u'Added comment: %r', comment)

    def elapstr(self, col, cr, model, iter, data=None):
        """Format elapsed time into text for listview."""
        ft = model.get_value(iter, COL_TODFINISH)
        if ft is not None:
            st = model.get_value(iter, COL_TODSTART)
            if st is None:  # defer to wall start time
                st = model.get_value(iter, COL_WALLSTART)
                cr.set_property(u'style', uiutil.STYLE_OBLIQUE)
            else:
                cr.set_property(u'style', uiutil.STYLE_NORMAL)
            et = self.getelapsed(iter)
            if et is not None:
                cr.set_property(u'text', et.timestr(2))
            else:
                cr.set_property(u'text', u'[ERR]')
        else:
            cr.set_property(u'text', u'')

    def loadcats(self, cats=[]):
        self.cats = []  # clear old cat list
        if u'AUTO' in cats:  # ignore any others and re-load from rdb
            self.cats = self.meet.rdb.listcats()
            self.autocats = True
        else:
            self.autocats = False
            for cat in cats:
                if cat != u'':
                    cat = cat.upper()
                    if cat not in [u'CAT', u'SPARE', u'TEAM']:
                        self.cats.append(cat)
                    else:
                        LOG.warning(u'Invalid result category: %r', cat)
        self.cats.append(u'')  # always include one empty cat
        self.catlaps = {}
        for cat in self.cats:
            self.results[cat] = tod.todlist(cat)
            self.inters[COL_INTERA][cat] = tod.todlist(cat)
            self.inters[COL_INTERB][cat] = tod.todlist(cat)
            self.inters[COL_INTERC][cat] = tod.todlist(cat)
            self.inters[COL_INTERD][cat] = tod.todlist(cat)
            self.inters[COL_INTERE][cat] = tod.todlist(cat)
            lt = self.finishpass
            dbr = self.meet.rdb.getrider(cat, u'cat')
            if dbr is not None:
                clt = strops.confopt_posint(
                    self.meet.rdb.getvalue(dbr, riderdb.COL_CAT), None)
                if clt is not None:
                    # override lap count from category
                    lt = clt
            self.catlaps[cat] = lt
            LOG.debug(u'Set category %r pass count to: %r', cat, lt)
        LOG.debug(u'Result category list updated: %r', self.cats)

    def loadconfig(self):
        """Load race config from disk."""
        self.riders.clear()
        self.results = {u'': tod.todlist(u'UNCAT')}
        self.cats = []

        cr = jsonconfig.config({
            u'irtt': {
                u'startlist': u'',
                u'id': EVENT_ID,
                u'start': u'0',
                u'comment': [],
                u'categories': [],
                u'arrivalcount': 4,
                u'lstart': u'0',
                u'startgap': u'1:00',
                u'precision': 1,
                u'autoexport': False,
                u'intermeds': [],
                u'contests': [],
                u'minelap': STARTFUDGE,
                u'sloppystart': False,
                u'startdelay': None,
                u'startloop': None,
                u'starttrig': None,
                u'finishloop': u'thbc',
                u'finishpass': None,
                u'interloops': {},
                u'tallys': [],
                u'onestartlist': True,
                u'timelimit': None,
                u'finished': False,
                u'showinter': None,
                u'intera': None,
                u'interb': None,
                u'interc': None,
                u'interd': None,
                u'intere': None,
            }
        })
        cr.add_section(u'irtt')
        cr.add_section(u'riders')
        cr.add_section(u'stagebonus')
        cr.add_section(u'stagepenalty')
        cr.merge(metarace.sysconf, u'irtt')

        if os.path.exists(self.configfile):
            try:
                with open(self.configfile, 'rb') as f:
                    cr.read(f)
            except Exception as e:
                LOG.error(u'Unable to read config: %s', e)
        else:
            LOG.info(u'%r not found, loading defaults', self.configfile)

        # load default gap
        self.startgap = tod.mktod(cr.get(u'irtt', u'startgap'))
        if self.startgap is None:
            self.startgap = tod.tod(u'1:00')

        # load result precision
        self.precision = strops.confopt_posint(cr.get(u'irtt', u'precision'))
        if self.precision > 2:  # posint forbids negatives
            self.precision = 2

        # load start delay for wireless impulse
        self.startdelay = tod.mktod(cr.get(u'irtt', u'startdelay'))
        if self.startdelay is None:
            self.startdelay = tod.ZERO

        # load minimum elapsed time
        self.minelap = tod.mktod(cr.get(u'irtt', u'minelap'))
        if self.minelap is None:
            self.minelap = STARTFUDGE
        self.timelimit = cr.get(u'irtt', u'timelimit')  # save as str

        # allow auto export
        self.autoexport = strops.confopt_bool(cr.get(u'irtt', u'autoexport'))
        # sloppy start times
        self.sloppystart = strops.confopt_bool(cr.get(u'irtt', u'sloppystart'))

        # transponder-based timing
        self.startloop = cr.get(u'irtt', u'startloop')
        self.starttrig = cr.get(u'irtt', u'starttrig')
        self.finishloop = cr.get(u'irtt', u'finishloop')
        self.finishpass = cr.get(u'irtt', u'finishpass')
        if self.startloop is not None or self.finishloop is not None:
            self.precision = 1
            LOG.info(u'Forced precision to 1: startloop=%r finishloop=%r',
                     self.startloop, self.finishloop)

        # load intermediate split schema
        self.showinter = strops.confopt_posint(cr.get(u'irtt', u'showinter'),
                                               None)
        self.ischem[COL_INTERA] = unjsob(cr.get(u'irtt', u'intera'))
        self.ischem[COL_INTERB] = unjsob(cr.get(u'irtt', u'interb'))
        self.ischem[COL_INTERC] = unjsob(cr.get(u'irtt', u'interc'))
        self.ischem[COL_INTERD] = unjsob(cr.get(u'irtt', u'interd'))
        self.ischem[COL_INTERE] = unjsob(cr.get(u'irtt', u'intere'))
        self.interloops = cr.get(u'irtt', u'interloops')

        # load _result_ categories
        self.loadcats(cr.get(u'irtt', u'categories'))

        # restore intermediates
        for i in cr.get(u'irtt', u'intermeds'):
            if i in RESERVED_SOURCES:
                LOG.info(u'Ignoring reserved intermediate: %r', i)
            else:
                crkey = u'intermed_' + i
                descr = u''
                places = u''
                if cr.has_option(crkey, u'descr'):
                    descr = cr.get(crkey, u'descr')
                if cr.has_option(crkey, u'places'):
                    places = strops.reformat_placelist(cr.get(
                        crkey, u'places'))
                if i not in self.intermeds:
                    LOG.debug(u'Adding inter %r: %r %r', i, descr, places)
                    self.intermeds.append(i)
                    self.intermap[i] = {u'descr': descr, u'places': places}
                else:
                    LOG.info(u'Ignoring duplicate inter: %r', i)

        # load contest meta data
        tallyset = set()
        for i in cr.get(u'irtt', u'contests'):
            if i not in self.contests:
                self.contests.append(i)
                self.contestmap[i] = {}
                crkey = u'contest_' + i
                tally = u''
                if cr.has_option(crkey, u'tally'):
                    tally = cr.get(crkey, u'tally')
                    if tally:
                        tallyset.add(tally)
                self.contestmap[i][u'tally'] = tally
                descr = i
                if cr.has_option(crkey, u'descr'):
                    descr = cr.get(crkey, u'descr')
                    if descr == u'':
                        descr = i
                self.contestmap[i][u'descr'] = descr
                labels = []
                if cr.has_option(crkey, u'labels'):
                    labels = cr.get(crkey, u'labels').split()
                self.contestmap[i][u'labels'] = labels
                source = i
                if cr.has_option(crkey, u'source'):
                    source = cr.get(crkey, u'source')
                    if source == u'':
                        source = i
                self.contestmap[i][u'source'] = source
                bonuses = []
                if cr.has_option(crkey, u'bonuses'):
                    for bstr in cr.get(crkey, u'bonuses').split():
                        bt = tod.mktod(bstr)
                        if bt is None:
                            LOG.info(u'Invalid bonus %r in contest %r', bstr,
                                     i)
                            bt = tod.ZERO
                        bonuses.append(bt)
                self.contestmap[i][u'bonuses'] = bonuses
                points = []
                if cr.has_option(crkey, u'points'):
                    pliststr = cr.get(crkey, u'points').strip()
                    if pliststr and tally == u'':  # no tally for these points!
                        LOG.error(u'No tally for points in contest %r', i)
                        tallyset.add(u'')  # add empty placeholder
                    for pstr in pliststr.split():
                        pt = 0
                        try:
                            pt = int(pstr)
                        except Exception:
                            LOG.info(u'Invalid points %r in contest %r', pstr,
                                     i)
                        points.append(pt)
                self.contestmap[i][u'points'] = points
                allsrc = False  # all riders in source get same pts
                if cr.has_option(crkey, u'all_source'):
                    allsrc = strops.confopt_bool(cr.get(crkey, u'all_source'))
                self.contestmap[i][u'all_source'] = allsrc
            else:
                LOG.info(u'Ignoring duplicate contest %r', i)

            # check for invalid allsrc
            if self.contestmap[i][u'all_source']:
                if (len(self.contestmap[i][u'points']) > 1
                        or len(self.contestmap[i][u'bonuses']) > 1):
                    LOG.info(u'Ignoring extra points/bonus for allsrc %r', i)

        # load points tally meta data
        tallylist = cr.get(u'irtt', 'tallys')
        # append any 'missing' tallys from points data errors
        for i in tallyset:
            if i not in tallylist:
                LOG.debug(u'Adding missing tally to config %r', i)
                tallylist.append(i)
        # then scan for meta data
        for i in tallylist:
            if i not in self.tallys:
                self.tallys.append(i)
                self.tallymap[i] = {}
                self.points[i] = {}  # redundant, but ok
                self.pointscb[i] = {}
                crkey = u'tally_' + i
                descr = u''
                if cr.has_option(crkey, u'descr'):
                    descr = cr.get(crkey, u'descr')
                self.tallymap[i][u'descr'] = descr
                keepdnf = False
                if cr.has_option(crkey, u'keepdnf'):
                    keepdnf = strops.confopt_bool(cr.get(crkey, u'keepdnf'))
                self.tallymap[i][u'keepdnf'] = keepdnf
            else:
                LOG.info(u'Ignoring duplicate points tally %r', i)

        # re-join any existing timer state -> no, just do a start
        self.set_syncstart(tod.mktod(cr.get(u'irtt', u'start')),
                           tod.mktod(cr.get(u'irtt', u'lstart')))

        # re-load starters/results
        self.onestart = False
        for rs in cr.get(u'irtt', u'startlist').split():
            (r, s) = strops.bibstr2bibser(rs)
            self.addrider(r, s)
            wst = None
            tst = None
            ft = None
            pt = None
            ima = None
            imb = None
            imc = None
            imd = None
            ime = None
            lpass = None
            pcnt = 0
            if cr.has_option(u'riders', rs):
                # bbb.sss = comment,wall_start,timy_start,finish,penalty,place
                nr = self.getrider(r, s)
                ril = cr.get(u'riders', rs)  # vec
                lr = len(ril)
                if lr > 0:
                    nr[COL_COMMENT] = ril[0]
                if lr > 1:
                    wst = tod.mktod(ril[1])
                if lr > 2:
                    tst = tod.mktod(ril[2])
                if lr > 3:
                    ft = tod.mktod(ril[3])
                if lr > 4:
                    pt = tod.mktod(ril[4])
                if lr > 6:
                    ima = tod.mktod(ril[6])
                if lr > 7:
                    imb = tod.mktod(ril[7])
                if lr > 8:
                    imc = tod.mktod(ril[8])
                if lr > 9:
                    imd = tod.mktod(ril[9])
                if lr > 10:
                    ime = tod.mktod(ril[10])
                if lr > 11:
                    pcnt = strops.confopt_posint(ril[11])
                if lr > 12:
                    lpass = tod.mktod(ril[12])
            nri = self.getiter(r, s)
            self.settimes(nri, wst, tst, ft, pt, doplaces=False)
            self.setpasses(nri, pcnt)
            self.setinter(nri, ima, COL_INTERA)
            self.setinter(nri, imb, COL_INTERB)
            self.setinter(nri, imc, COL_INTERC)
            self.setinter(nri, imd, COL_INTERD)
            self.setinter(nri, ime, COL_INTERE)
            self.riders.set_value(nri, COL_LASTSEEN, lpass)

        self.placexfer()

        self.comment = cr.get(u'irtt', u'comment')
        self.arrivalcount = strops.confopt_posint(
            cr.get(u'irtt', u'arrivalcount'), 4)

        if strops.confopt_bool(cr.get(u'irtt', u'finished')):
            self.set_finished()
        self.onestartlist = strops.confopt_bool(
            cr.get(u'irtt', u'onestartlist'))

        # After load complete - check config and report. This ensures
        # an error message is left on top of status stack. This is not
        # always a hard fail and the user should be left to determine
        # an appropriate outcome.
        eid = cr.get(u'irtt', u'id')
        if eid and eid != EVENT_ID:
            LOG.info(u'Event config mismatch: %r != %r', eid, EVENT_ID)
            self.readonly = True

    def saveconfig(self):
        """Save race to disk."""
        if self.readonly:
            LOG.error(u'Attempt to save readonly event')
            return
        cw = jsonconfig.config()
        cw.add_section(u'irtt')
        if self.start is not None:
            cw.set(u'irtt', u'start', self.start.rawtime())
        if self.lstart is not None:
            cw.set(u'irtt', u'lstart', self.lstart.rawtime())
        cw.set(u'irtt', u'comment', self.comment)
        if self.startgap is not None:
            cw.set(u'irtt', u'startgap', self.startgap.rawtime(0))
        else:
            cw.set(u'irtt', u'startgap', None)
        if self.startdelay is not None:
            cw.set(u'irtt', u'startdelay', self.startdelay.rawtime())
        else:
            cw.set(u'irtt', u'startdelay', None)
        if self.minelap is not None:
            cw.set(u'irtt', u'minelap', self.minelap.rawtime())
        else:
            cw.set(u'irtt', u'minelap', None)

        cw.set(u'irtt', u'arrivalcount', self.arrivalcount)
        cw.set(u'irtt', u'sloppystart', self.sloppystart)
        cw.set(u'irtt', u'autoexport', self.autoexport)
        cw.set(u'irtt', u'startloop', self.startloop)
        cw.set(u'irtt', u'starttrig', self.starttrig)
        cw.set(u'irtt', u'finishloop', self.finishloop)
        cw.set(u'irtt', u'finishpass', self.finishpass)
        cw.set(u'irtt', u'onestartlist', self.onestartlist)
        cw.set(u'irtt', u'precision', self.precision)
        cw.set(u'irtt', u'timelimit', self.timelimit)

        # save intermediate data
        cw.set(u'irtt', u'intermeds', self.intermeds)
        for i in self.intermeds:
            crkey = u'intermed_' + i
            cw.add_section(crkey)
            cw.set(crkey, u'descr', self.intermap[i][u'descr'])
            cw.set(crkey, u'places', self.intermap[i][u'places'])
        # save contest meta data
        cw.set(u'irtt', u'contests', self.contests)
        for i in self.contests:
            crkey = u'contest_' + i
            cw.add_section(crkey)
            cw.set(crkey, u'tally', self.contestmap[i][u'tally'])
            cw.set(crkey, u'source', self.contestmap[i][u'source'])
            cw.set(crkey, u'all_source', self.contestmap[i][u'all_source'])
            blist = []
            for b in self.contestmap[i][u'bonuses']:
                blist.append(b.rawtime(0))
            cw.set(crkey, u'bonuses', u' '.join(blist))
            plist = []
            for p in self.contestmap[i][u'points']:
                plist.append(str(p))
            cw.set(crkey, u'points', u' '.join(plist))
        # save tally meta data
        cw.set(u'irtt', u'tallys', self.tallys)
        for i in self.tallys:
            crkey = u'tally_' + i
            cw.add_section(crkey)
            cw.set(crkey, u'descr', self.tallymap[i][u'descr'])
            cw.set(crkey, u'keepdnf', self.tallymap[i][u'keepdnf'])

        # save intermediate split schema
        cw.set(u'irtt', u'intera', jsob(self.ischem[COL_INTERA]))
        cw.set(u'irtt', u'interb', jsob(self.ischem[COL_INTERB]))
        cw.set(u'irtt', u'interc', jsob(self.ischem[COL_INTERC]))
        cw.set(u'irtt', u'interd', jsob(self.ischem[COL_INTERD]))
        cw.set(u'irtt', u'intere', jsob(self.ischem[COL_INTERE]))
        cw.set(u'irtt', u'interloops', self.interloops)
        cw.set(u'irtt', u'showinter', self.showinter)

        # save riders
        cw.set(u'irtt', u'startlist', self.get_startlist())
        if self.autocats:
            cw.set(u'irtt', u'categories', [u'AUTO'])
        else:
            cw.set(u'irtt', u'categories', self.get_catlist())
        cw.add_section(u'riders')
        for r in self.riders:
            if r[COL_BIB] != '':
                bib = r[COL_BIB].decode('utf-8')
                ser = r[COL_SERIES].decode('utf-8')
                # place is saved for info only
                wst = u''
                if r[COL_WALLSTART] is not None:
                    wst = r[COL_WALLSTART].rawtime()
                tst = u''
                if r[COL_TODSTART] is not None:
                    tst = r[COL_TODSTART].rawtime()
                tft = u''
                if r[COL_TODFINISH] is not None:
                    tft = r[COL_TODFINISH].rawtime()
                tpt = u''
                if r[COL_TODPENALTY] is not None:
                    tpt = r[COL_TODPENALTY].rawtime()
                tima = u''
                if r[COL_INTERA] is not None:
                    tima = r[COL_INTERA].rawtime()
                timb = u''
                if r[COL_INTERB] is not None:
                    timb = r[COL_INTERB].rawtime()
                timc = u''
                if r[COL_INTERC] is not None:
                    timc = r[COL_INTERC].rawtime()
                timd = u''
                if r[COL_INTERD] is not None:
                    timd = r[COL_INTERD].rawtime()
                tine = u''
                if r[COL_INTERE] is not None:
                    tine = r[COL_INTERE].rawtime()
                pcnt = u''
                if r[COL_PASS] is not None:
                    pcnt = str(r[COL_PASS])
                lpass = u''
                if r[COL_LASTSEEN] is not None:
                    lpass = r[COL_LASTSEEN].rawtime()
                slice = [
                    r[COL_COMMENT].decode('utf-8'), wst, tst, tft, tpt,
                    r[COL_PLACE], tima, timb, timc, timd, tine, pcnt, lpass
                ]
                cw.set(u'riders', strops.bibser2bibstr(bib, ser), slice)
        cw.set(u'irtt', u'finished', self.timerstat == 'finished')
        cw.set(u'irtt', u'id', EVENT_ID)
        LOG.debug(u'Saving event config %r', self.configfile)
        with metarace.savefile(self.configfile) as f:
            cw.write(f)

    def get_ridercmdorder(self):
        ret = RIDER_COMMANDS_ORD[0:]
        for i in self.intermeds:
            ret.append(i)
        return ret

    def get_ridercmds(self):
        """Return a dict of rider bib commands for container ui."""
        ret = {}
        for k in RIDER_COMMANDS:
            ret[k] = RIDER_COMMANDS[k]
        for k in self.intermap:
            descr = k
            if self.intermap[k]['descr']:
                descr = self.intermap[k]['descr']
            ret[k] = descr
        return ret

    def get_startlist(self):
        """Return a list of bibs in the rider model as b.s."""
        ret = []
        for r in self.riders:
            ret.append(strops.bibser2bibstr(r[COL_BIB], r[COL_SERIES]))
        return u' '.join(ret)

    def shutdown(self, win=None, msg='Exiting'):
        """Close event."""
        LOG.debug(u'Event shutdown: %r', msg)
        if not self.readonly:
            self.saveconfig()
        self.winopen = False

    def key_riderno(self, r):
        if r[1] is not None:
            return strops.riderno_key(r[1])
        else:
            return 86400  # maxval

    def key_starttime(self, r):
        if r[1] is not None:
            return int(r[1].truncate(0).timeval)
        else:
            return 86400  # maxval

    def reorder_signon(self):
        """Reorder riders for a sign on."""
        aux = []
        cnt = 0
        for r in self.riders:
            aux.append([cnt, r[COL_BIB]])
            cnt += 1
        if len(aux) > 1:
            aux.sort(key=self.key_riderno)
            self.riders.reorder([a[0] for a in aux])
        return cnt

    def reorder_startlist(self):
        """Reorder riders for a startlist."""
        aux = []
        cnt = 0
        for r in self.riders:
            aux.append([cnt, r[COL_WALLSTART]])
            cnt += 1
        if len(aux) > 1:
            aux.sort(key=self.key_starttime)
            self.riders.reorder([a[0] for a in aux])
        return cnt

    def signon_report(self):
        """Return a signon report."""
        ret = []
        sec = report.signon_list(u'signon')
        self.reorder_signon()
        for r in self.riders:
            cmt = r[COL_COMMENT].decode('utf-8')
            sec.lines.append([
                cmt, r[COL_BIB].decode('utf-8'), r[COL_NAMESTR].decode('utf-8')
            ])
        ret.append(sec)
        return ret

    def startlist_report(self):
        """Return a startlist report."""
        self.reorder_startlist()
        ret = []
        if len(self.cats) > 1 and not self.onestartlist:
            for c in self.cats:
                if c:
                    ret.extend(self.startlist_report_gen(c))
                    ret.append(report.pagebreak(0.05))
        else:
            ret = self.startlist_report_gen()
        return ret

    def startlist_report_gen(self, cat=None):
        catnamecache = {}
        catname = u''
        subhead = u''
        if cat is not None:
            dbr = self.meet.rdb.getrider(cat, u'cat')
            if dbr is not None:
                catname = self.meet.rdb.getvalue(dbr, riderdb.COL_FIRST)
                subhead = self.meet.rdb.getvalue(dbr, riderdb.COL_LAST)
        else:
            cat = u''  # match all riders

        if self.onestartlist:
            for rc in self.get_catlist():
                dbr = self.meet.rdb.getrider(rc, u'cat')
                if dbr is not None:
                    cname = self.meet.rdb.getvalue(
                        dbr, riderdb.COL_FIRST)  # already decode
                    if cname:
                        catnamecache[rc] = cname
        """Return a startlist report (rough style)."""
        ret = []
        sec = report.rttstartlist(u'startlist')
        sec.heading = u'Startlist'
        if catname:
            sec.heading += u': ' + catname
            sec.subheading = subhead
        rcnt = 0
        cat = self.ridercat(cat)
        lt = None
        for r in self.riders:
            rcat = r[COL_CAT].decode('utf-8').upper()
            if cat == u'' or rcat == cat:
                rcnt += 1
                ucicode = None
                ## replace with ridermap
                dbr = self.meet.rdb.getrider(r[COL_BIB], r[COL_SERIES])
                if dbr is not None:
                    ucicode = self.meet.rdb.getvalue(dbr, riderdb.COL_UCICODE)
                    nat = self.meet.rdb.getvalue(
                        dbr, riderdb.COL_NOTE)[0:3].upper()
                    if nat:
                        ucicode = nat
                ## to here
                bstr = r[COL_BIB].decode('utf-8').upper()
                stxt = u''
                if r[COL_WALLSTART] is not None:
                    stxt = r[COL_WALLSTART].meridiem()
                    if lt is not None:
                        if r[COL_WALLSTART] - lt > self.startgap:
                            sec.lines.append([None, None, None])  # GAP!!
                    lt = r[COL_WALLSTART]
                nstr = r[COL_NAMESTR]
                cstr = None
                if self.onestartlist and r[COL_CAT] != cat:  # show if not
                    cstr = r[COL_CAT].decode('utf-8')
                    if cstr in catnamecache and len(catnamecache[cstr]) < 8:
                        cstr = catnamecache[cstr]
                sec.lines.append([stxt, bstr, nstr, ucicode, u'____', cstr])
                if cstr in [u'MB', u'WB']:
                    # lookup pilot - series lookup
                    dbr = self.meet.rdb.getrider(r[COL_BIB], u'pilot')
                    if dbr is not None:
                        puci = self.meet.rdb.getvalue(dbr, riderdb.COL_UCICODE)
                        pnam = strops.listname(
                            self.meet.rdb.getvalue(dbr, riderdb.COL_FIRST),
                            self.meet.rdb.getvalue(dbr, riderdb.COL_LAST),
                            self.meet.rdb.getvalue(dbr, riderdb.COL_CLUB))
                        sec.lines.append([u'', u'', pnam, puci, u'', u'pilot'])

        ret.append(sec)
        if rcnt > 1:
            sec = report.bullet_text(u'ridercnt')
            sec.lines.append([u'', u'Total riders: ' + unicode(rcnt)])
            ret.append(sec)
        return ret

    def sort_arrival(self, model, i1, i2, data=None):
        """Sort model by all arrivals."""
        v1 = model.get_value(i1, COL_ETA)
        v2 = model.get_value(i2, COL_ETA)
        if v1 is not None and v2 is not None:
            return cmp(v1, v2)
        else:
            if v1 is None and v2 is None:
                return 0  # same
            else:  # nones are filtered in list traversal
                if v1 is None:
                    return 1
                else:
                    return -1

    def sort_finishtod(self, model, i1, i2, data=None):
        """Sort model on finish tod, then start time."""
        t1 = model.get_value(i1, COL_TODFINISH)
        t2 = model.get_value(i2, COL_TODFINISH)
        if t1 is not None and t2 is not None:
            return cmp(t1, t2)
        else:
            if t1 is None and t2 is None:
                # go by wall start
                s1 = model.get_value(i1, COL_WALLSTART)
                s2 = model.get_value(i2, COL_WALLSTART)
                if s1 is not None and s2 is not None:
                    return cmp(s1, s2)
                else:
                    if s1 is None and s2 is None:
                        return 0
                    elif s1 is None:
                        return 1
                    else:
                        return -1
            else:
                if t1 is None:
                    return 1
                else:
                    return -1

    def arrival_report(self, limit=0):
        """Return an arrival report."""
        ret = []
        ###return ret
        cmod = gtk.TreeModelSort(self.riders)
        cmod.set_sort_func(COL_TODFINISH, self.sort_arrival)
        cmod.set_sort_column_id(COL_TODFINISH, gtk.SORT_ASCENDING)
        sec = report.section(u'arrivals')
        intlbl = None
        if self.showinter is not None:
            intlbl = u'Inter'
        sec.heading = u'Riders On Course'
        sec.footer = u'* denotes projected finish time.'
        # this is probably not required until intermeds available

        sec.colheader = [None, None, None, intlbl, u'Finish', u'Avg']
        sec.lines = []
        nowtime = tod.now()
        for r in cmod:
            plstr = r[COL_PLACE]
            bstr = r[COL_BIB].decode('utf-8')
            nstr = r[COL_NAMESTR].decode('utf-8')
            turnstr = u''
            ets = u''
            speedstr = u''
            rankstr = u''
            noshow = False
            cat = self.ridercat(r[COL_CAT].decode('utf-8'))
            i = self.getiter(r[COL_BIB], r[COL_SERIES])
            if plstr.isdigit():  # rider placed at finish
                ## only show for a short while
                until = r[COL_TODFINISH] + ARRIVALTIMEOUT
                if nowtime < until:
                    et = self.getelapsed(i)
                    ets = et.rawtime(self.precision)
                    rankstr = u'(' + plstr + u'.)'
                    speedstr = u''
                    # cat distance should override this
                    if self.meet.distance is not None:
                        speedstr = et.speedstr(1000.0 * self.meet.distance)
                else:
                    noshow = True
                    speedstr = u''
            elif r[COL_ETA] is not None:
                # append km mark if available
                if r[COL_PASS] > 0:
                    nstr += (u' @ km' + unicode(r[COL_PASS]))
                # projected finish time
                ets = u'*' + r[COL_ETA].rawtime(self.precision)

            if self.showinter is not None and self.showinter in self.ischem and self.ischem[
                    self.showinter] is not None:
                # show time at the turnaround
                trk = self.inters[self.showinter][cat].rank(
                    r[COL_BIB], r[COL_SERIES])
                if trk is not None:
                    tet = self.inters[self.showinter][cat][trk][0]
                    tplstr = unicode(trk + 1)
                    trankstr = u' (' + tplstr + u'.)'
                    turnstr = tet.rawtime(self.precision) + trankstr
                    if not speedstr:
                        # override speed from turn
                        speedstr = u''
                        dist = self.ischem[self.showinter][u'dist']
                        if dist is not None:
                            speedstr = tet.speedstr(1000.0 * dist)
                else:
                    pass

            if not noshow:
                if ets or speedstr:  # only add riders with an estimate
                    sec.lines.append(
                        [rankstr, bstr, nstr, turnstr, ets, speedstr])

        if len(sec.lines) > 0:
            #if limit > 0 and len(sec.lines) > limit:
            #sec.lines = sec.lines[0:limit]
            ret.append(sec)
        return ret

    def camera_report(self):
        """Return a judges report."""
        ret = []
        cmod = gtk.TreeModelSort(self.riders)
        cmod.set_sort_func(COL_TODFINISH, self.sort_finishtod)
        cmod.set_sort_column_id(COL_TODFINISH, gtk.SORT_ASCENDING)
        lcount = 0
        count = 1
        sec = report.section()
        sec.heading = u'Judges Report'
        sec.colheader = [u'Hit', None, None, u'Start', u'Fin', u'Net']

        for r in cmod:
            bstr = strops.bibser2bibstr(r[COL_BIB].decode('utf-8'),
                                        r[COL_SERIES].decode('utf-8'))
            nstr = r[COL_NAMESTR].decode('utf-8')
            plstr = r[COL_PLACE].decode('utf-8')
            rkstr = u''
            if plstr and plstr.isdigit():
                rk = int(plstr)
                if rk < 6:  # annotate top 5 places
                    rkstr = u'(' + plstr + u'.)'
            sts = u'-'
            if r[COL_TODSTART] is not None:
                sts = r[COL_TODSTART].rawtime(2)
            elif r[COL_WALLSTART] is not None:
                sts = r[COL_WALLSTART].rawtime(0) + u'   '
            fts = u'-'
            if r[COL_TODFINISH] is not None:
                fts = r[COL_TODFINISH].rawtime(2)
            i = self.getiter(r[COL_BIB], r[COL_SERIES])
            et = self.getelapsed(i)
            ets = u'-'
            hits = u''
            if et is not None:
                ets = et.rawtime(self.precision)
                hits = unicode(count)
                if rkstr:
                    hits += u' ' + rkstr
                count += 1
            elif r[COL_COMMENT] != u'':
                hits = r[COL_COMMENT].decode('utf-8')
            sec.lines.append([hits, bstr, nstr, sts, fts, ets, rkstr])
            lcount += 1
            if lcount % 10 == 0:
                sec.lines.append([None, None, None])

        ret.append(sec)
        return ret

    def points_report(self):
        """Return the points tally report."""
        ret = []
        aux = []
        cnt = 0
        for tally in self.tallys:
            sec = report.section()
            sec.heading = self.tallymap[tally][u'descr']
            sec.units = u'pt'
            tallytot = 0
            aux = []
            for bib in self.points[tally]:
                r = self.getrider(bib)
                tallytot += self.points[tally][bib]
                aux.append([
                    self.points[tally][bib],
                    strops.riderno_key(bib),
                    [
                        None, r[COL_BIB], r[COL_NAMESTR],
                        strops.truncpad(str(self.pointscb[tally][bib]),
                                        10,
                                        elipsis=False), None,
                        str(self.points[tally][bib])
                    ], self.pointscb[tally][bib]
                ])
            aux.sort(sort_tally)
            for r in aux:
                sec.lines.append(r[2])
            sec.lines.append([None, None, None])
            sec.lines.append([None, None, u'Total Points: ' + str(tallytot)])
            ret.append(sec)

        if len(self.bonuses) > 0:
            sec = report.section()
            sec.heading = u'Stage Bonuses'
            sec.units = u'sec'
            aux = []
            for bib in self.bonuses:
                r = self.getrider(bib)
                aux.append([
                    self.bonuses[bib],
                    strops.riderno_key(bib),
                    [
                        None, r[COL_BIB], r[COL_NAMESTR], None, None,
                        str(int(self.bonuses[bib].truncate(0).timeval))
                    ], 0, 0, 0
                ])
            aux.sort(sort_tally)
            for r in aux:
                sec.lines.append(r[2])
            ret.append(sec)
        return ret

    def catresult_report(self):
        """Return a categorised result report."""
        ret = []
        for cat in self.cats:
            if not cat:
                continue  # ignore empty and None cat
            ret.extend(self.single_catresult(cat))
        return ret

    def single_catresult(self, cat=u''):
        ret = []
        catname = cat  # fallback emergency, cat is never '' here
        subhead = u''
        distance = self.meet.distance  # fall on meet dist
        dbr = self.meet.rdb.getrider(cat, u'cat')
        if dbr is not None:
            catname = self.meet.rdb.getvalue(
                dbr, riderdb.COL_FIRST)  # already decode
            subhead = self.meet.rdb.getvalue(dbr, riderdb.COL_LAST)
            dist = self.meet.rdb.getvalue(dbr, riderdb.COL_REFID)
            try:
                distance = float(dist)
            except:
                LOG.warning(u'Invalid distance %r for cat %r', dist, cat)
        sec = report.section(cat + u'result')
        rsec = sec
        ret.append(sec)
        ct = None
        lt = None
        lpstr = None
        totcount = 0
        dnscount = 0
        dnfcount = 0
        hdcount = 0
        fincount = 0
        for r in self.riders:  # scan whole list even though cat are sorted.
            if cat == u'' or cat == self.ridercat(r[COL_CAT].decode('utf-8')):
                placed = False
                totcount += 1
                i = self.getiter(r[COL_BIB], r[COL_SERIES])
                ft = self.getelapsed(i)
                bstr = r[COL_BIB].decode('utf-8')
                nstr = r[COL_NAMESTR].decode('utf-8')
                cstr = u''
                if cat == u'':  # categorised result does not need cat
                    cstr = r[COL_CAT].decode('utf-8')
                # this should be inserted separately in specific reports
                ucicode = None
                ## replace with rmap lookup
                dbr = self.meet.rdb.getrider(r[COL_BIB], r[COL_SERIES])
                if dbr is not None:
                    ucicode = self.meet.rdb.getvalue(dbr, riderdb.COL_UCICODE)
                ## to here
                if ucicode:
                    ## overwrite category string
                    cstr = ucicode
                if ct is None:
                    ct = ft
                pstr = None
                if r[COL_PLACE] != u'' and r[COL_PLACE].isdigit():
                    pstr = r[COL_PLACE] + u'.'
                    fincount += 1  # only count placed finishers
                    placed = True
                else:
                    pstr = r[COL_COMMENT]
                    # 'special' dnfs
                    if pstr == u'dns':
                        dnscount += 1
                    elif pstr == u'otl':
                        hdcount += 1
                    else:
                        if pstr:  # commented dnf
                            dnfcount += 1
                    if pstr:
                        placed = True
                        if lpstr != pstr:
                            ## append an empty row
                            sec.lines.append(
                                [None, None, None, None, None, None])
                            lpstr = pstr
                tstr = None
                if ft is not None:
                    tstr = ft.rawtime(self.precision)
                dstr = None
                if ct is not None and ft is not None and ct != ft:
                    dstr = u'+' + (ft - ct).rawtime(1)
                if placed:
                    sec.lines.append([pstr, bstr, nstr, cstr, tstr, dstr])
                    if cat in [u'WB', u'MB']:  #also look up pilots
                        # lookup pilot - series lookup
                        dbr = self.meet.rdb.getrider(r[COL_BIB], u'pilot')
                        if dbr is not None:
                            puci = self.meet.rdb.getvalue(
                                dbr, riderdb.COL_UCICODE)
                            pnam = strops.listname(
                                self.meet.rdb.getvalue(dbr, riderdb.COL_FIRST),
                                self.meet.rdb.getvalue(dbr, riderdb.COL_LAST),
                                self.meet.rdb.getvalue(dbr, riderdb.COL_CLUB))
                            sec.lines.append(
                                [u'', u'pilot', pnam, puci, u'', u''])

        residual = totcount - (fincount + dnfcount + dnscount + hdcount)

        if self.timerstat == u'finished':  # THIS OVERRIDES RESIDUAL
            sec.heading = u'Result'
        else:
            if self.racestat == u'prerace':
                sec.heading = u''  # anything better?
            else:
                if residual > 0:
                    sec.heading = u'Standings'
                else:
                    sec.heading = u'Provisional Result'

        # Race metadata / UCI comments
        sec = report.bullet_text(u'uci' + cat)
        if ct is not None:
            if distance is not None:
                avgprompt = u'Average speed of the winner: '
                if residual > 0:
                    avgprompt = u'Average speed of the leader: '
                sec.lines.append(
                    [None, avgprompt + ct.speedstr(1000.0 * distance)])
        sec.lines.append(
            [None, u'Number of starters: ' + unicode(totcount - dnscount)])
        if hdcount > 0:
            sec.lines.append([
                None,
                u'Riders finishing out of time limits: ' + unicode(hdcount)
            ])
        if dnfcount > 0:
            sec.lines.append(
                [None, u'Riders abandoning the race: ' + unicode(dnfcount)])
        ret.append(sec)

        # finish report title manipulation
        if catname:
            rsec.heading += u': ' + catname
            rsec.subheading = subhead
            ret.append(report.pagebreak())
        return ret

    def result_report(self):
        """Return a race result report."""
        ret = []
        # dump results
        self.placexfer()  # ensure all cat places are filled
        # also re-announces!
        if self.timerstat == u'running':
            # until final, show last few
            ret.extend(self.arrival_report(self.arrivalcount))
        if len(self.cats) > 1:
            ret.extend(self.catresult_report())
        else:
            ret.extend(self.single_catresult())

        # Decisions of commissaires panel
        if len(self.comment) > 0:
            sec = report.bullet_text(u'comms')
            sec.heading = u'Decisions of the Commissaires Panel'
            for cl in self.comment:
                sec.lines.append([None, cl.strip()])
            ret.append(sec)
        return ret

    def startlist_gen(self, cat=u''):
        """Generator function to export a startlist."""
        mcat = self.ridercat(cat)
        self.reorder_startlist()
        for r in self.riders:
            if mcat == u'' or mcat == self.ridercat(r[COL_CAT]):
                start = u''
                if r[COL_WALLSTART] is not None:
                    start = r[COL_WALLSTART].rawtime(0)
                bib = r[COL_BIB]
                series = r[COL_SERIES]
                name = u''
                ## replace with rmap lookup
                dbr = self.meet.rdb.getrider(bib, series)
                if dbr is not None:
                    name = strops.listname(
                        self.meet.rdb.getvalue(dbr, riderdb.COL_FIRST),
                        self.meet.rdb.getvalue(dbr, riderdb.COL_LAST), None)
                ## to here
                cat = r[COL_CAT]
                yield [start, bib, series, name, cat]

    def lifexport(self):
        return []

    def get_elapsed(self):
        return None

    def result_gen(self, cat=u''):
        """Generator function to export a final result."""
        self.placexfer()
        mcat = self.ridercat(cat)
        rcount = 0
        lrank = None
        lpl = None
        for r in self.riders:
            if mcat == u'' or mcat == self.ridercat(r[COL_CAT]):
                i = self.getiter(r[COL_BIB], r[COL_SERIES])
                ft = self.getelapsed(i)
                if ft is not None:
                    ft = ft.truncate(2)  # RETAIN Hundredths
                bib = r[COL_BIB].decode(u'utf-8')
                crank = None
                rank = None
                if r[COL_PLACE].isdigit():
                    rcount += 1
                    rank = int(r[COL_PLACE])
                    if rank != lrank:
                        crank = rcount
                    else:
                        crank = lpl
                    lpl = crank
                    lrank = rank
                else:
                    crank = r[COL_COMMENT].decode(u'utf-8')
                extra = None
                if r[COL_WALLSTART] is not None:
                    extra = r[COL_WALLSTART]

                bonus = None
                penalty = None  # should stay none for IRTT - ft contains
                # any stage penalty
                yield [crank, bib, ft, bonus, penalty]

    def main_loop(self, cb):
        """Run callback once in main loop idle handler."""
        cb(u'')
        return False

    def set_syncstart(self, start=None, lstart=None):
        if start is not None:
            if lstart is None:
                lstart = start
            self.start = start
            self.lstart = lstart
            self.timerstat = u'running'
            self.meet.stat_but.buttonchg(uiutil.bg_armstart, u'Running')
            self.meet.stat_but.set_sensitive(True)
            LOG.info(u'Timer sync @ %s', start.rawtime(2))
            self.sl.toidle()
            self.fl.toidle()

    def rfidinttrig(self, lr, e, bibstr, bib, series):
        """Register Intermediate RFID crossing."""
        st = lr[COL_WALLSTART]
        if lr[COL_TODSTART] is not None:
            st = lr[COL_TODSTART]
        if st is not None and e > st and e - st > STARTFUDGE:
            if lr[COL_TODFINISH] is None:
                # Got a rider on course, find out where they _should_ be
                self.doannounce = True
                elap = e - st
                # find first matching split point
                split = None
                for isplit in self.interloops[e.source]:
                    minelap = self.ischem[isplit][u'minelap']
                    maxelap = self.ischem[isplit][u'maxelap']
                    if lr[isplit] is None:
                        if elap > minelap and elap < maxelap:
                            split = isplit
                            break

                if split is not None:
                    # save and announce arrival at intermediate
                    nri = self.getiter(bib, series)
                    rank = self.setinter(nri, e, split)
                    place = u'(' + unicode(rank + 1) + u'.)'
                    namestr = lr[COL_NAMESTR].decode('utf-8')
                    cat = lr[COL_CAT].decode('utf-8')
                    rcat = self.ridercat(cat)
                    # use cat field for split label
                    label = self.ischem[split][u'label']
                    rts = u''
                    rt = self.inters[split][rcat][rank][0]
                    if rt is not None:
                        rts = rt.rawtime(2)
                    ##self.meet.scb.add_rider([place,bib,namestr,label,rts],
                    ##'ttsplit')
                    LOG.info(u'Intermediate %s: %s %s@%s/%s', label, place,
                             bibstr, e.rawtime(2), e.source)
                    lr[COL_ETA] = self.geteta(nri)
                else:
                    LOG.info(u'No match for intermediate: %s@%s/%s', bibstr,
                             e.rawtime(2), e.source)
            else:
                LOG.info(u'Intermediate finished rider: %s@%s/%s', bibstr,
                         e.rawtime(2), e.source)
        else:
            LOG.info(u'Intermediate rider not yet on course: %s@%s/%s', bibstr,
                     e.rawtime(2), e.source)
        return False

    def start_by_rfid(self, lr, e, bibstr):
        # ignore already finished rider
        if lr[COL_TODFINISH] is not None:
            LOG.info(u'Finished rider on startloop: %s:%s@%s/%s', bibstr,
                     e.chan, e.rawtime(2), e.source)
            return False

        # ignore passings if start not properly armed
        if not self.sloppystart:
            if lr[COL_TODSTART] is not None:
                LOG.info(u'Started rider on startloop: %s:%s@%s/%s', bibstr,
                         e.chan, e.rawtime(2), e.source)
                return False
            # compare wall and actual starts
            if lr[COL_WALLSTART] is not None:
                wv = lr[COL_WALLSTART].timeval
                ev = e.timeval
                if abs(wv - ev) > 5:  # differ by more than 5 secs
                    LOG.info(u'Ignored start time: %s:%s@%s/%s != %s', bibstr,
                             e.chan, e.rawtime(2), e.source,
                             lr[COL_WALLSTART].rawtime(0))
                    return False

        LOG.info(u'Set start time: %s:%s@%s/%s', bibstr, e.chan, e.rawtime(2),
                 e.source)
        i = self.getiter(lr[COL_BIB], lr[COL_SERIES])
        self.settimes(i, tst=e)
        return False

    def setrftime(self, bib, rank, rftime, bonus=None):
        """Override rider result from CSV Data."""
        LOG.info(u'Set finish time from CSV: ' + bib + u'@' +
                 rftime.rawtime(2))
        i = self.getiter(bib, u'')
        self.settimes(i, tft=rftime)

    def setriderval(self, bib, rank, bunch, bonus=None):
        """Hook for CSV import - assume bunch holds elapsed only."""
        LOG.debug(u'Set rider val by elapsed time: ' + bib + u'/' +
                  bunch.rawtime(2))
        i = self.getiter(bib, u'')
        self.settimes(i, tst=tod.ZERO, tft=bunch)

    def finish_by_rfid(self, lr, e, bibstr):
        if lr[COL_TODFINISH] is not None:
            LOG.info(u'Finished rider seen on finishloop: %s:%s@%s/%s', bibstr,
                     e.chan, e.rawtime(2), e.source)
            return False

        if lr[COL_WALLSTART] is None and lr[COL_TODSTART] is None:
            LOG.warning(u'No start time for rider at finish: %s:%s@%s/%s',
                        bibstr, e.chan, e.rawtime(2), e.source)
            return False

        cat = self.ridercat(lr[COL_CAT])
        finishpass = self.finishpass
        if cat in self.catlaps:
            finishpass = self.catlaps[cat]
            LOG.debug(u'%r laps=%s, cat=%r', bibstr, finishpass, cat)

        if finishpass is None:
            st = lr[COL_WALLSTART]
            if lr[COL_TODSTART] is not None:
                st = lr[COL_TODSTART]  # use tod if avail
            if e > st + self.minelap:
                LOG.info(u'Set finish time: %s:%s@%s/%s', bibstr, e.chan,
                         e.rawtime(2), e.source)
                i = self.getiter(lr[COL_BIB], lr[COL_SERIES])
                self.settimes(i, tst=lr[COL_TODSTART], tft=e)
            else:
                LOG.info(u'Ignored early finish: %s:%s@%s/%s', bibstr, e.chan,
                         e.rawtime(2), e.source)
        else:
            lt = lr[COL_WALLSTART]
            if lr[COL_TODSTART] is not None:
                lt = lr[COL_TODSTART]
            if lr[COL_LASTSEEN] is not None and lr[COL_LASTSEEN] > lt:
                lt = lr[COL_LASTSEEN]
            if e > lt + self.minelap:
                lr[COL_PASS] += 1
                nc = lr[COL_PASS]
                if nc >= finishpass:
                    LOG.info(u'Set finish lap time: %s:%s@%s/%s', bibstr,
                             e.chan, e.rawtime(2), e.source)
                    i = self.getiter(lr[COL_BIB], lr[COL_SERIES])
                    self.settimes(i, tst=lr[COL_TODSTART], tft=e)
                else:
                    LOG.info(u'Lap %s passing: %s:%s@%s/%s', nc, bibstr,
                             e.chan, e.rawtime(2), e.source)
            else:
                LOG.info(u'Ignored short lap: %s:%s@%s/%s', bibstr, e.chan,
                         e.rawtime(2), e.source)

        # save a copy of this passing
        lr[COL_LASTSEEN] = e

        return False

    def timertrig(self, e):
        """Process transponder passing event."""
        if e.refid in [u'', u'255']:
            # Triggers from a decoder are distinguished by source id
            if self.starttrig is not None and e.source == self.starttrig:
                self.start_trig(e)
            else:
                self.fin_trig(e)
            return False

        r = self.meet.rdb.getrefid(e.refid)
        if r is None:
            LOG.info(u'Unknown rider: %s:%s@%s/%s', e.refid, e.chan,
                     e.rawtime(2), e.source)
            return False

        bib = self.meet.rdb.getvalue(r, riderdb.COL_BIB)
        series = self.meet.rdb.getvalue(r, riderdb.COL_SERIES)
        lr = self.getrider(bib, series)
        if lr is not None:
            # distinguish a shared finish / start loop
            okfin = False
            st = lr[COL_WALLSTART]
            if lr[COL_TODSTART] is not None:
                st = lr[COL_TODSTART]
            if st is not None and e > st and e - st > self.minelap:
                okfin = True

            bibstr = strops.bibser2bibstr(bib, series)

            # switch on loop source mode
            if okfin and self.finishloop and e.source == self.finishloop:
                return self.finish_by_rfid(lr, e, bibstr)
            elif self.startloop and e.source == self.startloop:
                return self.start_by_rfid(lr, e, bibstr)
            elif e.source in self.interloops:
                return self.rfidinttrig(lr, e, bibstr, bib, series)
            elif self.finishloop and e.source == self.finishloop:
                # handle the case where suorce matches, but timing is off
                LOG.info(u'Early arrival at finish: %s:%s@%s/%s', bibstr,
                         e.chan, e.rawtime(2), e.source)
                return False

            if lr[COL_TODFINISH] is not None:
                LOG.info(u'Finished rider: %s:%s@%s/%s', bibstr, e.chan,
                         e.rawtime(2), e.source)
                return False

            if self.fl.getstatus() not in [u'armfin']:
                st = lr[COL_WALLSTART]
                if lr[COL_TODSTART] is not None:
                    st = lr[COL_TODSTART]
                if st is not None and e > st and e - st > self.minelap:
                    self.fl.setrider(lr[COL_BIB], lr[COL_SERIES])
                    self.armfinish()
                    LOG.info(u'Arm finish: %s:%s@%s/%s', bibstr, e.chan,
                             e.rawtime(2), e.source)
                else:
                    LOG.info(u'Early arrival at finish: %s:%s@%s/%s', bibstr,
                             e.chan, e.rawtime(2), e.source)
            else:
                LOG.info(u'Finish blocked: %s:%s@%s/%s', bibstr, e.chan,
                         e.rawtime(2), e.source)
        else:
            LOG.info(u'Non-starter: %s:%s@%s/%s', bibstr, e.chan, e.rawtime(2),
                     e.source)
        return False

    def int_trig(self, t):
        """Register intermediate trigger."""
        LOG.info('Intermediate cell: %s', t.rawtime(2))

    def fin_trig(self, t):
        """Register finish trigger."""
        LOG.info(u'Finish trigger %s@%s/%s', t.chan, t.rawtime(2), t.source)
        if self.timerstat == u'running':
            if self.fl.getstatus() == u'armfin':
                bib = self.fl.bibent.get_text()
                series = self.fl.serent.get_text()
                i = self.getiter(bib, series)
                if i is not None:
                    cat = self.ridercat(self.riders.get_value(i, COL_CAT))
                    self.curcat = cat
                    self.settimes(i,
                                  tst=self.riders.get_value(i, COL_TODSTART),
                                  tft=t)
                    self.fl.tofinish()
                    ft = self.getelapsed(i)
                    if ft is not None:
                        self.fl.set_time(ft.timestr(2))
                        rank = self.results[cat].rank(bib, series) + 1
                        self.announce_rider(
                            str(rank),
                            bib,
                            self.riders.get_value(i, COL_NAMESTR),
                            self.riders.get_value(i, COL_SHORTNAME),
                            cat,
                            et=ft)  # announce the raw elapsed time
                        # send a flush hint to minimise display lag
                        self.meet.cmd_announce(u'redraw', u'timer')
                    else:
                        self.fl.set_time(u'[err]')

                else:
                    LOG.error(u'Missing rider at finish')
                    self.sl.toidle()
            else:
                pass
        elif self.timerstat == u'armstart':
            self.set_syncstart(t)

    def start_trig(self, t):
        """Register start trigger."""
        LOG.info(u'Start trigger %s@%s/%s', t.chan, t.rawtime(2), t.source)
        if self.timerstat == u'running':
            # apply start trig to start line rider
            if self.sl.getstatus() == u'armstart':
                i = self.getiter(self.sl.bibent.get_text(),
                                 self.sl.serent.get_text())
                if i is not None:
                    nst = t - self.startdelay
                    self.settimes(i, tst=nst, doplaces=False)
                    self.sl.torunning()
                else:
                    LOG.error(u'Missing rider at start')
                    self.sl.toidle()
            else:
                pass
        elif self.timerstat == u'armstart':
            self.set_syncstart(t, tod.now())

    def alttimertrig(self, e):
        """Handle chronometer callbacks."""
        # note: these impulses are sourced from alttimer device and keyboard
        #       transponder triggers are collected separately in timertrig()
        channo = strops.chan2id(e.chan)
        if channo == 0:
            self.start_trig(e)
        elif channo == 1:
            self.fin_trig(e)
        else:
            LOG.info(u'Alt timer: %s@%s/%s', e.chan, e.rawtime(), e.source)
        return False

    def on_start(self, curoft):
        # use search instead of lookup to avoid the tosw problem
        for r in self.riders:
            ws = r[COL_WALLSTART]
            if ws is not None:
                if curoft + tod.tod(u'30') == ws:
                    bib = r[COL_BIB].decode('utf-8')
                    ser = r[COL_SERIES].decode('utf-8')
                    LOG.info(u'pre-load starter: ' + repr(bib))
                    self.sl.setrider(bib, ser)
                    self.meet.cmd_announce(u'startline', bib)
                    break
                if curoft + tod.tod(u'5') == ws:
                    bib = r[COL_BIB].decode('utf-8')
                    ser = r[COL_SERIES].decode('utf-8')
                    LOG.info(u'Load starter: ' + repr(bib))
                    self.sl.setrider(bib, ser)
                    self.sl.toarmstart()
                    self.start_unload = ws + tod.tod(u'5')
                    break

    def timeout(self):
        """Update slow changing aspects of race."""
        if not self.winopen:
            return False
        if self.timerstat == u'running':
            nowoft = (tod.now() - self.lstart).truncate(0)
            if self.sl.getstatus() in [u'idle', u'load']:
                if nowoft.timeval % 5 == 0:  # every five
                    self.on_start(nowoft)
            else:
                if nowoft == self.start_unload:
                    self.sl.toidle()

            # after manips, then re-set start time
            self.sl.set_time(nowoft.timestr(0))

            # if finish lane loaded, set the elapsed time
            if self.fl.getstatus() in [u'load', u'running', u'armfin']:
                bib = self.fl.bibent.get_text()
                series = self.fl.serent.get_text()
                i = self.getiter(bib, series)
                if i is not None:
                    et = self.getelapsed(i, runtime=True)
                    self.fl.set_time(et.timestr(0))
                    self.announce_rider(u'',
                                        bib,
                                        self.riders.get_value(i, COL_NAMESTR),
                                        self.riders.get_value(
                                            i, COL_SHORTNAME),
                                        self.riders.get_value(i, COL_CAT),
                                        rt=et)  # announce running time

        if self.doannounce:
            self.doannounce = False
            glib.idle_add(self.delayed_announce)
            if self.autoexport:
                glib.idle_add(self.doautoexport)
        return True

    def doautoexport(self, data=None):
        """Run an export process."""
        self.meet.menu_data_results_cb(None)
        return False

    def clearplaces(self):
        """Clear rider places."""
        aux = []
        count = 0
        for r in self.riders:
            r[COL_PLACE] = r[COL_COMMENT]
            aux.append([count, r[COL_BIB], r[COL_COMMENT]])
            count += 1
        if len(aux) > 1:
            aux.sort(sort_dnfs)
            self.riders.reorder([a[0] for a in aux])

    def getrider(self, bib, series=''):
        """Return temporary reference to model row."""
        ret = None
        for r in self.riders:
            if r[COL_BIB] == bib and r[COL_SERIES] == series:
                ret = r
                break
        return ret

    def starttime(self, start=None, bib='', series=''):
        """Adjust start time for the rider."""
        r = self.getrider(bib, series)
        if r is not None:
            r[COL_WALLSTART] = start
            #self.unstart(bib, series, wst=start)

    def delrider(self, bib='', series=''):
        """Delete the specificed rider from the race model."""
        i = self.getiter(bib, series)
        if i is not None:
            self.riders.remove(i)

    def addrider(self, bib='', series=''):
        """Add specified rider to race model."""
        if bib == u'' or self.getrider(bib, series) is None:
            ## could be a rmap lookup here
            nr = [
                bib, series, u'', u'', u'', None, None, None, tod.ZERO, u'',
                u'', None, None, None, None, None, None, None, 0
            ]
            dbr = self.meet.rdb.getrider(bib, series)
            if dbr is not None:
                nr[COL_NAMESTR] = strops.listname(
                    self.meet.rdb.getvalue(dbr, riderdb.COL_FIRST),
                    self.meet.rdb.getvalue(dbr, riderdb.COL_LAST),
                    self.meet.rdb.getvalue(dbr, riderdb.COL_CLUB))
                nr[COL_CAT] = self.meet.rdb.getvalue(dbr, riderdb.COL_CAT)
                nr[COL_SHORTNAME] = strops.fitname(
                    self.meet.rdb.getvalue(dbr, riderdb.COL_FIRST),
                    self.meet.rdb.getvalue(dbr, riderdb.COL_LAST), 12)
            return self.riders.append(nr)
        else:
            return None

    def editcol_cb(self, cell, path, new_text, col):
        """Update value in edited cell."""
        new_text = new_text.strip()
        if col == COL_BIB:
            if new_text.isalnum():
                if self.getrider(new_text,
                                 self.riders[path][COL_SERIES]) is None:
                    self.riders[path][COL_BIB] = new_text
                    dbr = self.meet.rdb.getrider(new_text, self.series)
                    if dbr is not None:
                        nr[COL_NAMESTR] = strops.listname(
                            self.meet.rdb.getvalue(dbr, riderdb.COL_FIRST),
                            self.meet.rdb.getvalue(dbr, riderdb.COL_LAST),
                            self.meet.rdb.getvalue(dbr, riderdb.COL_CLUB))
                        nr[COL_CAT] = self.meet.rdb.getvalue(
                            dbr, riderdb.COL_CAT)
        elif col == COL_PASS:
            if new_text.isdigit():
                self.riders[path][COL_PASS] = int(new_text)
                LOG.debug(u'Adjusted pass count: %r:%r',
                          self.riders[path][COL_BIB],
                          self.riders[path][COL_PASS])
        else:
            self.riders[path][col] = new_text.strip()

    def decode_limit(self, limitstr, elap=None):
        """Decode a limit and finish time into raw bunch time."""
        ret = None
        if limitstr:
            limit = None
            down = False
            if u'+' in limitstr:
                down = True
                limitstr = limitstr.replace(u'+', u'')
            if u'%' in limitstr:
                down = True
                if elap is not None:
                    try:
                        frac = 0.01 * float(limitstr.replace(u'%', u''))
                        limit = tod.tod(int(frac * float(elap.as_seconds())))
                    except Exception:
                        pass
            else:  # assume tod without sanity check
                limit = tod.mktod(limitstr)
                if limit is not None:
                    if elap is not None and limit < elap:
                        down = True  # assume a time less than winner is down
                    else:  # assume raw bunch time, ignore elap
                        pass

            # assign limit discovered above, if possible
            if limit is not None:
                if down:
                    if elap is not None:
                        ret = elap + limit  # down time on finish
                else:
                    ret = limit
            if ret is None:
                LOG.warning(u'Unable to decode time limit: %r', limitstr)
        return ret

    def placexfer(self):
        """Transfer places into model."""
        #note: clearplaces also transfers comments into rank col (dns,dnf)
        self.places = u''
        placelist = []
        self.clearplaces()
        count = 0
        for cat in self.cats:
            ft = None
            if len(self.results[cat]) > 0:
                ft = self.results[cat][0][0]
            limit = None
            if ft is not None and self.timelimit is not None:
                limit = self.decode_limit(self.timelimit, ft)
                if limit is not None:
                    LOG.info(u'Time limit: ' + self.timelimit + u' = ' +
                             limit.rawtime(0) + u', +' +
                             (limit - ft).rawtime(0))
            lt = None
            place = 1
            pcount = 0
            for t in self.results[cat]:
                np = strops.bibser2bibstr(t[0].refid, t[0].index)
                if np in placelist:
                    LOG.error(u'Result for rider %r already in placelist', np)
                    # this is a bad fail - indicates duplicate category entry
                placelist.append(np)
                i = self.getiter(t[0].refid, t[0].index)
                if i is not None:
                    if lt is not None:
                        if lt != t[0]:
                            place = pcount + 1
                    if limit is not None and t[0] > limit:
                        self.riders.set_value(i, COL_PLACE, u'otl')
                        self.riders.set_value(i, COL_COMMENT, u'otl')
                    else:
                        self.riders.set_value(i, COL_PLACE, str(place))
                    j = self.riders.get_iter(count)
                    self.riders.swap(j, i)
                    count += 1
                    pcount += 1
                    lt = t[0]
                else:
                    LOG.error('Extra result for rider %r', np)

        # check counts for racestat
        self.racestat = u'prerace'
        fullcnt = len(self.riders)
        placed = 0
        for r in self.riders:
            if r[COL_PLACE] and r[COL_PLACE] in [u'dns', u'dnf', u'dsq']:
                r[COL_ETA] = None
            else:
                i = self.getiter(r[COL_BIB], r[COL_SERIES])
                r[COL_ETA] = self.geteta(i)
                #LOG.debug(u'Set ETA: ' + repr(r[COL_ETA]))
                # if start set:
                # transfer out finish time to ETA
                # or use inters to establish ETA
            if r[COL_PLACE]:
                placed += 1
        LOG.debug(u'placed = ' + unicode(placed) + ', total = ' +
                  unicode(fullcnt))
        LOG.debug(u'place list = ' + repr(placelist))
        if placed > 0:
            if placed < fullcnt:
                self.racestat = u'virtual'
            else:
                self.places = u' '.join(placelist)
                if self.timerstat == u'finished':
                    self.racestat = u'final'
                else:
                    self.racestat = u'provisional'
        LOG.debug(u'Racestat set to: ' + repr(self.racestat))

        # pass two: compute any intermediates
        self.bonuses = {}  # bonuses are global to stage
        for c in self.tallys:  # points are grouped by tally
            self.points[c] = {}
        for c in self.contests:
            self.assign_places(c)

        self.doannounce = True

    def get_placelist(self):
        """Return place list."""
        # assume this follows a place sorting.
        fp = None
        ret = ''
        for r in self.riders:
            if r[COL_PLACE]:
                #bibstr = strops.bibser2bibstr(r[COL_BIB], r[COL_SERIES])
                bibstr = r[COL_BIB]  # bibstr will fail later on
                if r[COL_PLACE] != fp:
                    ret += ' ' + bibstr
                else:
                    ret += '-' + bibstr
        return ret

    def get_starters(self):
        """Return a list of riders that 'started' the race."""
        ret = []
        for r in self.riders:
            if r[COL_COMMENT] != 'dns':
                ret.append(r[COL_BIB])
        return ' '.join(ret)

    def assign_places(self, contest):
        """Transfer points and bonuses into the named contest."""
        ## ERROR bib.ser will fail!
        # fetch context meta infos
        src = self.contestmap[contest]['source']
        if src not in RESERVED_SOURCES and src not in self.intermeds:
            LOG.info('Invalid intermediate source: ' + repr(src) +
                     ' in contest: ' + repr(contest))
            return
        tally = self.contestmap[contest]['tally']
        bonuses = self.contestmap[contest]['bonuses']
        points = self.contestmap[contest]['points']
        allsrc = self.contestmap[contest]['all_source']
        allpts = 0
        allbonus = tod.ZERO
        if allsrc:
            if len(points) > 0:
                allpts = points[0]
            if len(bonuses) > 0:
                allbonus = bonuses[0]
        placestr = ''
        if src == 'fin':
            placestr = self.get_placelist()
            LOG.info('Using placestr = ' + repr(placestr))
        elif src == 'reg':
            placestr = self.get_startlist()
        elif src == 'start':
            placestr = self.get_starters()
        else:
            placestr = self.intermap[src]['places']
        placeset = set()
        idx = 0
        for placegroup in placestr.split():
            curplace = idx + 1
            for bib in placegroup.split('-'):
                if bib not in placeset:
                    placeset.add(bib)
                    r = self.getrider(bib)
                    if r is None:
                        LOG.error('Invalid rider in place string.')
                        break
                        #self.addrider(bib)
                        #r = self.getrider(bib)
                    idx += 1
                    if allsrc:  # all listed places get same pts/bonus..
                        if allbonus is not tod.ZERO:
                            if bib in self.bonuses:
                                self.bonuses[bib] += allbonus
                            else:
                                self.bonuses[bib] = allbonus
                        if allpts != 0:
                            if bib in self.points[tally]:
                                self.points[tally][bib] += allpts
                            else:
                                self.points[tally][bib] = allpts
                                self.pointscb[tally][bib] = [0, 0, 0]
                            # No countback for all_source entries
                    else:  # points/bonus as per config
                        if len(bonuses) >= curplace:  # bonus is vector
                            if bib in self.bonuses:
                                self.bonuses[bib] += bonuses[curplace - 1]
                            else:
                                self.bonuses[bib] = bonuses[curplace - 1]
                        if tally and len(points) >= curplace:  # points vector
                            if bib in self.points[tally]:
                                self.points[tally][bib] += points[curplace - 1]
                            else:
                                self.points[tally][bib] = points[curplace - 1]
                                self.pointscb[tally][bib] = [0, 0, 0]
                            if curplace <= 3:  # countback on 1-3
                                self.pointscb[tally][bib][curplace - 1] += 1
                else:
                    LOG.warning('Duplicate no. = ' + str(bib) + ' in ' +
                                repr(contest) + ' places.')

    def getiter(self, bib, series=''):
        """Return temporary iterator to model row."""
        i = self.riders.get_iter_first()
        while i is not None:
            if self.riders.get_value(i,
                                     COL_BIB) == bib and self.riders.get_value(
                                         i, COL_SERIES) == series:
                break
            i = self.riders.iter_next(i)
        return i

    #def unstart(self, bib='', series='', wst=None):
    #"""Register a rider as not yet started."""
    #idx = strops.bibser2bibstr(bib, series)
    #self.unstarters[idx] = wst

    #def oncourse(self, bib='', series=''):
    #"""Remove rider from the not yet started list."""
    #pass
    #idx = strops.bibser2bibstr(bib, series)
    #if idx in self.unstarters:
    #del(self.unstarters[idx])

    def dnfriders(self, biblist='', code='dnf'):
        """Remove each rider from the race with supplied code."""
        recalc = False
        for bibstr in biblist.split():
            bib, ser = strops.bibstr2bibser(bibstr)
            r = self.getrider(bib, ser)
            if r is not None:
                r[COL_COMMENT] = code
                nri = self.getiter(bib, ser)
                self.settimes(nri, doplaces=False)
                recalc = True
            else:
                LOG.warning('Unregistered Rider ' + str(bibstr) +
                            ' unchanged.')
        if recalc:
            self.placexfer()
        return False

    def setinter(self, iter, imed=None, inter=None):
        """Update the intermediate time for this rider and return rank."""
        bib = self.riders.get_value(iter, COL_BIB)
        series = self.riders.get_value(iter, COL_SERIES)
        cat = self.ridercat(self.riders.get_value(iter, COL_CAT))
        ret = None

        # fetch handles
        res = self.inters[inter][cat]

        # clear result for this bib
        res.remove(bib, series)

        # save intermed tod to rider model
        self.riders.set_value(iter, inter, imed)
        tst = self.riders.get_value(iter, COL_TODSTART)
        wst = self.riders.get_value(iter, COL_WALLSTART)

        # determine start time
        if imed is not None:
            if tst is not None:  # got a start trigger
                res.insert(imed - tst, None, bib, series)
                ret = res.rank(bib, series)
            elif wst is not None:  # start on wall time
                res.insert(imed - wst, None, bib, series)
                ret = res.rank(bib, series)
            else:
                LOG.error('No start time for intermediate ' +
                          strops.bibser2bibstr(bib, series))
        return ret

    def setpasses(self, iter, passes=None):
        """Set rider pass count."""
        self.riders.set_value(iter, COL_PASS, passes)

    def settimes(self,
                 iter,
                 wst=None,
                 tst=None,
                 tft=None,
                 pt=None,
                 doplaces=True):
        """Transfer race times into rider model."""
        bib = self.riders.get_value(iter, COL_BIB)
        series = self.riders.get_value(iter, COL_SERIES)
        cat = self.ridercat(self.riders.get_value(iter, COL_CAT))
        #LOG.debug('Check: ' + repr(bib) + ', ' + repr(series)
        #+ ', ' + repr(cat))

        # clear result for this bib
        self.results[cat].remove(bib, series)

        # assign tods
        if wst is not None:  # Don't clear a set wall start time!
            self.riders.set_value(iter, COL_WALLSTART, wst)
        else:
            wst = self.riders.get_value(iter, COL_WALLSTART)
        #self.unstart(bib, series, wst)	# reg ignorer
        # but allow others to be cleared no worries
        oft = self.riders.get_value(iter, COL_TODFINISH)
        self.riders.set_value(iter, COL_TODSTART, tst)
        self.riders.set_value(iter, COL_TODFINISH, tft)

        if pt is not None:  # Don't clear penalty either
            self.riders.set_value(iter, COL_TODPENALTY, pt)
        else:
            pt = self.riders.get_value(iter, COL_TODPENALTY)

        # save result
        if tft is not None:
            self.onestart = True
            if tst is not None:  # got a start trigger
                self.results[cat].insert(
                    (tft - tst).truncate(self.precision) + pt, None, bib,
                    series)
            elif wst is not None:  # start on wall time
                self.results[cat].insert(
                    (tft - wst).truncate(self.precision) + pt, None, bib,
                    series)
            else:
                LOG.error('No start time for rider ' +
                          strops.bibser2bibstr(bib, series))
        elif tst is not None:
            #self.oncourse(bib, series)	# started but not finished
            pass

        # if reqd, do places
        if doplaces and oft != tft:
            self.placexfer()

    def bibent_cb(self, entry, tp):
        """Bib entry callback."""
        bib = tp.bibent.get_text().strip()
        series = tp.serent.get_text().strip()
        namestr = self.lanelookup(bib, series)
        if namestr is not None:
            tp.biblbl.set_text(self.lanelookup(bib, series))
            tp.toload()

    def tment_cb(self, entry, tp):
        """Manually register a finish time."""
        thetime = tod.mktod(entry.get_text())
        if thetime is not None:
            bib = tp.bibent.get_text().strip()
            series = tp.serent.get_text().strip()
            if bib != '':
                self.armfinish()
                self.meet.alttimer.trig(thetime, chan=1, index='MANU')
                entry.set_text('')
                tp.grab_focus()
        else:
            LOG.error('Invalid finish time.')

    def lanelookup(self, bib=None, series=''):
        """Prepare name string for timer lane."""
        rtxt = None
        r = self.getrider(bib, series)
        if r is None:
            LOG.info('Non starter specified: ' + repr(bib))
        else:
            rtxt = strops.truncpad(r[COL_NAMESTR], 35)
        return rtxt

    def time_context_menu(self, widget, event, data=None):
        """Popup menu for result list."""
        self.context_menu.popup(None, None, None, event.button, event.time,
                                selpath)

    def treeview_button_press(self, treeview, event):
        """Set callback for mouse press on model view."""
        if event.button == 3:
            pathinfo = treeview.get_path_at_pos(int(event.x), int(event.y))
            if pathinfo is not None:
                path, col, cellx, celly = pathinfo
                treeview.grab_focus()
                treeview.set_cursor(path, col, 0)
                self.context_menu.popup(None, None, None, event.button,
                                        event.time)
                return True
        return False

    def tod_context_print_activate_cb(self, menuitem, data=None):
        """Print times for selected rider."""
        LOG.info(u'Print times not implemented.')
        pass

    def tod_context_dns_activate_cb(self, menuitem, data=None):
        """Register rider as non-starter."""
        sel = self.view.get_selection().get_selected()
        if sel is not None:
            i = sel[1]  # grab off row iter
            bib = self.riders.get_value(i, COL_BIB)
            series = self.riders.get_value(i, COL_SERIES)
            self.dnfriders(strops.bibser2bibstr(bib, series), u'dns')

    def tod_context_dnf_activate_cb(self, menuitem, data=None):
        """Register rider as non-finisher."""
        sel = self.view.get_selection().get_selected()
        if sel is not None:
            i = sel[1]  # grab off row iter
            bib = self.riders.get_value(i, COL_BIB)
            series = self.riders.get_value(i, COL_SERIES)
            self.dnfriders(strops.bibser2bibstr(bib, series), u'dnf')

    def tod_context_dsq_activate_cb(self, menuitem, data=None):
        """Disqualify rider."""
        sel = self.view.get_selection().get_selected()
        if sel is not None:
            i = sel[1]  # grab off row iter
            bib = self.riders.get_value(i, COL_BIB)
            series = self.riders.get_value(i, COL_SERIES)
            self.dnfriders(strops.bibser2bibstr(bib, series), u'dsq')

    def tod_context_rel_activate_cb(self, menuitem, data=None):
        """Relegate rider."""
        LOG.info(u'Relegate not implemented for time trial.')
        pass

    def tod_context_ntr_activate_cb(self, menuitem, data=None):
        """Register no time recorded for rider and place last."""
        ## TODO
        LOG.info(u'NTR not implemented for time trial.')
        pass

    def tod_context_clear_activate_cb(self, menuitem, data=None):
        """Clear times for selected rider."""
        sel = self.view.get_selection().get_selected()
        if sel is not None:
            self.riders.set_value(sel[1], COL_COMMENT, u'')
            self.riders.set_value(sel[1], COL_PASS, 0)
            self.settimes(sel[1])  # clear iter to empty vals
            self.log_clear(
                self.riders.get_value(sel[1], COL_BIB).decode('utf-8'),
                self.riders.get_value(sel[1], COL_SERIES).decode('utf-8'))

    def now_button_clicked_cb(self, button, entry=None):
        """Set specified entry to the current time."""
        if entry is not None:
            entry.set_text(tod.now().timestr())

    def tod_context_edit_activate_cb(self, menuitem, data=None):
        """Run edit time dialog."""
        sel = self.view.get_selection().get_selected()
        if sel is not None:
            i = sel[1]  # grab off row iter and read in cur times
            tst = self.riders.get_value(i, COL_TODSTART)
            tft = self.riders.get_value(i, COL_TODFINISH)
            tpt = self.riders.get_value(i, COL_TODPENALTY)

            # prepare text entry boxes
            st = ''
            if tst is not None:
                st = tst.timestr()
            ft = ''
            if tft is not None:
                ft = tft.timestr()
            bt = ''
            pt = '0'
            if tpt is not None:
                pt = tpt.timestr()

            # run the dialog
            (ret, st, ft, bt, pt) = uiutil.edit_times_dlg(self.meet.window,
                                                          st,
                                                          ft,
                                                          bt,
                                                          pt,
                                                          bonus=True,
                                                          penalty=True)
            if ret == 1:
                stod = tod.mktod(st)
                ftod = tod.mktod(ft)
                ptod = tod.mktod(pt)
                if ptod is None:
                    ptod = tod.ZERO
                bib = self.riders.get_value(i, COL_BIB)
                series = self.riders.get_value(i, COL_SERIES)
                self.settimes(i, tst=stod, tft=ftod, pt=ptod)  # update model
                LOG.info('Race times manually adjusted for rider ' +
                         strops.bibser2bibstr(bib, series))
            else:
                LOG.info('Edit race times cancelled.')

    def tod_context_del_activate_cb(self, menuitem, data=None):
        """Delete selected row from race model."""
        sel = self.view.get_selection().get_selected()
        if sel is not None:
            i = sel[1]  # grab off row iter
            self.settimes(i)  # clear times
            if self.riders.remove(i):
                pass  # re-select?

    def log_clear(self, bib, series):
        """Print clear time log."""
        LOG.info('Time cleared for rider ' + strops.bibser2bibstr(bib, series))

    def title_close_clicked_cb(self, button, entry=None):
        """Close and save the race."""
        self.meet.close_event()

    def set_titlestr(self, titlestr=None):
        """Update the title string label."""
        if titlestr is None or titlestr == '':
            titlestr = 'Individual Road Time Trial'
        self.title_namestr.set_text(titlestr)

    def destroy(self):
        """Signal race shutdown."""
        if self.context_menu is not None:
            self.context_menu.destroy()
        self.frame.destroy()

    def show(self):
        """Show race window."""
        self.frame.show()

    def hide(self):
        """Hide race window."""
        self.frame.hide()

    def ridercat(self, cat):
        """Return a category from the result for the riders cat."""
        ret = u''  # default is the 'None' category - uncategorised
        checka = cat.upper()
        if checka in self.results:
            ret = checka
        #LOG.debug('ridercat read ' + repr(cat) + '/' + repr(checka)
        #+ '  Returned: ' + repr(ret))
        return ret

    def get_catlist(self):
        """Return the ordered list of categories."""
        rvec = []
        for cat in self.cats:
            if cat != '':
                rvec.append(cat)
        return rvec

    def __init__(self, meet, event, ui=True):
        """Constructor."""
        self.meet = meet
        self.event = event
        self.evno = event[u'evid']
        # series is specified per-rider
        self.configfile = meet.event_configfile(self.evno)
        self.readonly = not ui
        rstr = u''
        if self.readonly:
            rstr = u'readonly '
        LOG.debug(u'Init %r event %r', rstr, self.evno)

        self.recalclock = threading.Lock()
        self._dorecalc = False

        # properties
        self.sloppystart = False
        self.autoexport = False
        self.finishloop = None
        self.startloop = None
        self.starttrig = None
        self.precision = 2
        self.finishpass = None

        # race run time attributes
        self.onestart = False
        self.winopen = True
        self.timerstat = u'idle'
        self.racestat = u'prerace'
        self.start = None
        self.lstart = None
        self.start_unload = None
        self.startgap = None
        self.startdelay = tod.ZERO
        self.cats = []  # the ordered list of cats for results
        self.autocats = False
        self.results = {u'': tod.todlist(u'UNCAT')}
        self.inters = {}
        self.ischem = {}
        self.showinter = None
        for im in [COL_INTERA, COL_INTERB, COL_INTERC, COL_INTERD, COL_INTERE]:
            self.inters[im] = {u'': tod.todlist(u'UNCAT')}
            self.ischem[im] = None
        self.interloops = {}  # map of loop ids to inter splits
        self.curfintod = None
        self.doannounce = False
        self.onestartlist = False
        self.curcat = u''
        self.catlaps = {}
        self.comment = []
        self.places = u''

        self.bonuses = {}
        self.points = {}
        self.pointscb = {}

        ## these have to go!
        self.intermeds = []  # sorted list of intermediate keys
        self.intermap = {}  # map of intermediate keys to results
        self.contests = []  # sorted list of contests
        self.contestmap = {}  # map of contest keys
        self.tallys = []  # sorted list of points tallys
        self.tallymap = {}  # map of tally keys

        self.riders = gtk.ListStore(
            gobject.TYPE_STRING,  # 0 bib
            gobject.TYPE_STRING,  # 1 series
            gobject.TYPE_STRING,  # 2 namestr
            gobject.TYPE_STRING,  # 3 cat
            gobject.TYPE_STRING,  # 4 comment
            gobject.TYPE_PYOBJECT,  # 5 wstart
            gobject.TYPE_PYOBJECT,  # 6 tstart
            gobject.TYPE_PYOBJECT,  # 7 finish
            gobject.TYPE_PYOBJECT,  # 8 penalty
            gobject.TYPE_STRING,  # 9 place
            gobject.TYPE_STRING,  # 10 shortname
            gobject.TYPE_PYOBJECT,  # 11 intermediate
            gobject.TYPE_PYOBJECT,  # 12 intermediate
            gobject.TYPE_PYOBJECT,  # 13 intermediate
            gobject.TYPE_PYOBJECT,  # 14 intermediate
            gobject.TYPE_PYOBJECT,  # 15 intermediate
            gobject.TYPE_PYOBJECT,  # 16 last seen
            gobject.TYPE_PYOBJECT,  # 17 eta
            gobject.TYPE_INT)  # 18 pass count

        uifile = os.path.join(metarace.UI_PATH, u'irtt.ui')
        LOG.debug(u'Building event interface from %r', uifile)
        b = gtk.Builder()
        b.add_from_file(uifile)

        self.frame = b.get_object(u'race_vbox')
        self.frame.connect(u'destroy', self.shutdown)

        # meta info pane
        self.title_namestr = b.get_object(u'title_namestr')
        self.set_titlestr()

        # Timer Panes
        mf = b.get_object(u'race_timer_pane')
        self.sl = timerpane.timerpane(u'Start Line', doser=True)
        self.sl.disable()
        self.sl.bibent.connect(u'activate', self.bibent_cb, self.sl)
        self.sl.serent.connect(u'activate', self.bibent_cb, self.sl)
        self.fl = timerpane.timerpane(u'Finish Line', doser=True)
        self.fl.disable()
        self.fl.bibent.connect(u'activate', self.bibent_cb, self.fl)
        self.fl.serent.connect(u'activate', self.bibent_cb, self.fl)
        self.fl.tment.connect(u'activate', self.tment_cb, self.fl)
        mf.pack_start(self.sl.frame)
        mf.pack_start(self.fl.frame)
        mf.set_focus_chain([self.sl.frame, self.fl.frame, self.sl.frame])

        # Result Pane
        t = gtk.TreeView(self.riders)
        self.view = t
        t.set_reorderable(True)
        t.set_rules_hint(True)
        self.context_menu = None

        # show window
        if ui:
            t.connect(u'button_press_event', self.treeview_button_press)
            # TODO: show team name & club but pop up for rider list
            uiutil.mkviewcolbibser(t)
            uiutil.mkviewcoltxt(t, u'Rider', COL_NAMESTR, expand=True)
            uiutil.mkviewcoltxt(t, u'Cat', COL_CAT, self.editcol_cb)
            uiutil.mkviewcoltxt(t, u'Passes', COL_PASS, self.editcol_cb)
            # -> Add in start time field with edit!
            uiutil.mkviewcoltod(t, u'Start', cb=self.wallstartstr)
            uiutil.mkviewcoltod(t, u'Time', cb=self.elapstr)
            uiutil.mkviewcoltxt(t, u'Rank', COL_PLACE, halign=0.5, calign=0.5)
            t.show()
            b.get_object(u'race_result_win').add(t)
            b.connect_signals(self)

            b = gtk.Builder()
            b.add_from_file(os.path.join(metarace.UI_PATH, u'tod_context.ui'))
            self.context_menu = b.get_object(u'tod_context')
            b.connect_signals(self)

            # reconfigure the chronometer
            self.meet.alttimer.armlock()  # lock the arm to capture all hits
            self.meet.alttimer.arm(0)  # start line
            self.meet.alttimer.arm(1)  # finish line (primary)
            self.meet.alttimer.arm(2)  # use for backup trigger a
            self.meet.alttimer.arm(3)  # use for backup trigger b
            self.meet.alttimer.delaytime(u'0.01')

            # connect timer callback functions
            self.meet.timercb = self.timertrig  # transponders
            self.meet.alttimercb = self.alttimertrig  # chronometer
