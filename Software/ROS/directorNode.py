#!/usr/bin/env python
#Schrodinger's Cat Robot: Main Node
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Float32
from std_msgs.msg import String

#initialize Global Variables
motion_command='Stop'

#Publisher Nodes
def mcommand_talker():
	global motion_command
	#set up node as publisher
	pub=rospy.Publisher('motion_command',String,queue_size=10)

	
	#publish next command
	rate=rospy.Rate(.2)
	pub.publish(motion_command)
	rate.sleep()

def ():
	global motion_command
	#set up node as publisher
	pub=rospy.Publisher('',String,queue_size=10)

	
	#publish next command
	rate=rospy.Rate(.2)
	pub.publish()
	rate.sleep()

#Main: Play Director fuction: controls the actions of our robot in correct 
def director():
	rospy.init_node('director', anonymous=True)
	

	
if __name__=='__main__':
	try:
		director()
	except rospy.ROSInterruptException:
		pass
