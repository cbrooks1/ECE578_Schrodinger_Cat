#!/usr/bin/env python
#Schrodinger's Cat Robot: Main Node
import rospy

from std_msgs.msg import String

#initialize Global Variables
wheel='Stop'
servo='Neutral'

#Publisher Nodes
#"Go_Forward","Go_Backward","Turn_Left","Turn_Right","Stop"
def mcommand_talker():
	global wheel
	#set up node as publisher
	pub=rospy.Publisher('motion_command',String,queue_size=10)

	
	#publish next command
	rate=rospy.Rate(.2)
	pub.publish(wheel)
	rate.sleep()

#"Wave","Point","No","Neutral","Arms_up"
def scommand_talker():
	global servo
	#set up node as publisher
	pub=rospy.Publisher('servo_command',String,queue_size=10)

	
	#publish next command
	rate=rospy.Rate(.2)
	pub.publish(servo)
	rate.sleep()

#Main: Play Director fuction: controls the actions of our robot in correct 
def director():
	global wheel, servo
	rospy.init_node('director', anonymous=True)
	rospy.sleep(10)
	servo='Wave'
	wheel='Go_Forward'
	mcommand_talker()
	mcommand_talker()
	print('goforward')
	rospy.sleep(1)
	wheel='Stop'
	mcommand_talker()
	scommand_talker()
	rospy.sleep(2)
	servo='Neutral'
	scommand_talker()
	rospy.sleep(10)
	servo='Point'
	wheel='Go_Back'
	print('Go back')
	mcommand_talker()
	rospy.sleep(1)
	wheel='Stop'
	mcommand_talker()
	scommand_talker()
	rospy.sleep(5)
	servo='Neutral'
	scommand_talker()
	rospy.sleep(30)
	wheel='Turn_Right'
	print('turn right')
	mcommand_talker()
	rospy.sleep(7)
	wheel='Turn_Left'
	mcommand_talker()
	rospy.sleep(7)
	wheel='Stop'
	mcommand_talker()
	rospy.sleep(37)
	rospy.spin()
	
if __name__=='__main__':
	try:
		director()
	except rospy.ROSInterruptException:
		pass
