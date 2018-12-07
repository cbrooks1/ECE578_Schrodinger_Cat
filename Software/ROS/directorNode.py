#!/usr/bin/env python
#Schrodinger's Cat Robot: Main Node
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Float32
from std_msgs.msg import String

#initialize Global Variables
face_command=
image_command=
motion_command=
mfeedback_command=

#Callback funtions
def callback1(data):
def callback2(data):


#Publisher Nodes
def face_talker():
	global face_command
	#set up node as publisher
	pub=rospy.Publisher('face',Int32,queue_size=10)

	
	#publish next command
	rate=rospy.Rate(.2)
	pub.publish(face_command)
	rate.sleep()
	
def image_talker():
	global image_command
	#set up node as publisher
	pub=rospy.Publisher('image_topic',Image??,queue_size=10)

	
	#publish next command
	rate=rospy.Rate(.2)
	pub.publish(image_command)
	rate.sleep()

def mcommand_talker():
	global motion_command
	#set up node as publisher
	pub=rospy.Publisher('motion_command',String,queue_size=10)

	
	#publish next command
	rate=rospy.Rate(.2)
	pub.publish(motion_command)
	rate.sleep()

def mfeedback_talker():
	global mfeedback_command
	#set up node as publisher
	pub=rospy.Publisher('motion_feedback',String,queue_size=10)

	
	#publish next command
	rate=rospy.Rate(.2)
	pub.publish(mfeedback_command)
	rate.sleep()

	
#suscriber nodes: Do we need this? Can we just use a director function and publish what we want to happen
def listener():
	#Set up node
	rospy.init_node('director', anonymous=True)
	
	#suscribe node to the sensor's topics
	rospy.Subscriber('coordinates',Float32, callback1) 
	rospy.Subscriber('/turtle1/cmd_vel',Twist??, callback2)
	rospy.spin()

#Main: Play Director fuction: controls the actions of our robot in correct 
def director():
	
if __name__=='__main__':
	try:
		listener()
	except rospy.ROSInterruptException:
		pass
