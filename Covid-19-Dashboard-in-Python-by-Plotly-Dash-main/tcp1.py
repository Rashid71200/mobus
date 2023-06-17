import socket
import threading
import random
import time

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

msg = ""  # Declare msg as a global variable

def handle_client(conn, addr):
    global msg  # Declare msg as a global variable

    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        msg = conn.recv(1024).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            break

        print(f"[{addr}] {msg}")
        #conn.send("Message received".encode(FORMAT))

        for i in range(1000):
            a = random.randint(1, 20)
            #conn.send(str(a).encode(FORMAT))
            conn.send(bytes(str(random.randint(1, 20)), 'utf-8'))
            time.sleep(2)


    conn.close()
    print(f"[CONNECTION CLOSED] {addr} disconnected.")

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

start()

print(f"rsyyr{msg}")
