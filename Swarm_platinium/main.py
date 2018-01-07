
from ev3dev.ev3 import *
from time import sleep
import time
import threading
import socket
from ultrasonic_function import *
from compas_function import *
from client import *


mA = LargeMotor('outA')
mB = LargeMotor('outB')
ultrasonic = UltrasonicSensor()
assert ultrasonic.connected


speed_swarm = 0.13
heading=360;
def findeboucle():
    global encore
    encore = False


encore = True 

timer = threading.Timer(30, findeboucle)
timer.start()




while encore:
    '''value_swarm1 = "1.connect" '''
    client_send_data('192.168.1.22', 1112, value_swarm1)
    tmps1 = time.time()
    mA.run_forever(speed_sp=400)
    mB.run_forever(speed_sp=400)

    distance_object = mesure_distance(ultrasonic,'distance')

    if distance_object <= 30:
        tmps2 = time.time()-tmps1
        distance_parcour =speed_swarm*tmps2
        mA.stop(stop_action="brake")
        mB.stop(stop_action="brake")
        sleep(1)
        mB.run_to_rel_pos(position_sp=360, speed_sp=600, stop_action="hold")
        sleep(1)
        value= "Swarm1 --->Distance detected "+ str(distance_object) +" position : "+str(heading)+"Distance parcouru :"+str(distance_parcour)
        client_send_data('192.168.1.22', 1112, value)
        if heading == 0:
            heading = 360

        heading = heading - 90
        sleep(2)




mA.stop(stop_action="brake")
mB.stop(stop_action="brake")

client_send_data('192.168.1.22', 1112, "")




