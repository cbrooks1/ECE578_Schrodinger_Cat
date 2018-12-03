#! /usr/bin/python


# Using this CvBridge Tutorial for converting
# ROS images to OpenCV2 images
# http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython

# Using this OpenCV2 tutorial for saving Images:
# http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html

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
import time

# Instantiate CvBridge
bridge = CvBridge()
pub=rospy.Publisher('coordinates',Float32,queue_size=1)
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
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.04 * peri, True)
            print(len(approx))

            if (4 <= len(approx) <7):
                screenCnt = approx
                x, y, h, w = cv2.boundingRect(screenCnt)
                pub.publish(int(x))
                rospy.loginfo(int(x))
                
                print("Robot detected")
    except CvBridgeError, e:
        print(e)
    else:
        # Save your OpenCV2 image as a jpeg 
        cv2.imwrite('camera_image.jpeg', cv2_img)
        
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
   
    print("Hi Rakhee")
    main()
