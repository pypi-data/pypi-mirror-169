import functools
import logging
import re
import io
import serial
import string
import time
import asyncio
import threading
import numpy as np
from functools import wraps
from typing import Callable, Coroutine
from threading import RLock

_LOGGER = logging.getLogger(__name__)
'''
#ZxxPWRppp,SRCs,GRPt,VOL-yy
'''
CONSR_PATTERN = re.compile('Z(?P<zone>\d{2})'
                     'PWR(?P<power>ON|OFF),'
                     'SRC(?P<source>\d),'
                     'GRP(?P<group>0|1),'
                     'VOL(?P<volume>-\d\d|-MT|-XM)')
'''
#ZxxORp,BASSyy,TREByy,GRPq,VRSTr
'''
ESSENTIA_D_SETSR_PATTERN = re.compile('Z(?P<zone>\d{2})'
                     'OR(?P<override>\d),'
                     'BASS(?P<bass>[+-]?\d{2}),'
                     'TREB(?P<treble>[+-]?\d{2}),'
                     'GRP(?P<group>0|1),'
                     'VRST(?P<volume_reset>1|0)')
'''
#Z0x,BASSyy,TREByy,GRPq
'''
SIMPLESE_SETSR_PATTERN = re.compile('Z(?P<zone>\d{2})'
                     '(?P<override>.)'
                     'BASS(?P<bass>[+-]?\d{2}),'
                     'TREB(?P<treble>[+-]?\d{2}),'
                     'GRP(?P<group>0|1)')
'''
#MPU_E6D_vx.yy
'''
ESSENTIA_D_VERSION = re.compile('MPU_E6D[A-Za-z\t .]+')
'''
#MPU_A4D_vx.yy
'''
SIMPLESE_VERSION = re.compile('MPU_A4D[A-Za-z\t .]+')

EOL = b'\r'
TIMEOUT_OP       = 0.2   # Number of seconds before serial operation timeout
TIMEOUT_RESPONSE = 1     # Number of seconds before command response timeout
zoneinit = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0])
zonesetinit = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0])
zonepwr = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0])
zonepwrsave = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0])
zonevol = np.array([0,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78])
zonevolsave = np.array([0,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78,-78])
zonesrc = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0])
zonesrcsave = np.array([0,1,1,1,1,1,1,1,1,1,1,1,1])
zonemute = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0])
zonemutesave = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0])
zonebass = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0])
zonetreble = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0])
zonegroup = np.array([0,1,1,1,1,1,1,1,1,1,1,1,1])
zoneoverride = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0])
zonevolreset = np.array([0,1,1,1,1,1,1,1,1,1,1,1,1])

class ZoneStatus(object):
    def __init__(self
                 ,zone: int
                 ,power: str
                 ,source: int
                 ,group: bool
                 ,volume: float  # -78 -> 0
                 ,from_port: bool
                 ):

        self.source = str(source)
        self.zone = abs(int(zone))
        if 'ON' in power:
           self.power = bool(1)
           """ Nuvo does not send update from other zones using source
               grouping.  See if is enabled and if so, update the other
               zones that are powered up. """
           if zonegroup[self.zone] == 0:
               for count in range(1,13):
                   if zonegroup[count] == 0 and zonepwr[count] == 1:
                       zonesrc[count] = self.source
                       if from_port:
                           try:
                               callbackobj = media_zonetable.index(count)
                               callbackint = int(callbackobj)
                               media_callback[callbackint]()
                           except:
                               callbackobj =  None

        else:
           self.power = bool(0)

        if 'MT' in volume:
           self.mute = bool(1)
           self.volume = zonevol[self.zone]
        else:
           self.mute = bool(0)
           self.volume = int(volume)

        zonepwr[self.zone] = self.power
        zonevol[self.zone] = self.volume
        zonesrc[self.zone] = self.source
        zonemute[self.zone] = self.mute

        if from_port:
            try:
               callbackobj = media_zonetable.index(self.zone)
               callbackint = int(callbackobj)
               media_callback[callbackint]()
            except:
               callbackobj =  None

        _LOGGER.debug('Zone: %s, Power: %s, Vol: %s, Mute: %s, Source: %s, Init: %s', \
           self.zone, self.power, self.volume, self.mute, self.source, \
           zoneinit[int(self.zone)])

    @classmethod
    def from_string(cls, match):
        ZoneStatus(*[str(m) for m in match.groups()], True)

