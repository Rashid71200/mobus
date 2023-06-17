import socket
import threading

FORMAT = 'utf-8'

#host = socket.gethostbyname(socket.gethostname())
host = input('IP Address of Server' )

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, 5050))

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode(FORMAT)
            if message == 'NICK':
                client.send(nickname.encode(FORMAT))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

# Sending Messages To Server
def write():
    while True:
        #message = '{}: {}'.format(nickname, input(''))
        message = '{}'.format(int(64))
        client.send(message.encode(FORMAT))
        message = '{}'.format(input('message '))
        client.send(message.encode(FORMAT))

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()