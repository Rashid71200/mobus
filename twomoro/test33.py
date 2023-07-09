from pymodbus.client.sync import ModbusSerialClient
from pymodbus.payload import BinaryPayloadDecoder, BinaryPayloadBuilder, Endian
import time
import struct

client = ModbusSerialClient(
        method='rtu',
        port='COM6',
        baudrate=9600,
        bytesize=8,
        parity='E',
        stopbits=1,
        timeout=1
    )


client.connect()

        
# Read the holding register values
response1 = client.read_holding_registers(address=3746, count=2, unit=1)

decoder = BinaryPayloadDecoder.fromRegisters(response1.registers, Endian.Big, wordorder=Endian.Little)
print(decoder.decode_32bit_float())

#print(response1.registers[0])
#print(response1.registers[1])