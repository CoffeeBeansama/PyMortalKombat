import socket
from _thread import *

server = "192.168.1.12"
port = 5555

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    print(e)

s.listen(2)
print("Waiting for connection...Server started!")

def threadedClient(conn):
    conn.send(str.encode("Hello from server"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            if not data:
                print("Connection Disconnected!!")
                break
            else:
                print(f"Received: {reply} from client")
                print(f"Sending: {reply} to client")
            conn.sendall(str.encode(reply))
        except:
            break

    print("Connection lost")
    conn.close()

while True:
    conn,addr = s.accept()
    print("this")
    print(f"Connected to: {addr}")

    start_new_thread(threadedClient,(conn,))


