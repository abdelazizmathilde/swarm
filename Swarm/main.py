
from ev3dev.ev3 import *
from time import sleep
import threading
import socket
from ultrasonic_function import *
from compas_function import *
from client import *


mA = LargeMotor('outA')
mB = LargeMotor('outB')
ultrasonic = UltrasonicSensor()
assert ultrasonic.connected
#gyroscope = GyroSensor()
#assert gyroscope.connected


def findeboucle():
    global encore
    encore = False


encore = True 

timer = threading.Timer(16, findeboucle)
timer.start()

data = []


while encore:

    mA.run_forever(speed_sp=400)
    mB.run_forever(speed_sp=400)

    distance = mesure_distance(ultrasonic,'distance')
    print(distance)
    angle = 0
    if distance <= 30:
        mA.stop(stop_action="brake")
        mB.stop(stop_action="brake")
        sleep(1)
        mB.run_to_rel_pos(position_sp=360, speed_sp=600, stop_action="hold")
        sleep(1)
        value= "Swarm1 --->Distance detected "+ str(distance) +" position : "+str(angle)
        data.append(value)




mA.stop(stop_action="brake")
mB.stop(stop_action="brake")

for i in range(len(data)):

    client_send_data('172.20.10.3', 1112, value)



client_send_data('172.20.10.3', 1112, "")




