#!/usr/bin/env python
#Schrodinger's Cat Robot: Face Node
import rospy
import screeninfo
import numpy as np
import cv2
from std_msgs.msg import Int32
from std_msgs.msg import String

#initialize Global Variables
screen_id = 0
is_color = True

# get the size of the screen
screen = screeninfo.get_monitors()[screen_id]
width, height = screen.width, screen.height

# create image
if is_color:
	image1 = cv2.imread('unamused.png', 1)
	image2 = cv2.imread('lookleft.png', 1)
	image3 = cv2.imread('lookright.png', 1)
	image4 = cv2.imread('sleeping.png', 1)
	image5 = cv2.imread('happy_open.png', 1)
	image6 = cv2.imread('happy_closed.png', 1)
	image7 = cv2.imread('angry_open.png', 1)
	image8 = cv2.imread('angry_closed.png', 1)
window_name = 'projector'
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

#Callback funtions to take data that node is subscribed to and assign it to global variables
def callback1(data):
	global image1, image2, image3, image4, image5, image6, image7, image8
	if data.data==1:
		cv2.imshow(window_name, image1)
	elif data.data<130:
		cv2.imshow(window_name, image2)
	elif data.data>130:
		cv2.imshow(window_name, image3)
	elif data.data==4:
		cv2.imshow(window_name, image4)
	elif data.data==5:
		cv2.imshow(window_name, image5)
	elif data.data==6:
		cv2.imshow(window_name, image6)
	elif data.data==7:
		cv2.imshow(window_name, image7)
	elif data.data==8:
		cv2.imshow(window_name, image8)
	else:
		cv2.imshow(window_name, image6)
	

def listener():
	#Set up node
	rospy.init_node('face_listener', anonymous=True)
	
	#suscribe node to the sensor's topics
	rospy.Subscriber('coordinates', Int32,callback1) 
	rospy.spin()
if __name__=='__main__':
	try:
		listener()
	except rospy.ROSInterruptException:
		pass
