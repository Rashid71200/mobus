from pymodbus.client.sync import ModbusSerialClient
from pymodbus.payload import BinaryPayloadDecoder, BinaryPayloadBuilder, Endian
import time
import struct

import tkinter as tk
import webbrowser

def open_link(event):
    webbrowser.open("https://ahrneloy.github.io/")


def update_text():
    try:
        client.connect()

        
        # Read the holding register values
        response1 = client.read_holding_registers(address=3546, count=2, unit=1)
        response2 = client.read_holding_registers(address=3646, count=2, unit=1)
        response3 = client.read_holding_registers(address=3746, count=2, unit=1)
        response4 = client.read_holding_registers(address=3846, count=2, unit=1)

        if response1.isError():
            print(f"Request error: {response1}")
        else:
            # Extract the values from the response
            val01 = response1.registers[0]
            val11 = response1.registers[1]
            #vavg = int_to_float(val11, val01)
            #print("Voltage =", val01, "V")
            #print("Voltage =", val11, "V")

            decoder = BinaryPayloadDecoder.fromRegisters(response1.registers, Endian.Big, wordorder=Endian.Little)
            #print("Voltage =", decoder.decode_32bit_float(), "V")
            canvas.itemconfig(text1, text=str( round(decoder.decode_32bit_float(), 2)))


            decoder1 = BinaryPayloadDecoder.fromRegisters(response2.registers, Endian.Big, wordorder=Endian.Little)
            canvas.itemconfig(text2, text=str( round(decoder1.decode_32bit_float(), 2)))

            decoder2 = BinaryPayloadDecoder.fromRegisters(response3.registers, Endian.Big, wordorder=Endian.Little)
            canvas.itemconfig(text3, text=str(round(decoder2.decode_32bit_float(), 2)))


            decoder3 = BinaryPayloadDecoder.fromRegisters(response4.registers, Endian.Big, wordorder=Endian.Little)
            canvas.itemconfig(text5, text=str(round(decoder3.decode_32bit_float(), 2)))

            #print(str(round(decoder3.decode_32bit_float(), 2)))

            root.after(1000, update_text)
            #time.sleep(1.0)

            # Wait for 1 second before the next read

    except Exception as e:
        print("Error:", e)

    finally:
        client.close()




'''
def int_to_float(data0, data1):
    combined_data = (data0 << 16) | data1
    float_bytes = combined_data.to_bytes(4, byteorder='big', signed=False)
    result = struct.unpack('>f', float_bytes)[0]
    return result
'''




client = ModbusSerialClient(
        method='rtu',
        port='COM6',
        baudrate=9600,
        bytesize=8,
        parity='E',
        stopbits=1,
        timeout=1
    )


value = [ 11.11,
         22.22,
         33.33,
         44.44 ]


# Create the main window
root = tk.Tk()

# Set the window size
root.geometry("832x861")

# Create a Canvas widget to hold the image and text
canvas = tk.Canvas(root, width=832, height=861)
canvas.pack()

# Load and display the image
image = tk.PhotoImage(file="C:/Users/AhrNeloy/Desktop/final_dash_board_code/modbus_python_V2/Schneider_meter1.png")
canvas.create_image(0, 0, anchor="nw", image=image)

# Create and place the text labels
text1 = canvas.create_text(400, 284, text=value[0], fill="black", font=("Arial", 35, "bold"), anchor="center")
text2 = canvas.create_text(400, 361, text=value[3], fill="black", font=("Arial", 35, "bold"), anchor="center")


text3 = canvas.create_text(400, 435, text=value[1], fill="black", font=("Arial", 35, "bold"), anchor="center")
text5 = canvas.create_text(400, 512, text=value[2], fill="black", font=("Arial", 35, "bold"), anchor="center")

text4 = canvas.create_text(400, 832, text="©Azaharul Rashid", fill="#e0e0e4", font=("Arial", 22, "bold"), anchor="center")
canvas.tag_bind(text4, "<Button-1>", open_link)
canvas.tag_bind(text4, "<Enter>", lambda e: canvas.itemconfig(text4, fill="red"))
canvas.tag_bind(text4, "<Leave>", lambda e: canvas.itemconfig(text4, fill="blue"))

update_text()

# Start the main loop
root.mainloop()