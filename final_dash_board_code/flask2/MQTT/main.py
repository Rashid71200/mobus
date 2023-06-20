from flask import Flask
import paho.mqtt.client as mqtt

app = Flask(__name__)

def process_received_data(value):
    # Process the received value as needed
    print(f'Received value from MQTT: {value}')

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    client.subscribe('data')  # Subscribe to the MQTT topic

def on_message(client, userdata, msg):
    if msg.topic == 'data':
        payload = msg.payload.decode()
        data = json.loads(payload)
        value = data.get('value')
        process_received_data(value)  # Call the process_received_data function with the received value

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

broker_address = 'localhost'
broker_port = 1883

client.connect(broker_address, broker_port, 60)

client.loop_start()

if __name__ == '__main__':
    app.run()