# import the necessary packages

from pyimagesearch.facedetector import FaceDetector
from picamera.array import PiRGBArray
from picamera import PiCamera
import screeninfo
import numpy as np
import argparse
import imutils
import cv2
import os
import time


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


        #image[:10, :10] = 0  # black at top-left corner
        #image[height - 10:, :10] = [1, 0, 0]  # blue at bottom-left
        #image[:10, width - 10:] = [0, 1, 0]  # green at top-right
        #image[height - 10:, width - 10:] = [0, 0, 1]  # red at bottom-right

window_name = 'projector'
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
                          cv2.WINDOW_FULLSCREEN)
cv2.imshow(window_name, image4)

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required = True,
	help = "path to where the face cascade resides")
args = vars(ap.parse_args())

fd = FaceDetector(args["face"])

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
#camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.2)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    cv2.imshow(window_name, image5)

    # grab the raw NumPy array representing the image
    bgr_image = frame.array
    bgr_image = imutils.resize(bgr_image, width = 300)
    gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
    
    # find faces in the image
    faceRects = fd.detect(gray_image, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30))
    bgr_clone = bgr_image.copy()

    # loop over the faces and draw a rectangle around each
    for (x, y, w, h) in faceRects:
	cv2.rectangle(bgr_clone, (x, y), (x + w, y + h), (0, 255, 0), 2)

    #print("I found %d face(s)" % (len(faceRects)))
    if len(faceRects) > 0:
        if (x < 105):

            os.system("espeak -ven+f1 -g5  'Look Theres my human on the left side meow Hi human ' 2>/dev/null")
            os.system("espeak -ven+f1 -g5  'I should go straight or else he will catch me ' 2>/dev/null")
            cv2.imshow(window_name, image2)

        elif(x > 125):
            os.system("espeak -ven+f1 -s180 -g10 'Look Theres my human on the right side meow Hi human' 2>/dev/null")
            cv2.imshow(window_name, image3)

            
    cv2.imshow(window_name, image5)
 
    # convert the images from bgr to hsv
    hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 70, 50])
    higher_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 70, 50])
    higher_red2 = np.array([180, 255, 255])


    mask1 = cv2.inRange(hsv_image, lower_red1, higher_red1)
    mask2 = cv2.inRange(hsv_image, lower_red2, higher_red2)

   

    # create NumPy arrays
    lower_green_range0 = np.array([0, 100, 100], dtype = "uint8")
    lower_green_range1 = np.array( [10, 255, 255], dtype = "uint8")

    upper_green_range0 = np.array([45, 100, 100], dtype = "uint8")
    upper_green_range1 = np.array([75, 255, 255], dtype = "uint8")

    
    # find the colors within the specified boundaries and appy the mask
    mask3 = cv2.inRange(hsv_image,  lower_green_range0 ,lower_green_range1)
    mask4 = cv2.inRange(hsv_image,  upper_green_range0 ,upper_green_range1)

    mask = mask4 | mask2

    """
    red_hue_image = cv2.addWeighted(lower_red_hue_range, 1.0, upper_red_hue_range, 1.0, 0.0)
    red_hue_image = cv2.GaussianBlur(red_hue_image, (9,9), 0)
    """
    result = cv2.bitwise_and(bgr_image, bgr_image, mask = mask4)
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred,25 , 255, cv2.THRESH_BINARY)[1]
    
    edged = cv2.Canny(thresh, 30, 200)
    
    # find contours
    (_ ,cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:4]
    screenCnt = None
    """
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    """
    # loop over contours
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        print(len(approx))
        #cv2.drawContours(bgr_clone, [approx], -1, (0, 255, 0), 2)

        cv2.imshow(window_name, image5)

        if (4 <= len(approx) <7):
            screenCnt = approx
            x, y, h, w = cv2.boundingRect(screenCnt)
            cv2.rectangle(bgr_image, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.drawContours(bgr_image,[screenCnt],0,(0,0,255),-1)
            cv2.imshow(window_name, image7)
            os.system("espeak -ven+f1 -g5  'look there is a mouse.' 2>/dev/null")
            os.system("espeak -ven+f1 -g5  'oh my god mouse escaped.' 2>/dev/null")
            cv2.imshow(window_name, image1)


    #cv2.imshow("Detection", bgr_clone)
    #cv2.imshow("Color mask", result)
    """

    gray_result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    #print(gray_result)

    
    output = bgr_image.copy()

    # detect circles in the image
    circles = cv2.HoughCircles(edged, cv2.HOUGH_GRADIENT, 1, bgr_image.shape[0]/8, 30, 45)
    print(circles)
        
    # ensure atleast some circles were found
    if circles is not None:
        
        #print("red circle detected")
        os.system("espeak 'red circle detected' 2>/dev/null")

        # convert the (x,y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # loop over the (x,y) coordinates and radius of the circles
        for (x, y, r) in circles:
            #draw the circles in the output image
            cv2.circle(bgr_image, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(bgr_image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    """
    #cv2.imshow("Color mask", np.hstack([gray, blurred, thresh]))
    #cv2.imshow("Detection", bgr_image)

    """
    # show the frame
    #cv2.imshow("Frame", np.hstack([bgr_clone,box_detect]))
    #cv2.imshow("Input Frame", bgr_image)
    #cv2.imshow("Box Detected", box_detect)
    #cv2.imshow("Threshold_Lower_red  Threshold_Upper_red", np.hstack([result]))
    """
    key = cv2.waitKey(1) & 0xFF
    
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the 'q' key was pressed, break from the loop
    if key == ord('q'):
        break

cv2.destroyAllWindows()


