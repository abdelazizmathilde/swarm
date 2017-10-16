
from ev3dev.ev3 import *
from time import sleep
import threading
import urllib.request
import socket
from ultrasonic_function import *
from client import *

Sound.speak('I love you laura !').wait()
mA = LargeMotor('outA')
mB = LargeMotor('outB')
ultrasonic = UltrasonicSensor()
assert ultrasonic.connected


def findeboucle():
    global encore
    encore = False


encore = True

timer = threading.Timer(16, findeboucle)
timer.start()

data = []
distance_last = 0
while encore:
    mA.run_forever(speed_sp=400)
    mB.run_forever(speed_sp=400)

    distance = mesure_distance(ultrasonic,'distance')

    if distance <= 7:

        if distance != distance_last:

            data.append(distance)
            distance_last = distance


    mA.stop(stop_action="hold")
    mB.stop(stop_action="hold")

    mB.run_to_rel_pos(position_sp=360, speed_sp=900, stop_action="hold")





mA.stop(stop_action="brake")
mB.stop(stop_action="brake")

for i in range(len(data)):
    data_send = "Swarm1" + data[i]
    client_send_data('localhost', 1111, data_send)









