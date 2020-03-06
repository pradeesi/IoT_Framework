import platform, os, time
from subprocess import PIPE, Popen


#====================================================================================
def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]
#====================================================================================


#====================================================================================
def check_PIGPIO_Service_Status(service_Name='pigpiod'):

	if platform.system() == 'Linux':
		Command = r"sudo ps -A | grep "
		Command = Command + service_Name

		output = cmdline(Command)
		
		if (service_Name in output):
			# Service is Running
			return 1
		else:
			# Service is not Running
			return 0
	else:
		# Invalid Plaform
		return 0
#====================================================================================


#====================================================================================
def start_PIGPIO_Service(service_Name='pigpiod'):
		
	if platform.system() == 'Linux':
		if check_PIGPIO_Service_Status() != 1:
			Command = r"sudo "
			Command = Command + service_Name
			
			output = cmdline(Command)
			
			time.sleep(5)
			
			status = check_PIGPIO_Service_Status(service_Name)
			
			if (status == 1):
				# Service is Running
				return 1
			else:
				# Service is not Running
				return 0
		else:
			return 1
	else:
		# Invalid Plaform
		return 0
#====================================================================================


#====================================================================================
def stop_PIGPIO_Service(service_Name='pigpiod'):
		
	if platform.system() == 'Linux':
		Command = r"pidof "
		Command = Command + service_Name
		
		PID = cmdline(Command)
		
		if (PID != None):
			Command = r'sudo kill ' + str(PID)
			output = cmdline(Command)
			return 1
		else:
			# Service is not Running
			return 0
	else:
		# Invalid Plaform
		return 0		
#====================================================================================
	
	