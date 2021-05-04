import socket, threading
import json
from math import *

LOCALHOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (LOCALHOST, PORT)

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("[New connection added]: ", clientAddress)
    def run(self):
        operation = ''
        while True:
            data = self.csocket.recv(1024)
            answer = data.decode()

            if answer == 'exit()':
                print("[Connection terminated.]")
                break

            result = eval(answer)

            print ("RECEIVED: ", answer)
            print ("RETURNED: ", result)

            self.csocket.send(bytes(str(result),'UTF-8'))
        print ("[Client at ", clientAddress , " disconnected...]")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)
print("[Server is starting...]")

while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    print(clientsock)
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()