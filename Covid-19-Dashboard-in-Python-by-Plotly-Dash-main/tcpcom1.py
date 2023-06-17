import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

print(f"The name of server {socket.gethostname()}")
print(f"The address of server {SERVER}")

ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
usear = {}
usearconn = {}
usearconn1 = []

def broadcast_message(message):
    for conn in usearconn1:
        conn.send(message)
    #

def handle_client(conn, addr):
    connected = True
    user_id = f"User{len(usear)}"
    usear[addr[1]] = user_id
    usearconn1.append(conn)
    print(f"[NEW CONNECTION] {user_id} connected from {addr[1]}")

    while connected:
        msg_length = int(conn.recv(HEADER).decode(FORMAT))
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            conn.close()
            usearconn1.remove(conn)
            break


        print(f"[{user_id}] {msg}")
        message = f'[{user_id}] {msg}'.encode(FORMAT)
        broadcast_message(message)

def start_server():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

if __name__ == '__main__':
    print("[STARTING] Server is starting...")
    start_server()