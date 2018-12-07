#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
from time import sleep
import sys

from gpiozero import pin12
from gpiozero import pin9
from gpiozero import pin8
from gpiozero import pin7
from gpiozero import pin6
from gpiozero import pin5

p12 = pin12(12)
p9 = pin9(9)
p8 = pin8(8)
p7 = pin7(7)
p6 = pin6(6)
p5 = pin5(5)

global motion_command
global pubMotion_Command
global motion_out
motion_commandList = ["Go_Forward","Go_Backward","Turn_Left","Turn_Right","Stop","Demo"]

#pubmotion = rospy.Publisher('motion_out',Int32, queue_size=1)

def callback0(data):
    motion_out = data.data


def robot_wheels():
    rospy.init_node("robot_wheels", anonymous=True)
    rate = rospy.Rate(10) # 10Hz
    rospy.Subscriber("motion_command", String, callback0)
    #rospy.Subscriber("motion_feedback", String, callback1)

    if motion_command in motion_commandList:
        if motion_command == "Go_Forward":
            p12.on()
            sleep(1)
            print ("-I am moving forward")
        
        if motion_command == "Go_Backward":
            p9.on()
            sleep(1)
            print ("-I am moving forward")
        
        if motion_command == "Turn_left":
            p8.on()
            sleep(1)
            print ("-I am Turning Let")
        
        if motion_command == "Turn_right":
            p7.on()
            sleep(1)
            print ("-I am Turning right")
        
        if motion_command == "Stop":
            p6.on()
            sleep(1)
            print ("-I stopped")
        
        if motion_command == "Demo":
            p5.on()
            sleep(1)
            print ("Demo mode is on")
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
