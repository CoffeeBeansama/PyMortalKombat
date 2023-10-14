import socket
from _thread import *
from player import Player
import pickle

server = "192.168.1.9"
port = 5555

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    print(e)

s.listen()
print("Waiting for connection...Server started!")


players = {
            0: {"x": 0, "y": 0,"width": 100,"height": 100,"color": (0,255,0)},
            1: {"x": 100, "y": 100,"width": 100,"height": 100,"color": (0,0,0)}
            }

gameIdCount = 0


def threadedClient(conn,player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data
            if not data:
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Connection lost")
    conn.close()


currentPlayers = 0
while True:
    conn,addr = s.accept()
    start_new_thread(threadedClient,(conn,currentPlayers))
    currentPlayers += 1
    if currentPlayers >= 3:
        currentPlayers -= 1







