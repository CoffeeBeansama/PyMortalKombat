import socket
from _thread import *
import pickle
from gamedata import Game
from settings import ip_address

class Server:
    def __init__(self):
        self.server = ip_address

        self.port = 5559
        self._socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        self.gameIdCount = 0

        self.games = {}
        self.idCount = 0

        self.startServer()

        self.currentPlayers = 0

    def startServer(self):
        try:
            self._socket.bind((self.server,self.port))
        except socket.error as e:
            pass

        self._socket.listen()
        print("Waiting for connection...Server started!")

    def threadedClient(self,conn,player,gameId):
        conn.send(str.encode(str(player)))

        reply = ""
        while True:
            try:
                data = conn.recv(4068).decode()
                if gameId in self.games:
                    game = self.games[gameId]
                    if not data:
                        break
                    else:
                        if data != "get":
                           match player:
                               case 0:    
                                   game.updatePlayerOneData(data)
                               case 1:
                                   game.updatePlayerTwoData(data)
                                 
                        conn.sendall(pickle.dumps(game))
                else:
                    break
            except:
                
                break
        
        print("Lost connection")

        try:
            del self.games[gameId]
        except:
            
            pass
        
        self.idCount -= 1
        conn.close()
        
        print("Connection lost")
        conn.close()

    def run(self):
        while True:
            conn,addr = self._socket.accept()

            self.idCount += 1
            player = 0
            gameId = (self.idCount -1) // 2

            if self.idCount % 2 == 1:
                self.games[gameId] = Game(gameId)
            else:
                player = 1

            
            start_new_thread(self.threadedClient,(conn,player,gameId))
           




server = Server()
server.run()