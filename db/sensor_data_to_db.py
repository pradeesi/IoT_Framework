import json

from db.db_operations import DatabaseManager
from settings.parseSettings import get_Settings

DB_Settings = get_Settings('SQLIGHT')
MQTT_Settings = get_Settings('MQTT')

def bmp180_Data(jsonData):
	print "BMP 180 Data"
	print jsonData
	#Parse Data
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['sid']
	DatenTime = json_Dict['dt']
	Pressure = json_Dict['pres']
	Pressure_At_Sea_Level = json_Dict['pres_at_sea_level']
	Altitude = json_Dict['alti']
	Temperature = json_Dict['temp']
	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into BMP180_Data (SensorID, Date_n_Time, Pressure, Pressure_At_Sea_Level, Altitude, Temperature) values (?,?,?,?,?,?)",[SensorID, DatenTime, Pressure, Pressure_At_Sea_Level, Altitude, Temperature])
	del dbObj


def dht22_Data(jsonData):
	print "DHT 22 Data"
	print jsonData
	#Parse Data 
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['sid']
	DatenTime = json_Dict['dt']	
	Temperature = json_Dict['temp']
	Humidity = json_Dict['humi']
	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into DHT22_Data (SensorID, Date_n_Time, Temperature, Humidity) values (?,?,?,?)",[SensorID, DatenTime, Temperature, Humidity])
	del dbObj
	
	
def light_Data(jsonData):
	print "LIGHT Data"
	print jsonData
	#Parse Data 
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['sid']
	DatenTime = json_Dict['dt']	
	Light = json_Dict['light']
	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("insert into LIGHT_Data (SensorID, Date_n_Time, Light) values (?,?,?)",[SensorID, DatenTime, Light])
	del dbObj

	
# Master Function	
def sensor_Data_Handler(Topic, jsonData):
	print Topic
	if Topic == MQTT_Settings['BMP180_TPC']:
		bmp180_Data(jsonData)
	elif Topic == MQTT_Settings['DHT22_TPC']:
		dht22_Data(jsonData)
	elif Topic == MQTT_Settings['LIGHT_TPC']:
		light_Data(jsonData)	
	