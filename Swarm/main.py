
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
gyroscope = GyroSensor()
assert gyroscope.connected


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

    if distance <= 3:

            angle = mesure_position(gyroscope,'angle')
            value = "Distance between robot and obstacle is:"+ str(distance) + " with an angle of :"+ str(angle)
            data.append(value)
            distance_last = distance


    mA.stop(stop_action="hold")
    mB.stop(stop_action="hold")

    mB.run_to_rel_pos(position_sp=360, speed_sp=900, stop_action="hold")





mA.stop(stop_action="brake")
mB.stop(stop_action="brake")

for i in range(len(data)):
    value="Swarm1 ->"+ str(data[i])
    print(value)
    client_send_data('localhost', 1111,value)








