import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    client.subscribe("data")

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload)
    value = payload['value']
    # Process the received value as needed
    print("Received value:", value)

broker_address = 'localhost'
broker_port = 1883

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, broker_port, 60)
client.loop_forever()