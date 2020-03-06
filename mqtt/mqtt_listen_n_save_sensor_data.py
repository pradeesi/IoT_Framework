import paho.mqtt.client as mqtt
from db.sensor_data_to_db import sensor_Data_Handler

from settings.parseSettings import get_Settings
MQTT_Settings = get_Settings('MQTT')

#Subscribe to all Sensors at Base Topic
def on_connect(mosq, obj, rc):
	mqttc.subscribe(MQTT_Settings['MQTT_BASE_TPC'], 0)

#Save Data into DB Table
def on_message(mosq, obj, msg):
	sensor_Data_Handler(msg.topic, msg.payload)
		
def on_subscribe(mosq, obj, mid, granted_qos):
    pass

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect
mqttc.connect(MQTT_Settings['HOST'], int(MQTT_Settings['PORT']), int(MQTT_Settings['KEEPALIVE']))

# Continue the network loop
mqttc.loop_forever()