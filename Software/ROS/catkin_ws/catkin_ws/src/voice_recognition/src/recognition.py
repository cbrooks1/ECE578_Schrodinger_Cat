#!/usr/bin/env python2

import os, sys
import rospy
import dialogflow
from speech_synthesis.srv import synthesis_service

def recognition(): 
    os.system("./record.py")
    response = dialogflow.dialogflow_main()
    if len(response) is 0:
        response = "a"
    rospy.loginfo(response)
    print(response)
    speech_synthesis = rospy.ServiceProxy('speech_synthesis', synthesis_service)
    return speech_synthesis(response)


if __name__ == '__main__':
    rospy.wait_for_service('speech_synthesis')
    while(True):
        recognition()
        raw_input("Press Enter to continue...")

