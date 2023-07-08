from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.transaction import ModbusRtuFramer as ModbusFramer
import time

client = ModbusTcpClient( 'xxx', port=yy,framer=ModbusFramer)
#update xxx with IP of the IP of the RS485-Ethernet adapter and yy with port number of the RS485-Ethernet adapter

while True:
	response = client.read_holding_registers(3926, 2, unit=1)
	assert(not response.isError())    
	decoder = BinaryPayloadDecoder.fromRegisters(response.registers, Endian.Big, wordorder=Endian.Little)
	reading=decoder.decode_32bit_float()
	print ("Voltage: " + str(reading) + "V")
	# Read Frequency
	response = client.read_holding_registers(3914, 2, unit=1)
	assert(not response.isError())    
	decoder = BinaryPayloadDecoder.fromRegisters(response.registers, Endian.Big, wordorder=Endian.Little)
	reading=decoder.decode_32bit_float()
	print ("Frequency: " + str(reading) + "Hz")
	client.close()
	time.sleep(1)