from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder

UNIT = 0x1

client= ModbusClient(method = "rtu", port="",stopbits = 1, bytesize = 8, parity = 'E', baudrate= 9600)
#modify port with com port of the USB device (eg COM3 in windows or /dev/ttyUSB0 in linux)
client.connect()
response = client.read_holding_registers(3926, 2, unit=UNIT)
decoder = BinaryPayloadDecoder.fromRegisters(response.registers, Endian.Big, wordorder=Endian.Little)
print ("read_holding_registers: " + str(decoder.decode_32bit_float()))
  
client.close()