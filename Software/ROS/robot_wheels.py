#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
import time
import sys

global motion_command
global pubMotion_Command
global motion_out
motion_commandList = ["Go_Forward","Turn_Left","Turn_Right","Stop"]

pubmotion = rospy.Publisher('motion_out',Int32, queue_size=1)

def callback0(data)
    motion_out = data.data
    

def callback1(data)
    feedback = data.data

def robot_wheels():
    rospy.init_node("robot_wheels", anonymous=True)
    rate = rospy.Rate(10) # 10Hz
    rospy.Subscriber("motion_command", String, callback0)
    rospy.Subscriber("motion_feedback", String, callback1)

    if motion_command in motion_commandList:
        if motion_command == "Go_Forward":
            motion_out = 1
            print ("-I am moving forward")
        if motion_command == "Turn_left":
            motion_out = 2
            print ("-I am Turning Let")
        if motion_command == "Turn_right"
            motion_out = 3;
            print ("-I am Turning right")
        if motion_command == "Stop"
            motion_out = 4
            print ("-I stopped")
        else:
            print ("unknown comman!!)

    while not rospy.is_shutdown():
        pubmotion.publish(motion_out)
    rate.sleep()
    rospy.spin()

if __name__ == '__main__':
	print("Schrodingers Cat")
	try:
		robot_wheels()
	except rospy.ROSInterruptException():
		pass
