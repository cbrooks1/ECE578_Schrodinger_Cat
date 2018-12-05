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

polly_client = boto3.Session(
	aws_access_key_id="AKIAJ5URJV74OG537KAQ",                     
	aws_secret_access_key="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",
	region_name='us-west-2').client('polly')

mixer.init()

def handle_speech_synthesis(req):
	response = polly_client.synthesize_speech(VoiceId='Ivy',
				OutputFormat='mp3', 
				Text = str(req))
	file = open('speech.mp3', 'w')
	file.write(response['AudioStream'].read())
	file.close()
	mixer.music.load('speech.mp3')
	mixer.music.play()
	return 1
	
def speech_synthesis_server():
	rospy.init_node('speech_synthesis_server')
	s = rospy.Service('speech_synthesis', synthesis_service, handle_speech_synthesis)
	print("Ready to synthesize.")	
	rospy.spin()

if __name__ == "__main__":
	speech_synthesis_server()
