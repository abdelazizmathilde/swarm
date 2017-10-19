
from ev3dev.ev3 import *
from time import sleep
import threading
import socket
from ultrasonic_function import *
from compas_function import *
from client import *
from display import *

mA = LargeMotor('outA')
mB = LargeMotor('outB')
ultrasonic = UltrasonicSensor()
assert ultrasonic.connected
gyroscope = GyroSensor()
assert gyroscope.connected

status = "online"


display_status_swarm_robot(1)
n=0

while n <= 30:
    print("Swarm1 Status: Online",end=" \r")
    mB.run_to_rel_pos(position_sp=200, speed_sp=900, stop_action="hold")

    sleep(0.9)
    distance_value = mesure_distance(ultrasonic, "distance")
    if distance_value > 100:
        distance_value = "infinite"

    angle_value= mesure_position(gyroscope,"angle")

    value = "Swarm1 --->Distance detected "+ str(distance_value) +" position : "+str(angle_value)
    client_send_data('localhost', 1111, value)
    n = n+2



client_send_data('localhost', 1111, "")



