from pymodbus.client.sync import ModbusSerialClient
import time
import struct

def int_to_float(data0, data1):
    combined_data = (data0 << 16) | data1
    float_bytes = combined_data.to_bytes(4, byteorder='big', signed=False)
    result = struct.unpack('>f', float_bytes)[0]
    return result

if __name__ == "__main__":
    # Create Modbus RTU client
    client = ModbusSerialClient(
        method='rtu',
        port='COM5',
        baudrate=9600,
        bytesize=8,
        parity='E',
        stopbits=1,
        timeout=1
    )

    try:
        client.connect()

        while True:
            # Read the holding register values
            response = client.read_holding_registers(address=3546, count=2, unit=1)

            if response.isError():
                print(f"Request error: {response}")
            else:
                # Extract the values from the response
                val0 = response.registers[0]
                val1 = response.registers[1]

                print("Register Values")
                print(val0)
                print(val1)

                voltage = int_to_float(val1, val0)
                print("Voltage =", voltage, "V")

            time.sleep(1.0)  # Wait for 1 second before the next read

    except Exception as e:
        print("Error:", e)

    finally:
        client.close()