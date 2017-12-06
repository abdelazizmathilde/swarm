import socket
import threading
from display import *

from ubidots import ApiClient

api = ApiClient(token='A1E-1QStnv5NBmTFatVnrL31BJfsZntBTY')


data_swarm = []
data_swarm1 = []
data_swarm2 = []
data_swarm3 = []
cycle = 0
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
            global cycle
            cycle+=1


        if cycle==1:
                    for x in range(len(data_swarm1)):
                        swarm1=data_swarm1[x]
                        distance_mesure_swarm1 = str(swarm1[29:34])
                        angle_mesure_swarm1 = str(swarm1[45:48])

                        api.save_collection([{'variable': '5a16bf9bc03f973145034cca', 'value': distance_mesure_swarm1},{'variable': '5a16bfa5c03f97312ede5031', 'value': angle_mesure_swarm1}])
                    for y in range(len(data_swarm2)):
                        swarm2=data_swarm2[y]
                        distance_mesure_swarm2 = str(swarm2[29:34])
                        angle_mesure_swarm2 = str(swarm2[45:48])

                        api.save_collection([{'variable': '5a16bb35c03f972c0b94f23e', 'value': distance_mesure_swarm2},{'variable': '5a16ba3ac03f972accc08c43', 'value': angle_mesure_swarm2}])
                    display_data_swarm(data_swarm1,1)
                    display_data_swarm(data_swarm2, 2)
                    display_data_swarm(data_swarm3, 3)
                    data_swarm1[:] = []
                    data_swarm2[:] = []
                    data_swarm3[:] = []
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 1112))

while n == 0:
    tcpsock.listen(10)
    print("En ecoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()






