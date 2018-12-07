#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
from time import sleep
import sys

from gpiozero import LED as gpioPin

pin21 = gpioPin(21)
pin20 = gpioPin(20)
pin16 = gpioPin(16)
pin26 = gpioPin(26)
pin19 = gpioPin(19)
pin13 = gpioPin(13)

global servo_command
global pubServo_Command
global servo_out
servo_commandList = ["Wave","Point","No","Neutral","Arms_up","Demo"]

# Here is the publisher for servo commands:
#pubservo = rospy.Publisher('servo_command', String, queue_size=1)

def callback0(data):
    servo_out = data.data  


def servo_control():
    rospy.init_node("servo_control", anonymous=True)
    rate = rospy.Rate(10) # 10Hz
    rospy.Subscriber("servo_command", String, callback0)

    if servo_command in servo_commandList:
        if servo_command == "Wave":
            pin21.on()
			pin20.off()
			pin16.off()
			pin26.off()
			pin19.off()
			pin13.off()
            print ("-I am waving")
        
        if servo_command == "Point":
            pin21.off()
			pin20.on()
			pin16.off()
			pin26.off()
			pin19.off()
			pin13.off()
            print ("-I am pointing")
        
        if servo_command == "No":
            pin21.off()
			pin20.off()
			pin16.on()
			pin26.off()
			pin19.off()
			pin13.off()
            print ("-I am gesturing negatively")
        
        if servo_command == "Neutral":
            pin21.off()
			pin20.off()
			pin16.off()
			pin26.on()
			pin19.off()
			pin13.off()
            print ("-I am returning to neutral position")
        
        if servo_command == "Arms_up":
            pin21.off()
			pin20.off()
			pin16.off()
			pin26.off()
			pin19.on()
			pin13.off()
            print ("-I raising my arms")
			
		if servo_command == "Demo":
            pin21.off()
			pin20.off()
			pin16.off()
			pin26.off()
			pin19.off()
			pin13.on()
            print ("-I will run a demo of my actions")
        else:
			pin21.off()
			pin20.off()
			pin16.off()
			pin26.off()
			pin19.off()
			pin13.off()
            print ("unknown command!!")
                
    rospy.spin()

	
if __name__ == '__main__':
	print("Schrodingers Cat - Servo control - running")
	try:
		servo_control()
	except rospy.ROSInterruptException():
		pass
