import ntplib

from time import ctime
import sys

print sys.platform


#europe.pool.ntp.org
#time-c.nist.gov

c = ntplib.NTPClient()
response = c.request('time-c.nist.gov', version=3)
print response.offset
print response.version

print ctime(response.tx_time)

print ntplib.leap_to_text(response.leap)

print response.root_delay

print ntplib.ref_id_to_text(response.ref_id)





import sys
import datetime

time_tuple = ( 2012, # Year
                  9, # Month
                  6, # Day
                  0, # Hour
                 38, # Minute
                  0, # Second
                  0, # Millisecond
              )

def _win_set_time(time_tuple):
    import pywin32
    # http://timgolden.me.uk/pywin32-docs/win32api__SetSystemTime_meth.html
    # pywin32.SetSystemTime(year, month , dayOfWeek , day , hour , minute , second , millseconds )
    dayOfWeek = datetime.datetime(time_tuple).isocalendar()[2]
    pywin32.SetSystemTime( time_tuple[:2] + (dayOfWeek,) + time_tuple[2:])


def _linux_set_time(time_tuple):
    import ctypes
    import ctypes.util
    import time

	
    CLOCK_REALTIME = 0

    class timespec(ctypes.Structure):
        _fields_ = [("tv_sec", ctypes.c_long),
                    ("tv_nsec", ctypes.c_long)]

    librt = ctypes.CDLL(ctypes.util.find_library("rt"))

    ts = timespec()
    ts.tv_sec = int( time.mktime( datetime.datetime( *time_tuple[:6]).timetuple() ) )
    ts.tv_nsec = time_tuple[6] * 1000000 # Millisecond to nanosecond

    # http://linux.die.net/man/3/clock_settime
    librt.clock_settime(CLOCK_REALTIME, ctypes.byref(ts))


if sys.platform=='linux2':
    _linux_set_time(time_tuple)

elif  sys.platform=='win32':
    _win_set_time(time_tuple)