#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
import time
import sys
from pyfirmata import Arduino, util
board = Arduino('/dev/ttyUSB0')

global motion_command
global pubMotion_Command
global motion_out
motion_commandList = ["Go_Forward","Go_Backward","Turn_Left","Turn_Right","Stop"]

#pubmotion = rospy.Publisher('motion_out',Int32, queue_size=1)

def callback0(data):
    motion_out = data.data
    

def callback1(data):
    feedback = data.data

def robot_wheels():
    rospy.init_node("robot_wheels", anonymous=True)
    rate = rospy.Rate(10) # 10Hz
    rospy.Subscriber("motion_command", String, callback0)
    rospy.Subscriber("motion_feedback", String, callback1)

    if motion_command in motion_commandList:
        if motion_command == "Go_Forward":
            pin2 = board.getpin('d:2:o')
            pin2.write(1)
            print ("-I am moving forward")
        
        if motion_command == "Go_Backward":
            pin3 = board.getpin('d:3:o')
            pin3.write(1)
            print ("-I am moving forward")
        
        if motion_command == "Turn_left":
            pin4 = board.getpin('d:4:o')
            pin4.write(1)
            print ("-I am Turning Let")
        
        if motion_command == "Turn_right":
            pin5 = board.getpin('d:5:o')
            pin5.write(1)
            print ("-I am Turning right")
        
        if motion_command == "Stop":
            pin6 = board.getpin('d:6:o')
            pin6.write(1)
            print ("-I stopped")
        else:
            print ("unknown command!!")
                
    rospy.spin()
    """
    while not rospy.is_shutdown():
        pubmotion.publish(motion_out)
    rate.sleep()
    rospy.spin()
    """
if __name__ == '__main__':
	print("Schrodingers Cat")
	try:
		robot_wheels()
	except rospy.ROSInterruptException():
		pass
