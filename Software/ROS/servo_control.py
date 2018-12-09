#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
from time import sleep
import sys
import serial

ser = serial.Serial("/dev/serial/by-id/usb-Arduino_Srl_Arduino_Uno_75330303035351715080-if00", baudrate=9600, timeout=3.0)


servo_command = "Neutral" # Default command
servo_cmd = "Neutral" # Default command
global servo_out
servo_commandList = ["Wave","Point","No","Neutral","Arms_up","Demo"]

# Here is the publisher for servo commands:
#pubservo = rospy.Publisher('servo_command', String, queue_size=1)

def callback_servo(data):
	global servo_command
    servo_command = data.data
	print('Callback -')
    run_command()
    #print(servo_command)	

def run_command():
    global servo_cmd, servo_command
    servo_cmd = servo_command
    print("Inside run command, running: " ,servo_cmd)
	
    if (servo_cmd == "Wave"):
        print("Wave start")
        ser.write('w'+'\n')
        #rospy.sleep(1)
        print ("-I am waving")
            
            
    elif (servo_cmd == "Point"):
        print("Point start")
        ser.write('p'+'\n')
        #rospy.sleep(1)
        print ("-I am pointing")
            
    elif (servo_cmd == "No"):
        print ("No start")
        ser.write('n'+'\n')
        #rospy.sleep(1)
        print ("-I am gesturing no")
            
    elif (servo_cmd == "Neutral"):
        print("Neutral start")
        ser.write('x'+'\n')
        #rospy.sleep(1)
        print ("-I am returning to neutral")
            
    elif (servo_cmd =="Arms_up"):
        print("Arms up start")
        ser.write('a'+'\n')
        #rospy.sleep(1)
        print ("-I am raising my arms")
            
    elif (servo_cmd =="Demo"):
        ser.write('m'+'\n')
        #rospy.sleep(1)
        print ("Demo mode is on")
    else:
        print ("Invalid command - no actions")
        
       
        rospy.spin()

def servo_control():
    global servo_cmd , servo_command
    rospy.init_node("servo_control", anonymous=True)
 #   rate = rospy.Rate(10) # 10Hz
    print('Running node: Servo control')
    rospy.Subscriber("/servo_control",String, callback_servo)

    rospy.spin()
    """
    while not rospy.is_shutdown():
        pubmotion.publish(servo_out)
    rate.sleep()
    rospy.spin()
    """


	
if __name__ == '__main__':
	print("Schrodingers Cat - Servo control - running")
	try:
		servo_control()
	except rospy.ROSInterruptException():
		pass
