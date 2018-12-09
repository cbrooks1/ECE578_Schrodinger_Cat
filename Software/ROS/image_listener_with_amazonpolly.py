#! /usr/bin/python
# ros node to detect robot and speak using amazon polly
# rospy for the subscriber
import rospy
import imutils
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import numpy as np
import cv2
import os
import time
from std_msgs.msg import Float32
from collections import deque
import sys
import screeninfo
from std_msgs.msg import String
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist
msg=Twist()
import boto3
from pygame import mixer
"""
#initialize Global Variables
screen_id = 0
# get the size of the screen
screen = screeninfo.get_monitors()[screen_id]
width, height = screen.width, screen.height

# create image
image1 = cv2.imread('unamused.png', 1)
window_name = 'projector'
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

cv2.imshow(window_name, image1)
cv2.waitKey(0)
"""
mixer.init()

polly_client = boto3.Session(
        aws_access_key_id="AKIAIL3HNQSM7GQ5L6RA",                     
        aws_secret_access_key="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",
        region_name='us-west-2').client('polly')

# Instantiate CvBridge
bridge = CvBridge()
#pub=rospy.Publisher('coordinates',Float32,queue_size=1)
global rate


def image_callback(msg):
    print("Received an image!")
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
        bgr_image = imutils.resize(cv2_img, width = 300)
        # convert the images from bgr to hsv
        hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
        upper_green_range0 = np.array([25, 146, 190], dtype = "uint8")
        upper_green_range1 = np.array([62, 174, 250], dtype = "uint8")
        mask4 = cv2.inRange(hsv_image,  upper_green_range0 ,upper_green_range1)

        result = cv2.bitwise_and(bgr_image, bgr_image, mask = mask4)
        gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(blurred,25 , 255, cv2.THRESH_BINARY)[1]
        edged = cv2.Canny(thresh, 30, 200)

        # find contours
        (_ ,cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:4]
        screenCnt = None

        # loop over contours
        for c in (cnts):
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.04 * peri, True)
            
            if (4 <= len(approx) <7):
                screenCnt = approx
                x, y, h, w = cv2.boundingRect(screenCnt)
                print("Robot detected")
                if(x>180):
                    response = polly_client.synthesize_speech(TextType= 'ssml', VoiceId='Ivy',
                        OutputFormat='mp3', 
                        Text = '<speak> Robot detected on right</speak>')
                    file = open('right.mp3', 'w')
                    file.write(response['AudioStream'].read())
                    file.close()
                    mixer.music.load('right.mp3')
                    mixer.music.play()
                    rospy.sleep(2)
                    break
                    
                elif(x<100):
                    response = polly_client.synthesize_speech(TextType= 'ssml', VoiceId='Ivy',
                        OutputFormat='mp3', 
                        Text = '<speak> Robot detected on left</speak>')
                    file = open('left.mp3', 'w')
                    file.write(response['AudioStream'].read())
                    file.close()
                    mixer.music.load('left.mp3')
                    mixer.music.play()
                    rospy.sleep(2)
                    break
                
                else:
                    response = polly_client.synthesize_speech(TextType= 'ssml', VoiceId='Ivy',
                        OutputFormat='mp3', 
                        Text = '<speak> Robot detected on front</speak>')
                    file = open('front.mp3', 'w')
                    file.write(response['AudioStream'].read())
                    file.close()
                    mixer.music.load('front.mp3')
                    mixer.music.play()
                    rospy.sleep(2)
                    break
                break
    except CvBridgeError, e:
        pass
            
def main():
    rospy.init_node('image_listener')
    
    rate = rospy.Rate(20) # 10hz
    
    # Define your image topic
    image_topic = "/raspicam_node/image_raw"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic, Image, image_callback)
    # Spin until ctrl + c
   
    rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    main()
