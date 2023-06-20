import paho.mqtt.client as mqtt
from pymodbus.client.sync import ModbusSerialClient
from datetime import datetime
import time
import json

variable_value = 20
valueBackup = 0

def backup_modbus(address, l):
    global valueBackup
    client = ModbusSerialClient(method="rtu", port="COM5", stopbits=1, bytesize=8, parity='N', baudrate=9600)
    try:
        client.connect()
        result = client.read_holding_registers(address=address, count=1, unit=(l + 1))
        valueBackup = result.registers[0]
    except:
        time.sleep(1)
        backup_modbus(address, l)

    print("reading from backup....................................................................................................... ")
    return valueBackup


def start_modbus(variable_value):
    b = variable_value
    l_values = []  # List to store the values from each slave
    client = ModbusSerialClient(method="rtu", port="COM5", stopbits=1, bytesize=8, parity='N', baudrate=9600)

    try:
        client.connect()
    except:
        time.sleep(4)
        start_modbus(variable_value)

    for l in range(b):  # Iterate over the slave addresses (1 to b)
        print(f"number of loop {l}")
        valueS = []  # List to store the key-value pairs for each slave

        update_values = {
            "voltage": 3546,
            "current": 3654,
            "frequency": 3756,
            "power": 3878
        }

        for key, address in update_values.items():
            # Reading Holding Registers.............................
            try:
                result = client.read_holding_registers(address=address, count=1, unit=(l + 1))
                value = result.registers[0]
            except:
                time.sleep(1)
                value = backup_modbus(address, l)
            # .......................................................

            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            valueS.append({key: value})  # Format key and value as a dictionary

        l_values.append(valueS)
        print('time to sleep')
        time.sleep(0.01)

    client.close()
    return l_values  # Return the list of dictionaries


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))


def send_data_to_mqtt(value):
    broker_address = 'localhost'
    broker_port = 1883
    client = mqtt.Client()

    client.on_connect = on_connect

    try:
        client.connect(broker_address, broker_port, 60)
        client.loop_start()

        topic = 'data'
        payload = json.dumps({'value': value})
        client.publish(topic, payload)
        print('Data sent successfully')
    except ConnectionRefusedError as e:
        print(f'An error occurred: {e}')
        send_data_to_mqtt(value)
    finally:
        client.loop_stop()
        client.disconnect()


while True:
    value = start_modbus(variable_value)
    send_data_to_mqtt(value)
    time.sleep(5)