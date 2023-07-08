from pymodbus.client.sync import ModbusSerialClient

# Configure the Modbus RTU client
client = ModbusSerialClient(method='rtu', port='COM8', baudrate=9600, stopbits=1, bytesize=8, parity='N')
client.connect()

while True:
    # Read the holding register value from the ESP8266
    response = client.read_holding_registers(address=3926, count=1, unit=1)
    if response.isError():
        print(f"Request result: {response}")
    else:
        valueReceived = response.registers[0]
        print(f"Received: {valueReceived}")

client.close()