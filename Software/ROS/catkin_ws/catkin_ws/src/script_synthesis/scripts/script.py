#!/usr/bin/env python


# Service Requests
# /phrase - String
#
# Service Response
# /status - int32

from speech_synthesis.srv import synthesis_service
import rospy
import boto3
from pygame import mixer


mixer.init()

def handle_speech_synthesis(req):

	mixer.music.load('line1.mp3')
	mixer.music.play()
	rospy.loginfo(str(req))

	mixer.music.load('line2.mp3')
	mixer.music.play()
	rospy.loginfo(str(req)

	mixer.music.load('line3.mp3')
	mixer.music.play()
	rospy.loginfo(str(req))
	return 1
	
def speech_synthesis_server():
	rospy.init_node('speech_synthesis_server')
	s = rospy.Service('speech_synthesis', synthesis_service, handle_speech_synthesis)
	print("Ready to synthesize.")	
	rospy.spin()

if __name__ == "__main__":
	speech_synthesis_server()
