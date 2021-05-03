import socket, threading
from math import *

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("[New connection added]: ", clientAddress)
    def run(self):
        operation = ''
        while True:
            data = self.csocket.recv(1024)
            operation = data.decode()

            if operation == 'exit()':
                print("[Connection terminated.]")
                break

            result = eval(operation)

            print ("RECEIVED: ", operation)
            print ("RETURNED: ", result)

            self.csocket.send(bytes(str(result),'UTF-8'))
        print ("[Client at ", clientAddress , " disconnected...]")

LOCALHOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (LOCALHOST, PORT)

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