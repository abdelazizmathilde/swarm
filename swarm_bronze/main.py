
import sys
from ev3dev.ev3 import *
import time
from ultrasonic_sensor import *


ultrasonic = UltrasonicSensor()
assert ultrasonic.connected


while True:


    distance = mesure_distance(ultrasonic,'distance')
    if distance >= 100:

        distance = "inf-"

    print(distance, end="\r")
    time.sleep(0.5)







