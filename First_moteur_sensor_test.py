#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep
# TODO: Add code here


# initialize the motor 
m = LargeMotor('outA')

# initialize the ultrasonic sensor

us = UltrasonicSensor() 
assert us.connected, "Connect a single US sensor to any sensor port"
us.mode='US-DIST-CM'
units = us.units

# initialize the variable
degre = 0



# Loop for the robot erotation 360 degres

for i in range(0, 19):

	m.run_to_rel_pos(position_sp=degre, speed_sp=500, stop_action="brake")

	degre = degre + 8

	distance = us.value()/10  # convert mm to cm

	print(" The distance between the robot and the obstacle is :" + str(distance) + units)

	print(degre)
	
	sleep(0.2)




ev3.Sound.speak('Welcome to the E V 3 dev project!').wait()
