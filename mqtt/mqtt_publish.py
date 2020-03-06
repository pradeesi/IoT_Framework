import paho.mqtt.client as mqtt
from settings.parseSettings import get_Settings

MQTT_Settings = get_Settings('MQTT')

def on_connect(client, userdata, rc):
	if rc != 0:
		pass
		#print "Unable to connect to MQTT Broker..."

def on_publish(client, userdata, mid):
	pass
	#print mid
		
def on_disconnect(client, userdata, rc):
	if rc !=0:
		pass
		#print "Unable to disconnect from MQTT Broker..."
		
		
class MQTT_Publish:
		
	def __init__(self):
		mqttc = mqtt.Client()
		mqttc.on_connect = on_connect
		mqttc.on_disconnect = on_disconnect
		mqttc.on_publish = on_publish
		mqttc.connect(MQTT_Settings['HOST'], int(MQTT_Settings['PORT']), int(MQTT_Settings['KEEPALIVE']))		
		self.mqtt_Client = mqttc
		
	def publish_To_Topic(self, topic, message):
		self.mqtt_Client.publish(topic,message)

	def __del__(self):
		self.mqtt_Client.disconnect()



