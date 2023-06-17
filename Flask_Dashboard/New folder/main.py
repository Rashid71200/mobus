from pymodbus.client.sync import ModbusSerialClient
from flask import Flask, render_template, request, session, redirect
from flask_socketio import join_room, leave_room, send, SocketIO
from openpyxl import Workbook
from datetime import datetime
import time


def start_modbus():
    k = ''
    valueS = []
    update_values = {
        "voltage": 3546,
        "current": 3654,
        "frequency": 3756,
        "power": 3878
    }
    value = 0
    client = ModbusSerialClient(method="rtu", port="COM5", stopbits=1, bytesize=8, parity='N', baudrate=9600)
    workbook = Workbook()
    sheet = workbook.active


    try:
        client.connect()

        for key, address in update_values.items():
            result = client.read_holding_registers(address=address, count=1, unit=1)
            value = result.registers[0]
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sheet.append([current_time, key, value])

            x = f"{key}*{value}"  # Format key and value as string
            workbook.save("data.xlsx")
            valueS.append(x)
        
        client.close()

        k = '$'.join(valueS)  # Join the valueS list with '$' as delimiter
        time.sleep(2)
    except:
        time.sleep(1)

    return k.lstrip('$').rstrip('$')


app = Flask(__name__)
app.config["SECRET_KEY"] = "ahrneloy"
socketio = SocketIO(app)

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("styledashboard.html")

@socketio.on("update")
def update_voltage():

    value = start_modbus()
    socketio.emit("update", {"value": value})

if __name__ == "__main__":
    socketio.run(app, debug=True)