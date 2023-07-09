from pymodbus.client.sync import ModbusSerialClient
import time
import random

client = ModbusSerialClient(method="rtu", port="COM7", stopbits=1, bytesize=8, parity='N', baudrate=9600)

update_values = {
        "voltage": 3926,
        "current": 3654,
        "frequency": 3756,
        "power": 3878
    }


while True:

    z= 0

    for k in range(20):

        try:
            client.connect()
            #print('Connected')

            for values in update_values.items():
                #print(f'in loop {values}')
                data = random.randint(20, 80)
                print(k)
                result_ = client.write_registers(values[1], data , unit=(k+1))
                #result_ = client.write_registers(3878, 99 , unit=2)
                #print('data retten')
                value = result_

                print(f'{values[0]} : {value}')

        except:
            time.sleep(1)
    client.close()
    time.sleep(5)
        