class ZonesetStatus(object):
    def __init__(self
             ,zone: int
             ,ovride: str
             ,bass: float
             ,treble: float
             ,grp: int
             ,vrset: int
             ,from_port: bool
             ):

        self.zone = abs(int(zone))
        self.treble = treble
        self.bass = bass
        zonebass[self.zone] = self.bass
        zonetreble[self.zone] = self.treble
        if MODEL == 'ESSENTIA_D':
            zoneoverride[self.zone] = int(ovride)
        zonevolreset[self.zone] = vrset
        zonegroup[self.zone] = grp

        if zoneoverride[self.zone] == 1:
           self.override = bool(1)
        else:
           self.override = bool(0)
        if zonevolreset[self.zone] == 1:
           self.volume_reset = bool(0)
        else:
           self.volume_reset = bool(1)
        if zonegroup[self.zone] == 1:
           self.group = bool(0)
        else:
           self.group = bool(1)

        if from_port:
            try:
                callbackindex = [i for i, x in enumerate(settings_zonetable) if x == self.zone]
                for callbackzone in callbackindex:
                    settings_callback[callbackzone]()
            except:
               callbackobj =  None

        _LOGGER.debug('Zone: %s, Bass: %s, Treble: %s, Override: %s, VolReset: %s, Group: %s, Init: %s',\
            self.zone, self.bass, self.treble, self.override, \
            self.volume_reset, self.group, zonesetinit[int(self.zone)])

    @classmethod
    def from_string(cls, match):
        if MODEL == 'SIMPLESE':
            ZonesetStatus(*[str(m) for m in match.groups()], '1', True)
        else:
            ZonesetStatus(*[str(m) for m in match.groups()], True)

class Nuvo(object):
    """
    Nuvo amplifier interface
    """
    def add_callback(self, coro: Callable[..., Coroutine], zone) -> None:
        """
        Add entity subscription for updates
        """
        raise NotImplemented()

    def get_model(self):
        """
        Get the Nuvo model from version request
        """
        raise NotImplemented()

    def zone_status(self, zone: int):
        """
        Get the structure representing the status of the zone
        :param zone: zone 1.12
        :return: status of the zone or None
        """
        raise NotImplemented()

    def zoneset_status(self, zone: int):
        """
        Get the structure representing the status of the zone
        :param zone: zone 1.12
        :return: status of the zone or None
        """
        raise NotImplemented()

    def set_power(self, zone: int, power: bool):
        """
        Turn zone on or off
        :param zone: zone 1.12
        :param power: True to turn on, False to turn off
        """
        raise NotImplemented()

    def set_mute(self, zone: int, mute: bool):
        """
        Mute zone on or off
        :param zone: zone 1.12
        :param mute: True to mute, False to unmute
        """
        raise NotImplemented()

    def set_volume(self, zone: int, volume: float):
        """
        Set volume for zone
        :param zone: zone 1.12
        :param volume: float from -78 to 0 inclusive
        """
        raise NotImplemented()

    def set_treble(self, zone: int, treble: float):
        """
        Set treble for zone
        :param zone: zone 1.12
        :param treble: float from -12 to 12 inclusive
        """
        raise NotImplemented()

    def set_bass(self, zone: int, bass: float):
        """
        Set bass for zone
        :param zone: zone 1.12
        :param bass: float from -12 to 12 inclusive
        """
        raise NotImplemented()

    def set_source(self, zone: int, source: int):
        """
        Set source for zone
        :param zone: zone 1.12
        :param source: integer from 1 to 6 inclusive
        """
        raise NotImplemented()

    def page_off(self, page_source, page_zones):
        """
        Restores zone to it's previous state prior to page request
        """
        raise NotImplemented()

    def page_on(self, page_source, page_zones, page_volume):
        """
        Power on all zones, set to paging source and volume
        """
        raise NotImplemented()

    def mute_all(self):
        """
        Mutes all zones.
        """
        raise NotImplemented()

    def unmute_all(self):
        """
        Unmutes all zones.
        """
        raise NotImplemented()

    def all_off(self):
        """
        Turn off all zones.
        """
        raise NotImplemented()

# Helpers

