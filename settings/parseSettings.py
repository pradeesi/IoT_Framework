import ConfigParser
import inspect, os
import platform
import socket


settings_Dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
settings_File_Path =  os.path.join(settings_Dir, 'settings.ini')

#================= GET SETTINGS FROM A SECTION AND RETURN SETTINGS DICT ==============
def get_Settings(Section_Name):
	try:
		config = ConfigParser.ConfigParser()
		config.optionxform=str   #By default config returns keys from Settings file in lower case. This line preserves the case for keys
		config.read(settings_File_Path)
		
		return dict(config.items(Section_Name))	
	except Exception as error_msg:
		return {"Error" : str(error_msg)}
#=====================================================================================


#======================================================
# Function to convert String Flags to Boolean
#======================================================
def Str_To_Boolean(boolean_Str = 'False'):
	return True if boolean_Str.title() == 'True' else False
#======================================================



#================= GET IP ADDRESS OF LOCAL SYSTEM (Used Internally by 'get_System_Details') ==============
if os.name != "nt":
    import fcntl
    import struct

def get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                ifname[:15]))[20:24])

def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi0",
            "ath0",
            "ath1",
            "ppp0",
            ]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
                pass
    return ip
#=====================================================================================



#================= GET SYSTEM DETAILS AND RETURN DICT ================================
def get_System_Details():
	OS_Details = {}
	OS_Details['OS_CLASS'] = platform.system()
	OS_Details['OS'] = os.name
	OS_Details['REL'] = platform.release()
	OS_Details['VER'] = platform.version()
	OS_Details['DIST'] = platform.dist()
	OS_Details['MACHINE'] = platform.machine()
	OS_Details['PROCESSOR'] = platform.processor()
	OS_Details['PLATFORM'] = platform.platform()
	OS_Details['PYTHON_VER'] = platform.python_version()
	OS_Details['HOST_NAME'] = socket.gethostname()
	OS_Details['IP_ADD'] = get_lan_ip()
	
	return OS_Details
#=====================================================================================	


	