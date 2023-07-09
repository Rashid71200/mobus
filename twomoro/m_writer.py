from pymodbus.payload import BinaryPayloadDecoder, BinaryPayloadBuilder, Endian
from pymodbus.client.sync import ModbusSerialClient

client = ModbusSerialClient(method="rtu", port="COM6", stopbits=1, bytesize=8, parity='N', baudrate=9600)
client.connect()

builder = BinaryPayloadBuilder(byteorder=Endian.Big, wordorder=Endian.Little)
builder.add_32bit_float(45.77)
payload = builder.build()
client.write_registers(3546, payload, count=2, unit=1, skip_encode=True)



builder1 = BinaryPayloadBuilder(byteorder=Endian.Big, wordorder=Endian.Little)
builder1.add_32bit_float(35.77)
payload1 = builder1.build()
client.write_registers(3646, payload1, count=2, unit=1, skip_encode=True)


builder2 = BinaryPayloadBuilder(byteorder=Endian.Big, wordorder=Endian.Little)
builder2.add_32bit_float(75.77)
payload2 = builder2.build()
client.write_registers(3746, payload2, count=2, unit=1, skip_encode=True)


builder3 = BinaryPayloadBuilder(byteorder=Endian.Big, wordorder=Endian.Little)
builder3.add_32bit_float(99.77)
payload3 = builder3.build()
client.write_registers(3846, payload3, count=2, unit=1, skip_encode=True)