def _is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def _parse_response(string: bytes):
   """
   :param request: request that is sent to the nuvo
   :return: regular expression return match(s)
   """
   match = re.search(ESSENTIA_D_SETSR_PATTERN, string)
   if match:
      _LOGGER.debug('Essentia D SETSR received')
      ZonesetStatus.from_string(match)

   if not match:
       match = re.search(CONSR_PATTERN, string)
       if match:
          _LOGGER.debug('CONSR received')
          ZoneStatus.from_string(match)

   if not match:
       match = re.search(SIMPLESE_SETSR_PATTERN, string)
       if match:
          _LOGGER.debug('Simplese SETSR received')
          ZonesetStatus.from_string(match)

   global MODEL

   if not match:
       match = re.search(ESSENTIA_D_VERSION, string)
       if match:
          _LOGGER.info('Nuvo returned model Essentia D')
          MODEL = 'ESSENTIA_D'

   if not match:
       match = re.search(SIMPLESE_VERSION, string)
       if match:
          _LOGGER.info('Nuvo returned model Simplese')
          MODEL = 'SIMPLESE'

   if (string == '#Busy'):
       _LOGGER.warn('BUSY RESPONSE - TRY AGAIN')
   return None

   if not match:
       _LOGGER.warn('NO MATCH - %s' , string)
   return None

def _format_version_request():
    return 'VER'.format()

def _format_zone_status_request(zone: int) -> str:
    return 'Z{:0=2}CONSR'.format(zone)

def _format_zoneset_status_request(zone: int) -> str:
    return 'Z{:0=2}SETSR'.format(zone)

def _format_set_power(zone: int, power: bool) -> str:
    zone = int(zone)
    if (power):
       zonepwr[int(zone)] = 1
       return 'Z{:0=2}ON'.format(zone)
    else:
       zonepwr[int(zone)] = 0
       return 'Z{:0=2}OFF'.format(zone)

def _format_set_mute(zone: int, mute: bool) -> str:
    if (mute):
       zonemute[int(zone)] = 1
       return 'Z{:0=2}MTON'.format(int(zone))
    else:
       zonemute[int(zone)] = 0
       return 'Z{:0=2}MTOFF'.format(int(zone))

def _format_set_group(zone: int, group: bool) -> str:
    if (group):
       return 'Z{:0=2}GRPON'.format(int(zone))
    else:
       return 'Z{:0=2}GRPOFF'.format(int(zone))

def _format_set_volume_reset(zone: int, volreset: bool) -> str:
    if (volreset):
       return 'Z{:0=2}VRSTON'.format(int(zone))
    else:
       return 'Z{:0=2}VRSTOFF'.format(int(zone))

def _format_set_volume(zone: int, volume: float) -> str:
    # If muted, status has no info on volume level
    if _is_int(volume):
       # Negative sign in volume parm produces erronous result
       zonevol[int(zone)] = int(volume)
       volume = abs(volume)
       volume = round(volume,0)
    return 'Z{:0=2}VOL{:0=2}'.format(int(zone), volume)

def _format_set_bass(zone: int, bass: float) -> bytes:
    zonebass[int(zone)] = bass
    if bass >= 0:
       return 'Z{:0=2}BASS+{:0=2}'.format(int(zone), int(bass))
    else:
       return 'Z{:0=2}BASS{:0=3}'.format(int(zone), int(bass))

def _format_set_treble(zone: int, treble: float) -> bytes:
    zonetreble[int(zone)] = treble
    if treble >= 0:
       return 'Z{:0=2}TREB+{:0=2}'.format(int(zone), int(treble))
    else:
       return 'Z{:0=2}TREB{:0=3}'.format(int(zone), int(treble))

def _format_set_source(zone: int, source: int) -> str:
    source = int(max(1, min(int(source), 6)))
    zonesrc[int(zone)] = source
    return 'Z{:0=2}SRC{}'.format(int(zone),source)

def _format_mute_all() -> str:
    return 'ALLMON'.format()

def _format_unmute_all() -> str:
    return 'ALLMOFF'.format()

def _format_all_off() -> str:
    return 'ALLOFF'.format()

