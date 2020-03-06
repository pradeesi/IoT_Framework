import paho.mqtt.client as mqtt

def on_connect(mosq, obj, rc):
    mqttc.subscribe("/india/karnataka/bangalore/ecity/ajmera/avenye/7", 0)
    print("rc: " + str(rc))

def on_message(mosq, obj, msg):
	print msg.topic
	print str(msg.qos)
	print str(msg.payload)

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
# Connect
mqttc.connect("iot.eclipse.org", 1883,60)


# Continue the network loop
mqttc.loop_forever()