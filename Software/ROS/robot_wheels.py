#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
from time import sleep
import sys
import serial

ser = serial.Serial("/dev/serial/by-id/usb-Arduino_Srl_Arduino_Uno_75330303035351715080-if00", baudrate=9600, timeout=3.0)


motion_cmd='Stop'
#motion_cmd = "Go_Forward"
motion= "Stop"
#motion_commandList = ["Go_Forward","Go_Backward","Turn_Left","Turn_Right","Stop","Demo"]
Flag=0
#pubmotion = rospy.Publisher('motion_out',Int32, queue_size=1)

def callback0(data):
    global motion
    motion = data.data
    print('callback')
    navigation()
    #print(motion)

def navigation():
    global motion_cmd, motion
    motion_cmd = motion
    print("insde navigation" ,motion_cmd)
    if (motion_cmd == "Go_Forward"):
        print("FFFF")
        ser.write('f'+'\n')
        #rospy.sleep(1)
        print ("-I am moving forward")
            
            
    elif (motion_cmd == "Go_Backward"):

        print("BBBB")
        ser.write('b'+'\n')
        #rospy.sleep(1)
        print ("-I am moving backward")
            
    elif (motion_cmd == "Turn_Right"):
        print ("RRR")
        ser.write('r'+'\n')
        #rospy.sleep(1)
        print ("-I am Turning Right")
            
    elif (motion_cmd == "Turn_Left"):
        print("LLLL")
        ser.write('l'+'\n')
        #rospy.sleep(1)
        print ("-I am Turning left")
            
    elif (motion_cmd =="Stop"):
        print("SSSS")
        ser.write('s'+'\n')
        #rospy.sleep(1)
        print ("-I stopped")
            
    elif (motion_cmd =="Demo"):
        ser.write('d'+'\n')
        #rospy.sleep(1)
        print ("Demo mode is on")
    else:
        print ("unknown command!!")
        
       
        rospy.spin()
    
def robot_wheels():
    global motion_cmd , motion
    rospy.init_node("robot_wheels", anonymous=True)
 #   rate = rospy.Rate(10) # 10Hz
    print('robot wheels')
    rospy.Subscriber("/motion_command",String, callback0)
    #rospy.Subscriber("motion_feedback", String, callback1)

    rospy.spin()
    """
    while not rospy.is_shutdown():
        pubmotion.publish(motion_out)
    rate.sleep()
    rospy.spin()
    """
if __name__ == '__main__':
	print("Schrodingers Cat")
	try:
            
                robot_wheels()
		
	except rospy.ROSInterruptException():
		pass