def get_nuvo(port_url, baud):
    """
    Return synchronous version of Nuvo interface
    :param port_url: serial port, i.e. '/dev/ttyUSB0,/dev/ttyS0'
    :param baud: baud, i.e '9600'
    :return: synchronous implementation of Nuvo interface
    """

    lock = RLock()

    def synchronized(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with lock:
                return func(*args, **kwargs)
        return wrapper

    class NuvoSync(Nuvo):
        def __init__(self, port_url):
            self._port = serial.serial_for_url(port_url, do_not_open=True)
            self._port.baudrate = int(baud)
            self._port.stopbits = serial.STOPBITS_ONE
            self._port.bytesize = serial.EIGHTBITS
            self._port.parity = serial.PARITY_NONE
            self._port.timeout = TIMEOUT_OP
            self._port.write_timeout = TIMEOUT_OP
            self._port.open()

        def get_model(self):
            findmodelcount = 0
            global MODEL
            while findmodelcount < 10:
                self._process_request(_format_version_request())
                time.sleep(TIMEOUT_RESPONSE)
                if 'MODEL' in globals():
                    findmodelcount = 10
                else:
                    findmodelcount += 1
            if not 'MODEL' in globals():
                _LOGGER.error('This does not appear to be a supported Nuvo device.')
                MODEL = 'Unknown'
            return MODEL

        def _send_request(self, request):
            """
            :param request: request that is sent to the nuvo
            :return: bool if transmit success
            """
            #format and send output command
            lineout = "*" + request + "\r"
            _LOGGER.debug('Sending "%s"', request)
            self._port.write(lineout.encode())
            time.sleep(0.1) #Must wait in between commands for MPU to process
            return True

        def _process_request(self, request: str):
            """
            :param request: request that is sent to the nuvo
            """
            # Send command to device
            self._send_request(request)

        def _listen():
            no_data = False
            receive_buffer = b''
            message = b''
            start_time = time.time()
            timeout = TIMEOUT_RESPONSE
            _LOGGER.info('Attempting connection - "%s" at %s baud', port_url, baud)
            try:
                port = serial.serial_for_url(port_url, do_not_open=True)
                port.baudrate = int(baud)
                port.stopbits = serial.STOPBITS_ONE
                port.bytesize = serial.EIGHTBITS
                port.parity = serial.PARITY_NONE
                port.open()
            except:
                _LOGGER.error('Could not open serial port.')
            # listen for response
            while (no_data == False):
                   # fill buffer until we get term seperator
               data = port.read(1)

               if data:
                  receive_buffer += data
                  if EOL in receive_buffer:
                      message, sep, receive_buffer = receive_buffer.partition(EOL)
                      _LOGGER.debug('Received: %s', message)
                      _parse_response(str(message))

        SyncThread = threading.Thread(target=_listen, args=(), daemon=True)
        SyncThread.start()

        def add_callback(self, callback: Callable[..., Coroutine], zone, entity) -> None:
            global media_zonetable
            global media_callback
            global settings_zonetable
            global settings_callback
            try:
                media_zonetable
            except:
                media_zonetable = []
                media_callback = []
                settings_zonetable = []
                settings_callback = []
            if entity == 'media':
                zone = int(zone)
                media_zonetable.append(zone)
                media_callback.append(callback)
                _LOGGER.debug('Added %s callback: %s', entity, callback)
            if entity == 'settings':
                zone = int(zone)
                settings_zonetable.append(zone)
                settings_callback.append(callback)
                _LOGGER.debug('Added %s callback: %s', entity, callback)

        @synchronized
        def zone_status(self, zone: int):
            """
            Send status request multiple times on startup to insure we get
            a response
            """
            if zoneinit[int(zone)] == 0:
               try:
                  rtn = ZoneStatus.from_string(self._process_request(
                                    _format_zone_status_request(zone)))
               except:
                  rtn = None
               zoneinit[int(zone)] += 1
               return rtn
            else:
               if zonepwr[int(zone)] == 1:
                  zonestrpwr = 'ON'
               else:
                  zonestrpwr = 'OFF'
               if zonemute[int(zone)] == 1:
                  zonestrvol = 'MT'
               else:
                  zonestrvol = str(zonevol[int(zone)])

               return ZoneStatus(int(zone), zonestrpwr,
                                    zonesrc[int(zone)], 0, zonestrvol, False)

        @synchronized
        def zoneset_status(self, zone: int):
            """
            Send status request multiple times on startup to insure we get
            a response
            """
            if zonesetinit[int(zone)] == 0:
               try:
                  rtn = ZonesetStatus.from_string(
                                    self._process_request(
                                    _format_zoneset_status_request(zone)))
               except:
                  rtn = None
               zonesetinit[int(zone)] += 1
               return rtn
            else:
               return ZonesetStatus(int(zone), zoneoverride[int(zone)],
                                    zonebass[int(zone)],
                                    zonetreble[int(zone)],
                                    zonegroup[int(zone)],
                                    zonevolreset[int(zone)], False)

        @synchronized
        def set_power(self, zone: int, power: bool):
            self._process_request(_format_set_power(zone, power))

        @synchronized
        def set_mute(self, zone: int, mute: bool):
            self._process_request(_format_set_mute(zone, mute))

        @synchronized
        def set_volume(self, zone: int, volume: float):
            self._process_request(_format_set_volume(zone, volume))

        @synchronized
        def set_group(self, zone: int, group: bool):
            self._process_request(_format_set_group(zone, group))

        @synchronized
        def set_volume_reset(self, zone: int, volreset: bool):
            self._process_request(_format_set_volume_reset(zone, volreset))

        @synchronized
        def set_treble(self, zone: int, treble: float):
            self._process_request(_format_set_treble(zone, treble))

        @synchronized
        def set_bass(self, zone: int, bass: float):
            self._process_request(_format_set_bass(zone, bass))

        @synchronized
        def set_source(self, zone: int, source: int):
            self._process_request(_format_set_source(zone, source))

        @synchronized
        def page_off(self, page_source, page_zones):
            zonecnt = 0
            while zonecnt < len(page_zones):
               self.set_volume(int(page_zones[zonecnt]),
                               zonevolsave[int(page_zones[zonecnt])])
               if zonemutesave[int(page_zones[zonecnt])] == 1:
                   self.set_mute(int(page_zones[zonecnt]), True)
               if zonepwrsave[int(page_zones[zonecnt])] == 0:
                   self.set_power(int(page_zones[zonecnt]), False)
               else:
                   if zonesrcsave[int(page_zones[zonecnt])] != page_source:
                       self.set_source(int(page_zones[zonecnt]),
                                       zonesrcsave[int(page_zones[zonecnt])])
               zonecnt += 1

        @synchronized
        def page_on(self, page_source, page_zones, page_volume):
            zonecnt = 0
            while zonecnt < len(page_zones):
               _LOGGER.debug('Page Zone: %s, Vol: %s, Src: %s', page_zones[zonecnt],\
                   page_volume[zonecnt], page_source)
               zonepwrsave[int(page_zones[zonecnt])] = zonepwr[int(page_zones[zonecnt])]
               zonesrcsave[int(page_zones[zonecnt])] = zonesrc[int(page_zones[zonecnt])]
               zonevolsave[int(page_zones[zonecnt])] = zonevol[int(page_zones[zonecnt])]
               zonemutesave[int(page_zones[zonecnt])] = zonemute[int(page_zones[zonecnt])]
               if zonepwr[int(page_zones[zonecnt])] == 0:
                   self.set_power(int(page_zones[zonecnt]), True)
                   time.sleep(0.05)
               if zonesrc[int(page_zones[zonecnt])] != page_source:
                   self.set_source(int(page_zones[zonecnt]), page_source)
               self.set_volume(int(page_zones[zonecnt]), int(page_volume[zonecnt]))
               zonecnt += 1

        @synchronized
        def mute_all(self):
            self._process_request(_format_mute_all())
            for count in range(1,13):
                zonemute[int(count)] = 1
                try:
                    callbackobj = media_zonetable.index(count)
                    callbackint = int(callbackobj)
                    media_callback[callbackint]()
                except:
                    callbackobj =  None

        @synchronized
        def unmute_all(self):
            self._process_request(_format_unmute_all())
            for count in range(1,13):
                zonemute[int(count)] = 0
                try:
                    callbackobj = media_zonetable.index(count)
                    callbackint = int(callbackobj)
                    media_callback[callbackint]()
                except:
                    callbackobj =  None

        @synchronized
        def all_off(self):
            self._process_request(_format_all_off())
            for count in range(1,13):
                zonepwr[int(count)] = 0
                try:
                    callbackobj = media_zonetable.index(count)
                    callbackint = int(callbackobj)
                    media_callback[callbackint]()
                except:
                    callbackobj =  None

    return NuvoSync(port_url)
