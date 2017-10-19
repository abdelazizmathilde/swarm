import socket
import threading
from display import *
data_swarm = []
data_swarm1 = []
data_swarm2 = []
data_swarm3 = []
n=0
class ClientThread(threading.Thread):
    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port,))

    def stop(self):
        self.running = False

    def run(self):
        print("Connection de %s %s" % (self.ip, self.port,))
        response = self.clientsocket.recv(2048)
        id=str(response[0:6].decode())
        if id == "Swarm1":
            data_swarm1.append(response.decode())
        if id == "Swarm2":
            data_swarm2.append(response.decode())
        if id == "Swarm3":
            data_swarm3.append(response.decode())

        if id == "":
            display_data_swarm(data_swarm1,1)
            display_data_swarm(data_swarm2, 2)
            display_data_swarm(data_swarm3, 3)
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 1111))

while n == 0:
    tcpsock.listen(10)
    print("En ecoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()






