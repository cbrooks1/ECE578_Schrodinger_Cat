# 
# Fall 2018 - ECE 478/578 - Robotics 1
**Intelligent Robotics Lab**
**Intelligent Robotics 1 Course Project**

**Portland State University**

# Project Name: ECE578_Schrodinger_Cat

Project Description
-Schrodinger Cat is one of the oldest robots in the lab. Schrodinger Cat is made up of a full body (head, arms, and legs controlled by servos) suspended above the ground by a base (which moves via a set of omni-wheels). The servos and motors are controlled via maestro controllers, controlled via and Arduino via a Raspberry Pi. We added a Raspberry Pi to the head of the robot to add vision, speech, and a screen to the robot.

# Project Status:
-For project 2, we moved the robot software to ROS, and implemented a better version of speech to text/text to speech, as well as performing a play with Einstein robot.

# Project Goals:
-Move robot software to a ROS system, and move over existing functionality
-Move text to speech capablities to a different system, implement speech to text
-Have robot perform play segment with another robot


# List of Hardware and Software (Tools, Libraries etc) :

Text to Speech
Dialogflow
Amazon Polly

Vision and Object Detection
https://thecodacus.com/opencv-object-tracking-colour-detection-python/
https://www.pyimagesearch.com/2018/06/25/raspberry-pi-face-recognition/
https://www.pyimagesearch.com/2016/02/15/determining-object-color-with-opencv/
https://gist.github.com/ronekko/dc3747211543165108b11073f929b85e
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html

Face Detection and Color Object Detection
https://docs.opencv.org/3.3.0/d7/d8b/tutorial_py_face_detection.html
https://www.superdatascience.com/opencv-face-detection/
https://www.blog.pythonlibrary.org/2018/08/15/face-detection-using-python-and-opencv/
https://www.geeksforgeeks.org/detection-specific-colorblue-using-opencv-python/
https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/

LCD Display/Face
https://gist.github.com/ronekko/dc3747211543165108b11073f929b85e
https://raspberrypi.stackexchange.com/questions/53931/why-is-my-raspberry-pi-3-display-not-filling-the-screen/54074

Servo Control
Details on the Pololu Mini Maestro: https://www.pololu.com/product/1356/resources 
Arduino Library for the Mini Maestro: https://github.com/pololu/maestro-arduino 

Board Hardware
Details on the Pololu Qiks - https://www.pololu.com/product/1110 
Arduino Library for the Pololu Qiks - https://github.com/pololu/qik-arduino 

# Other Notes:

Media Links
Videos of the robot can be found on the project GitHub page at:
https://github.com/cbrooks1/ECE578_Schrodinger_Cat/tree/master/Videos
THE NEW VIDEO OF THE ROBOT IS NAMED: RobotPlay_Clip

Code Reference
All of the code for this project can be found on the projects GitHub:
https://github.com/cbrooks1/ECE578_Schrodinger_Cat/tree/master


# Project Team :

Text to Speech / Speech to Text – Chelsea Brooks

Face  and Robot Detection ROS node - Rakhee Bhojakar

ROS System, 3D Printing/Screen Face - Erik Fox

ROS node for Wheels, Servos, Arduino Code -  Dakshayani Koppad

Servos, Arduino Code, Script Writing - Jamie Williams




