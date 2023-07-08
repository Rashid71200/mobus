from pymodbus.constants import Endian
from pymodbus.client.sync import ModbusSerialClient
from pymodbus.payload import BinaryPayloadDecoder
import time

# Configure the Modbus RTU client
client = ModbusSerialClient(method='rtu', port='COM8', baudrate=9600, stopbits=1, bytesize=8, parity='N')
client.connect()

try:
    while True:
        # Read the holding register value from the ESP8266
        response = client.read_holding_registers(address=3926, count=2, unit=1)
        if response.isError():
            print(f"Request result: {response}")
        else:
            valueReceived = response.registers[0]
            print(f"Received: {valueReceived}")
            decoder = BinaryPayloadDecoder.fromRegisters(response.registers, Endian.Big, wordorder=Endian.Little)
            reading = decoder.decode_32bit_float()
            print("Voltage: " + str(reading) + "V")
        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    # Close the Modbus RTU client connection
    client.close()