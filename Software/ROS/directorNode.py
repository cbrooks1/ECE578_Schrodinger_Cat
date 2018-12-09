#!/usr/bin/env python
#Schrodinger's Cat Robot: Main Node
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String

#initialize Global Variables
wheel='Stop'
servo='Neutral'

#Publisher Nodes
#"Go_Forward","Go_Backward","Turn_Left","Turn_Right","Stop"
def mcommand_talker():
	global wheel
	print('in talker')
	#set up node as publisher
	pub=rospy.Publisher('/motion_command',String,queue_size=10)
	#publish next command
	rate=rospy.Rate(5)
	pub.publish(wheel)
	print('published')
	rate.sleep()



##Main: Play Director fuction: controls the actions of our robot in correct 
def director():
	global wheel
        x=0
        rospy.init_node('director', anonymous=True)
        wheel="Go_Forward"
	mcommand_talker()
	while x!=1000:
            x=x+1
            mcommand_talker()
        wheel="Stop"
        mcommand_talker()
        wheel="Stop"
        mcommand_talker()
        wheel="Turn_Left"
        mcommand_talker()
	rospy.spin()
	
if __name__=='__main__':
	try:
		director()
	except rospy.ROSInterruptException:
		pass
