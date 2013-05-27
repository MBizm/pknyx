# -*- coding: utf-8 -*-

""" Python KNX framework

License
=======

 - B{pKNyX} (U{http://www.pknyx.org}) is Copyright:
  - (C) 2013 Frédéric Mantegazza

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
or see:

 - U{http://www.gnu.org/licenses/gpl.html}

Module purpose
==============

Datapoint management

Implements
==========

 - B{Datapoint}

Documentation
=============

Datapoint (DP) store knowledge about a datapoint in the KNX network, used for communication within the
pKNyX framework, to the KNX network, and with the user.
Datapoint is identified through a  L{GroupAddress}. A name is supplied to allow a
more friendly interaction with the user, the selected name does not have to be unique. <<<<<<<< ????
Information exchanged between datapoints consists of a certain encoding, defined by a
L{DPT}. This information exchange is done through messages, which are
sent with a L{Priority} associated with the respective datapoint. Every datapoint
object has its own DPT and priority.

The "flags" parameter is similar to the ETS flags. The value of each flag is represented by a letter:
 - c: Communication (allow the object to interact with the KNX bus)
 - r: Read (allow the object to answer to a read request from another participant)
 - w: Write (update the object's internal value with the one received in write telegram if they are different)
 - t : Transmit (allow the object to transmit it's value on the bus if it's modified internally by a rule or via XML protocol)
 - u : Update (update the object's internal value with the one received in "read response" telegram if they are different)
 - f : Force (force the object value to be transmitted on the bus, even if it didn't change).
       In the recent versions you can use s : Stateless flag alternatively which means exactly the same
       (object does not update it's state so linknx should always send it's value to the bus
 - i : Init (useless for the moment. Will perhaps replace the parameter init="request" in the future)

Each letter appearing inside the value of this parameter means the corresponding flag is set.
If "flags" is not specified, the default value is "cwtu" (Communication, Write, Transmit and Update).

The default set of flags is good for most normal objects like switches where the value kept internally by linknx is
corresponding to real object state. Another set of flags can be for example "crwtf" (or "crwts") for objects that
should send it's value to the KNX bus even if linknx maintains the same value. This is usefull for scenes.
Setting scene value to 'on' should send this value to KNX every time action is triggered to make the scene happen.

Usage
=====

>>> from dp import Datapoint as DP
>>> dp = DP("test")
>>> dp
<Datapoint("test", <DPTID("1.xxx")>, flags="cwtu", Priority(low)>)>
>>> dp.main
'test'
>>> dp.dptId
<DPTID("1.xxx")>
>>> dp.flags
'cwtu'
>>> dp.priority
<Priority(low)>

@author: Frédéric Mantegazza
@copyright: (C) 2013 Frédéric Mantegazza
@license: GPL
"""

__revision__ = "$Id$"

from pknyx.common.exception import PKNyXValueError
from pknyx.common.loggingServices import Logger
from pknyx.core.dpt.dptConverterFactory import DPTConverterFactory
from pknyx.core.dpt.dpt import DPTID
#from pknyx.core.knxFlags import KnxFlags
from pknyx.core.priority import Priority


class DPValueError(PKNyXValueError):
    """
    """


class Datapoint(object):
    """ Datapoint handling class

    @ivar _name: name of the Datapoint
    @type _name: str

    @ivar _flags: bus message flags
    @type _flags: str (or KnxFlags?)

    @ivar _priority: bus message priority
    @type _priority: L{Priority}

    @ivar _dptHandler: DPT handler associated with this Datapoint
    @param _dptHandler: L{DPTHandlerBase}
    """
    def __init__(self, name, dptId=DPTID(), flags="cwtu", priority=Priority()):
        """

        @param name: name of the Datapoint
        @type name: str

        @param dptId: Datapoint Type ID
        @type dptId: str L{DPTID}

        @param flags: bus message flags
        @type flags: str (or KnxFlags?)

        @param priority: bus message priority
        @type priority: str or L{Priority}
        """
        super(Datapoint, self).__init__()

        #Logger().debug("Datapoint.__init__(): name=%s, dptId=%r, flags=%r, priority=%s" % \
                       #(name, dptId, flags, priority, stateBased))

        self._name = name
        self._mainGroupAddress = mainGroupAddress
        if not isinstance(dptId, DPTID):
            dptId = DPTID(dptId)
        self._dptId = dptId
        #if not isinstance(flags, KnxFlags):
            #flags = KnxFlags(dptId)
        self._flags = flags
        if not isinstance(priority, Priority):
            priority = Priority(priority)
        self._priority = priority

        self._dptHandler = DPTConverterFactory.create(dptId)

    def __repr__(self):
        s = "<Datapoint(\"%s\", %s, flags=\"%s\", %s)>" % \
             (self._name, repr(self._dptId), self._flags, repr(self._priority))
        return s

    @property
    def name(self):
        """ return the Datapoint name
        """
        return self._name

    @property
    def dptId(self):
        """ return the DPT ID
        """
        return self._dptId

    #@dptId.setter
    #def dptId(self, dptId):
        #""" Change the Datapoint DPT ID
        #"""
        #if not isinstance(dptId, DPTID):
            #dptId = DPTID(dptId)
        #self._dptId = dptId
        self._dpt.

    @property
    def flags(self):
        """ return the Datapoint flags
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """ set the Datapoint flags
        """
        self._flags = flags

    @property
    def priority(self):
        """ return the Datapoint priority
        """
        return self._priority

    #@priority.setter
    #def priority(str, level):
        #""" Change the Datapoint priority
        #"""
        #if not isinstance(priority, Priority):
            #priority = Priority(priority)
        #self._priority = priority

    @property
    def value(self):
        return self._dpt.value

    @value.setter
    def value(self, value):
        self.dpt.value = value


if __name__ == '__main__':
    import unittest


    class DPTestCase(unittest.TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass