import RPi.GPIO as GPIO, time, os, json  
from datentime.datentime import dt   
 
from settings.parseSettings import get_Settings
Light_Sensor_Settings = get_Settings('PHOTOCELL')

DEBUG = 1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set GPIO Pin to Output Pun as we need to use it as 3V Power supply for Circuit
GPIO.setup(int(Light_Sensor_Settings['POWER']), GPIO.OUT)

def read_LIGHT():
		# Set GPIO High to supply 3V Power to Circuit
		GPIO.output(int(Light_Sensor_Settings['POWER']), GPIO.HIGH)
		
		RCpin = int(Light_Sensor_Settings['DATA'])
		reading = 0
		GPIO.setup(RCpin, GPIO.OUT)
		GPIO.output(RCpin, GPIO.LOW)
		time.sleep(0.1)
		GPIO.setup(RCpin, GPIO.IN)
		# This takes about 1 millisecond per loop cycle
		while (GPIO.input(RCpin) == GPIO.LOW):
			reading += 1
		
		GPIO.output(int(Light_Sensor_Settings['POWER']), GPIO.LOW)
		
		dt_Obj = dt()	
		data = {}
		
		data['sid'] = Light_Sensor_Settings['SENSOR_ID']
		data['dt'] = str(dt_Obj.get_DB_datetime_str())
		data['light'] = reading
		
		del dt_Obj
		#Return light reading
		json_data = json.dumps(data)
		return json_data