import json
from mqtt.mqtt_publish import MQTT_Publish
from bmp180.bmp180 import read_BMP180
from dht22.dht22 import read_DHT22
from led.status_led import status_LED_ON, status_LED_OFF
from photocell_light.photocell_light_sensor import read_LIGHT
from settings.parseSettings import get_Settings, Str_To_Boolean
from multi_threading.multi_threading import RepeatedTimer
from pir.pir_motion_sensor import PIR_Sensor
from camera.capture_time_lapse_photo import start_Time_Lapse_Photo_Capture
from camera.camera_file_gdrive_youtube_upload import PiCam_GDrive_YouTube_Upload_Service, get_GDrive_PiCam_Data_Path
from camera.capture_mp4_video import start_Video_Capture
from twitter_post.twitter_post import publish_Status_On_Twitter
from facebook_post.facebook_post import post_on_Facebook
from sms.ways2sms import send_SMS



#======================================================
#Fetch Settings
#======================================================
MQTT_Settings = get_Settings('MQTT')
DHT22_Settings = get_Settings('DHT22')
BMP180_Settings = get_Settings('BMP180')
LIGHT_Settings = get_Settings('PHOTOCELL')
STATUS_LED_Settings = get_Settings('STATUS_LED')
SYSTEM_Settings = get_Settings('SYSTEM')
Motion_Sensor_Settings = get_Settings('PIR')
Camera_Settings = get_Settings('CAMERA')
GOOGLE_DRIVE_Settings = get_Settings('GOOGLE_DRIVE')
FACEBOOK_Settings = get_Settings('FACEBOOK')
TWITTER_Settings = get_Settings('TWITTER')
WAYS2SMS_Settings = get_Settings('WAYS2SMS')
#======================================================


#======================================================
# Publish Data to MQTT Broker
#======================================================
def MQTT_Publish_Master(mqtt_Topic, json_Data):
	mqtt_Obj = MQTT_Publish()
	mqtt_Obj.publish_To_Topic(mqtt_Topic,json_Data)
	del mqtt_Obj
#======================================================


###########################################################
###########################################################
# SENSOR POLLING BLOCK (START)
###########################################################
###########################################################	
	
#======================================================
# DHT22 Sensor
#======================================================
def DHT22_Poll_n_Publish():
	#Read data from DHT22 Sensor
	json_Data = read_DHT22()
	#Publish sensor data on MQTT Broker
	mqtt_Topic = MQTT_Settings['DHT22_TPC']	
	MQTT_Publish_Master(mqtt_Topic,json_Data)
#======================================================


#======================================================
# BMP180 Sensor
#======================================================
def BMP180_Poll_n_Publish():
	#Read data from BMP180 Sensor
	json_Data = read_BMP180()
	#Publish sensor data on MQTT Broker
	mqtt_Topic = MQTT_Settings['BMP180_TPC']	
	MQTT_Publish_Master(mqtt_Topic,json_Data)
#======================================================
	
	
#======================================================
# Photocell Based Light Sensor
#======================================================
def LIGHT_Poll_n_Publish():
	#Read data from LIGHT Sensor
	json_Data = read_LIGHT()
	#Publish sensor data on MQTT Broker
	mqtt_Topic = MQTT_Settings['LIGHT_TPC']	
	MQTT_Publish_Master(mqtt_Topic,json_Data)
#======================================================


#======================================================
# Polling Master
#======================================================
def Sensor_Master():
	print "Polling Now..."

	#==============================================#
	if Str_To_Boolean(STATUS_LED_Settings['ENABLED']) == True:
		#Turn ON Status LED
		status_LED_ON()
	#==============================================#
	
	if Str_To_Boolean(DHT22_Settings['ENABLED']) == True:
		DHT22_Poll_n_Publish()
	
	if Str_To_Boolean(BMP180_Settings['ENABLED']) == True:
		BMP180_Poll_n_Publish()
		
	if Str_To_Boolean(LIGHT_Settings['ENABLED']) == True:
		LIGHT_Poll_n_Publish()

	#==============================================#
	if Str_To_Boolean(STATUS_LED_Settings['ENABLED']) == True:
		#Turn OFF Status LED
		status_LED_OFF()
	#==============================================#

#======================================================		


#Schedule the repeated Call for sensor Polling
rt = RepeatedTimer(int(SYSTEM_Settings['POLLING_INTERVAL']), Sensor_Master)


###########################################################
###########################################################
# SENSOR POLLING BLOCK (END)
###########################################################
###########################################################	


#==========================================================
#==========================================================


###########################################################
###########################################################
# SENSOR EVENT LISTENER BLOCK (START)
###########################################################
###########################################################	

#======================================================
# PIR Motion Sensor 
#======================================================
def motion_Event_Listener(json_Data, motion_flag):
	#=======================================
	if motion_flag == True:
		# Motion Detected 
		print "Motion Detected"
		
		#Start Capturing Video
		start_Video_Capture(json_Data)
		
		# Start Capturing Time Lapse Pictures
		#start_Time_Lapse_Photo_Capture(json_Data)
		
		# Post Event on Facebook and Twitter
		#Motion_Event_Dict = json.loads(json_Data)
		#gDrive_Folder_Link = get_GDrive_PiCam_Data_Path(Motion_Event_Dict['sid'],Motion_Event_Dict['dt'])
		
		# Facebook Post
		#if Str_To_Boolean(FACEBOOK_Settings['ENABLED']) == True:
		#	post_on_Facebook("Motion Detected at Sensor: " + Motion_Event_Dict['sid'] + " Pictures will be uploaded soon at " + gDrive_Folder_Link)
		
		# Twitter Post
		#if Str_To_Boolean(TWITTER_Settings['ENABLED']) == True:
		#	publish_Status_On_Twitter("Motion Detected at Sensor: " + Motion_Event_Dict['sid'] + " Pictures will be uploaded soon at " + gDrive_Folder_Link)
		
		# SMS
		#if Str_To_Boolean(WAYS2SMS_Settings['ENABLED']) == True:
		#	send_SMS('9900083747', "Motion Detected at Sensor: " + Motion_Event_Dict['sid'] + " Pictures will be uploaded soon at " + gDrive_Folder_Link)
		
	else:
		# Motion Stopped
		print "Motion Stopped"

				
	#Publish motion event on MQTT Broker
	mqtt_Topic = MQTT_Settings['MOTION_TPC']	
	MQTT_Publish_Master(mqtt_Topic,json_Data)
	#=======================================

#Initiate Motion Sensor Service with Event Listener Function Name
if Str_To_Boolean(Motion_Sensor_Settings['ENABLED']) == True:
	pir_Obj = PIR_Sensor()
	pir_Obj.monitor_PIR_Motion_Sensor(motion_Event_Listener)

#Start File Upload Service
if (Str_To_Boolean(Camera_Settings['ENABLED']) == True) and (Str_To_Boolean(GOOGLE_DRIVE_Settings['ENABLED']) == True):
	PiCam_GDrive_YouTube_Upload_Service()

#======================================================

###########################################################
###########################################################
# SENSOR EVENT LISTENER BLOCK (END)
###########################################################
###########################################################	