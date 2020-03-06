import json, platform, time 
import pigpio
from settings.parseSettings import get_Settings
from pigpiod_service_manager import start_PIGPIO_Service
from datentime.datentime import dt


DHT22_Settings = get_Settings('DHT22')

#For DHT Library
import DHT22_Library
#For Adafruit Library
import Adafruit_DHT as dht

Adafruit_Lib = True

def read_DHT22():
	dt_Obj = dt()	
	data = {}
	
	if Adafruit_Lib == True:
		Humidity, Temperature = dht.read_retry(dht.DHT22, int(DHT22_Settings['DATA']))
		
		data['sid'] = DHT22_Settings['SENSOR_ID']
		data['dt'] = str(dt_Obj.get_DB_datetime_str())
		data['temp'] = '{0:0.2f}'.format(Temperature)
		data['humi'] = '{0:0.2f}'.format(Humidity)
		
	else:
		dht22_Obj = DHT22_Sensor()
		dht22_Obj.read_Data()
		
		data['sid'] = DHT22_Settings['SENSOR_ID']
		data['dt'] = str(dt_Obj.get_DB_datetime_str())
		data['temp'] = dht22_Obj.Temperature
		data['humi'] = dht22_Obj.Humidity
		
		del dht22_Obj
	json_data = json.dumps(data)
	
	del dt_Obj

	
	return json_data
	

class DHT22_Sensor:
	
	def __init__(self):
		# Start PIGPIO Service, if it's not Running
		start_PIGPIO_Service()
		
	def read_Data(self):
		Data_Pin = int(DHT22_Settings['DATA'])
		LED_Pin = int(DHT22_Settings['LED'])
		Power_Pin = int(DHT22_Settings['POWER'])
		Sleep_Interval = int(DHT22_Settings['SLEEP_INTERVAL'])
		
		pi = pigpio.pi()
		s = DHT22_Library.sensor(pi, Data_Pin)
		s.trigger()
		
		#Sleep to read the data
		time.sleep(Sleep_Interval)
		
		self.Temperature = '{:3.2f}'.format(s.temperature() / 1.)
		self.Humidity = '{:3.2f}'.format(s.humidity() / 1.) 
		
		s.cancel()
		del s
		return 
		

		
		
		

