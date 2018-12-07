#!/usr/bin/env python


# Service Requests
# /phrase - String
#
# Service Response
# /status - int32

#from script_synthesis.srv import synthesis_service
import rospy
import boto3
from pygame import mixer
import os
from random import randint
from std_msgs.msg import Int32
from std_msgs.msg import String

global line_num

line_num = 1

#publinenumnber = rospy.Publisher('/line_num', Int32, queue_size=8)

mixer.init()

def line_number():
	global line_num

	if line_num == 1:
		mixer.music.load('line1.mp3')
		mixer.music.play()
		print("line 1")
		rospy.sleep(13)
	elif line_num == 2:
		mixer.music.load('line2.mp3')
		mixer.music.play()
		print("line 2")
		rospy.sleep(10)
	return 1
	
def speech_synthesis_server():
	rospy.init_node('speech_synthesis_server')
	
	#publish sensor values
	while not rospy.is_shutdown():	
		#publinenumnber.publish(line_num)
		#line_num = line_num + 1
		#line_number(line_num)

		mixer.music.load('line1.mp3')
		mixer.music.play()
		print("line 1")
		rospy.sleep(13)

		rospy.sleep(5)

		mixer.music.load('line2.mp3')
		mixer.music.play()
		print("line 2")
		rospy.sleep(10)

		rospy.sleep(5)

		mixer.music.load('line3.mp3')
		mixer.music.play()
		print("line 3")
		rospy.sleep(3)

		rospy.sleep(5)

		mixer.music.load('line4.mp3')
		mixer.music.play()
		print("line 4")
		rospy.sleep(9)

		rospy.sleep(5)

		mixer.music.load('line5.mp3')
		mixer.music.play()
		print("line 5")
		rospy.sleep(8)

		rospy.sleep(5)

		mixer.music.load('line6.mp3')
		mixer.music.play()
		print("line 6")
		rospy.sleep(8)

		rospy.sleep(5)

		print("line 7")
		rospy.sleep(10)

		rospy.sleep(5)

		mixer.music.load('line8.mp3')
		mixer.music.play()
		print("line 8")
		rospy.sleep(3)

		rospy.sleep(5)

		mixer.music.load('line9.mp3')
		mixer.music.play()
		print("line 9")
		rospy.sleep(2)

		rospy.sleep(5)

		mixer.music.load('line10.mp3')
		mixer.music.play()
		print("line 10")
		rospy.sleep(8)

		rospy.sleep(5)

		mixer.music.load('line11.mp3')
		mixer.music.play()
		print("line 11")
		rospy.sleep(4)

		rospy.sleep(5)

		mixer.music.load('line12.mp3')
		mixer.music.play()
		print("line 12")
		rospy.sleep(6)

		rospy.sleep(5)

		mixer.music.load('line13.mp3')
		mixer.music.play()
		print("line 13")
		rospy.sleep(2)

		rospy.sleep(5)

		mixer.music.load('line14.mp3')
		mixer.music.play()
		print("line 14")
		rospy.sleep(6)

		rospy.sleep(5)

		mixer.music.load('line15.mp3')
		mixer.music.play()
		print("line 15")
		rospy.sleep(3)

		rospy.sleep(5)

		mixer.music.load('line16.mp3')
		mixer.music.play()
		print("line 16")
		rospy.sleep(6)

		rospy.sleep(5)

		mixer.music.load('line17.mp3')
		mixer.music.play()
		print("line 17")
		rospy.sleep(1)

		rospy.sleep(5)

		mixer.music.load('line18.mp3')
		mixer.music.play()
		print("line 18")
		rospy.sleep(9)

		rospy.sleep(5)

		mixer.music.load('line19.mp3')
		mixer.music.play()
		print("line 19")
		rospy.sleep(2)

		rospy.sleep(5)

		mixer.music.load('line20.mp3')
		mixer.music.play()
		print("line 20")
		rospy.sleep(13)

		rospy.sleep(5)

		mixer.music.load('line21.mp3')
		mixer.music.play()
		print("line 21")
		rospy.sleep(4)

		rospy.sleep(5)

		mixer.music.load('line22.mp3')
		mixer.music.play()
		print("line 22")
		rospy.sleep(17)

		rospy.sleep(5)

		mixer.music.load('line23.mp3')
		mixer.music.play()
		print("line 23")
		rospy.sleep(1)

		rospy.sleep(5)

		mixer.music.load('line24.mp3')
		mixer.music.play()
		print("line 24")
		rospy.sleep(14)

		rospy.sleep(5)

		mixer.music.load('line25.mp3')
		mixer.music.play()
		print("line 25")
		rospy.sleep(5)

		rospy.sleep(5)

		mixer.music.load('line26.mp3')
		mixer.music.play()
		print("line 26")
		rospy.sleep(9)

		rospy.sleep(5)

		mixer.music.load('line27.mp3')
		mixer.music.play()
		print("line 27")
		rospy.sleep(6)

		rospy.sleep(5)

		mixer.music.load('line28.mp3')
		mixer.music.play()
		print("line 28")
		rospy.sleep(6)

		rospy.sleep(5)

		mixer.music.load('line29.mp3')
		mixer.music.play()
		print("line 29")
		rospy.sleep(8)

		rospy.sleep(5)

		mixer.music.load('line30.mp3')
		mixer.music.play()
		print("line 30")

		rospy.sleep(5)

		mixer.music.load('line31.mp3')
		mixer.music.play()
		print("line 31")
		rospy.sleep(7)

		rospy.sleep(5)

		mixer.music.load('line32.mp3')
		mixer.music.play()
		print("line 32")
		rospy.sleep(4)

		rospy.sleep(5)

		mixer.music.load('line33.mp3')
		mixer.music.play()
		print("line 33")
		rospy.sleep(6)

		rospy.sleep(5)

		mixer.music.load('line34.mp3')
		mixer.music.play()
		print("line 34")
		rospy.sleep(2)

		rospy.sleep(5)

		print("line 35")
		rospy.sleep(5)

		print("line 36")
		rospy.sleep(5)
		
	rate.sleep()	
	rospy.spin()

if __name__ == "__main__":
	speech_synthesis_server()
