from decimal import Decimal
import threading, time, json
import RPi.GPIO as GPIO
from datentime.datentime import dt


#Read Settings
from settings.parseSettings import get_Settings
Motion_Sensor_Settings = get_Settings('PIR')
Data_Pin = int(Motion_Sensor_Settings['DATA'])

#Set GPIO Mode and Pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(Data_Pin, GPIO.IN, GPIO.PUD_DOWN)

class PIR_Sensor():
	
	def __init__(self):
		pass
	
	#=============================================================================
	def read_PIR_Motion_Sensor(self, event_Listener_Function):
		#Initialize Variables
		Previous_Motion_State=0
		Current_Motion_State=0
		Motion_Start_Time = None
		dt_Obj = dt()
		
		#Keep Reading Sensor
		while True:
			Previous_Motion_State = Current_Motion_State
			#Read Motion Sensor
			Current_Motion_State = GPIO.input(Data_Pin)
			
			if Current_Motion_State != Previous_Motion_State:
				#Prepare json data				
				data = {}
				data['sid'] = str(Motion_Sensor_Settings['SENSOR_ID'])
				data['dt'] = dt_Obj.get_DB_datetime_str()					
				if Current_Motion_State == 1:
					data['Motion_Detected'] = True
					Motion_Start_Time = data['dt']
				else:
					data['Motion_Detected'] = False
					data['Motion_Start_Time'] = Motion_Start_Time				
				json_data = json.dumps(data)
			
				#Invoke Event Listener Function in new Thread 
				event_thread = threading.Thread(target=event_Listener_Function, args=[json_data, data['Motion_Detected']])
				self.event_Thread_ID = event_thread.start()
				
				# In case of Motion, Hold the state for some time.
				if data['Motion_Detected'] == True:
					time.sleep(Decimal(Motion_Sensor_Settings['MOTION_STATUS_HOLD_TIME']))		
		
			#Hold for Polling Interval
			time.sleep(Decimal(Motion_Sensor_Settings['POLLING_INTERVAL']))
					
		del dt_Obj
		return
	#=============================================================================


	#=============================================================================
	# Asynchronous Motion Sensor Monitor (MASTER)
	#=============================================================================
	def monitor_PIR_Motion_Sensor(self, event_Listener_Function):
		monitor_Sensor_Thread = threading.Thread(target=self.read_PIR_Motion_Sensor, args=[event_Listener_Function])
		self.monitor_Thread_ID = monitor_Sensor_Thread.start()
		return
	#=============================================================================

	def __del__(self):
		self.monitor_Thread_ID.stop()
		self.event_Thread_ID.stop()
		