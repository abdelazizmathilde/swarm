

import socket
import threading
from display import *

global data_table1
global data_table2
global data_table3
class ClientThread(threading.Thread):
    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port,))

    def run(self):
        print("Connection de %s %s" % (self.ip, self.port,))

        response = self.clientsocket.recv(255)
        if response != "":
            if response[0:6] == "Swarm1":
                data_table1.append(response)
            if response[0:6] == "Swarm2":
                data_table2.append(response)
            if response[0:6] == "Swarm3":
                data_table3.append(response)

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 1111))


def findeboucle():
    global encore
    encore = False


encore = True

timer = threading.Timer(16, findeboucle)
timer.start()

while encore:
    tcpsock.listen(10)
    print("En ecoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()


display_data_swarm(data_table1)
display_data_swarm(data_table2)
display_data_swarm(data_table3)

