import serial
import time
import random

# Register address for the random integer
REGISTER_ADDRESS = 3546

# Configure the serial port
port = serial.Serial('COM5', baudrate=9600, timeout=1)

def calculate_crc(data):
    # CRC calculation
    crc = 0xFFFF
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x0001:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc.to_bytes(2, byteorder='little')

def process_request(request):
    # Extract data from the request
    slave_address = request[0]
    function_code = request[1]
    register_address = int.from_bytes(request[2:4], byteorder='big')

    if function_code == 3:
        # Read Holding Registers
        register_count = int.from_bytes(request[4:6], byteorder='big')

        if register_address == REGISTER_ADDRESS and register_count == 1:
            # Generate a random integer for the register value
            register_value = random.randint(0, 65535)

            # Prepare response data
            response_data = register_value.to_bytes(2, byteorder='big')

            # Calculate CRC
            crc = calculate_crc(request[0:6] + response_data)

            # Prepare response
            response = bytearray([slave_address, function_code, 2, response_data[0], response_data[1]]) + crc
            port.write(response)
        else:
            # Invalid register address or count
            # Prepare exception response
            response = bytearray([slave_address, function_code + 0x80, 0x02])
            crc = calculate_crc(response)
            response += crc
            port.write(response)

    else:
        # Unsupported function code
        # Prepare exception response
        response = bytearray([slave_address, function_code + 0x80, 0x01])
        crc = calculate_crc(response)
        response += crc
        port.write(response)

while True:
    # Read incoming data
    if port.inWaiting() > 0:
        data = port.read(port.inWaiting())

        # Check minimum packet length
        if len(data) >= 4:
            # Verify slave address and CRC
            slave_address = data[0]
            crc = calculate_crc(data[:-2])
            if slave_address == 0x01 and crc == data[-2:]:
                # Process the request
                process_request(data[1:-2])

    time.sleep(0.01)

# Close the serial port
port.close()
