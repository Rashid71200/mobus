from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'  # Replace 'secret_key' with your secret key
socketio = SocketIO(app)

variable_value = 20  # Assuming you have a variable_value that you want to pass to the template

@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json
    value = data.get('value')

    # Process the received value as needed
    print(f'Received value from script1: {value}')

    # Update the variable_value with the received value
    global variable_value
    #variable_value = value

    # Emit a SocketIO event to update the clients
    socketio.emit('update', {'value': value}, namespace='/')

    # Return a response if needed
    return 'Data received'

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("styledashboard.html", variable_value=variable_value)

if __name__ == '__main__':
    socketio.run(app)



[
    [{'voltage': 69}, {'current': 53}, {'frequency': 52}, {'power': 25}],
    [{'voltage': 62}, {'current': 39}, {'frequency': 80}, {'power': 70}],
    [{'voltage': 45}, {'current': 35}, {'frequency': 33}, {'power': 65}],
    [{'voltage': 44}, {'current': 56}, {'frequency': 22}, {'power': 33}],
    [{'voltage': 73}, {'current': 55}, {'frequency': 46}, {'power': 42}],
    [{'voltage': 76}, {'current': 60}, {'frequency': 23}, {'power': 36}],
    [{'voltage': 46}, {'current': 21}, {'frequency': 32}, {'power': 53}],
    [{'voltage': 37}, {'current': 48}, {'frequency': 35}, {'power': 71}],
    [{'voltage': 45}, {'current': 42}, {'frequency': 54}, {'power': 52}],
    [{'voltage': 35}, {'current': 76}, {'frequency': 61}, {'power': 60}],
    [{'voltage': 20}, {'current': 44}, {'frequency': 34}, {'power': 74}],
    [{'voltage': 54}, {'current': 36}, {'frequency': 68}, {'power': 76}],
    [{'voltage': 64}, {'current': 21}, {'frequency': 46}, {'power': 45}],
    [{'voltage': 67}, {'current': 61}, {'frequency': 63}, {'power': 55}],
    [{'voltage': 77}, {'current': 72}, {'frequency': 66}, {'power': 70}],
    [{'voltage': 43}, {'current': 43}, {'frequency': 65}, {'power': 70}],
    [{'voltage': 66}, {'current': 41}, {'frequency': 59}, {'power': 43}],
    [{'voltage': 31}, {'current': 41}, {'frequency': 54}, {'power': 76}],
    [{'voltage': 25}, {'current': 58}, {'frequency': 42}, {'power': 73}],
    [{'voltage': 65}, {'current': 75}, {'frequency': 50}, {'power': 53}]
]