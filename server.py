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

def readPos(str):
    stringPos = str.split(",")
    return int(stringPos[0]), int(stringPos[1])


def makePos(tup):
    return str(tup[0]) + "," + str(tup[1])


playerPositions = [(0,0),(50,50)]

def threadedClient(conn,player):
    conn.send(str.encode(makePos(playerPositions[player])))
    reply = ""

    while True:
        try:
            data = readPos(conn.recv(2048).decode())
            playerPositions[player] = data

            if not data:
                print("Connection Disconnected!!")
                break
            else:
                match player:
                    case 0:
                        reply = playerPositions[0]
                    case 1:
                        reply = playerPositions[1]

                print(f"Received: {data} from client")
                print(f"Sending: {reply} to client")
            conn.sendall(str.encode(makePos(reply)))
        except:
            break

    print("Connection lost")
    conn.close()


currentPlayers = 0
while True:
    conn,addr = s.accept()
    print("this")
    print(f"Connected to: {addr}")

    start_new_thread(threadedClient,(conn,currentPlayers))
    currentPlayers += 1


