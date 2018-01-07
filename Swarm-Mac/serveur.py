import socket
import threading
from display import *
from tkinter import *
from ubidots import ApiClient
import multiprocessing
import queue
api = ApiClient(token='A1E-1QStnv5NBmTFatVnrL31BJfsZntBTY')
queue = multiprocessing.Queue(maxsize=1)
queue_end_loop = multiprocessing.Queue(maxsize=1)
data_swarm = []
data_swarm1 = []
data_swarm2 = []
data_swarm3 = []
global cycle
cycle = 0
n=0
fenetre = Tk()
fenetre .geometry("800x300")
fenetre.title('Swarms Result')

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
Label(fenetre, text='State Swarm 1 ' ).place(x= 50 , y=0)
Label(fenetre, text='State Swarm 2').place(x= 350 , y=0)
Label(fenetre, text='State Swarm 3').place(x= 650 , y=0)

def fermer():
    fenetre.destroy()

bouton=Button(fenetre,text='Exit',command=fermer)

bouton.place(x= 400 , y=150)
message_swarm1 = StringVar()
message_swarm1.set('')

message_swarm2 = StringVar()
message_swarm2.set('')

swarm1 = Label(fenetre, textvariable=message_swarm1)
swarm1.place(x= 70 , y=30)
swarm2 = Label(fenetre, textvariable=message_swarm2)
swarm2.place(x= 370 , y=30)

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
        queue.put(response)
        id=str(response[0:6].decode())
        print(response)

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
            display_data_swarm(data_swarm1, 1)
            display_data_swarm(data_swarm2, 2)
            display_data_swarm(data_swarm3, 3)
            data_swarm1[:] = []
            data_swarm2[:] = []
            data_swarm3[:] = []
            queue_end_loop.put("stop")
        else:
            queue_end_loop.put("")
           
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
     





tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 1112))

while n==0:

    tcpsock.listen(10)
    print("En ecoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()
    end_loop=queue_end_loop.get()
    status = queue.get()
    status_string=str(status[0:1].decode())
    if status_string== "1":

        status_ui = str(status[2:12].decode())
        message_swarm1.set(status_ui)
        if status_ui == "connect":
            swarm1.config(background="#90EE90")
        elif status_ui =="disconnect":
            swarm1.config(background="#FF5E4D")
        swarm1.update()
    elif status_string == "2":

        status_ui = str(status[2:12].decode())
        message_swarm2.set(status_ui)
        if status_ui == "connect":
            swarm2.config(background="#90EE90")
        elif status_ui == "disconnect":
            swarm2.config(background="#FF5E4D")
        swarm2.update()

    if end_loop == "stop":
      n=1

    else :
      n=0
fenetre.mainloop()








