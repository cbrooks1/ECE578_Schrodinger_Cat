#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from time import sleep
import sys


# This code calls the demo functions for both the wheels and the servos
# It only publishes, but does not subscribe

def servo_control():
    rospy.init_node("motion_demo", anonymous=True)
    rate = rospy.Rate(10) # 10Hz

	if not rospy.is_shutdown():
		pubservo = rospy.Publisher('servo_command', String, queue_size=1)
		pubwheels = rospy.Publisher('robot_wheels', String, queue_size=1)
		
		rospy.loginfo("Starting - Wheel demo")
		pubwheels.publish("Demo")
		sleep(60);
		
		rospy.loginfo("Starting - Servo demo")
		pubservo.publish("Demo")
		sleep(120);
		
		rospy.loginfo("Done with motion demo")

	
if __name__ == '__main__':
	print("Schrodingers Cat - Motion demo")
	try:
		servo_control()
	except rospy.ROSInterruptException():
		pass
