#!/usr/bin/env python2

import os, sys
import rospy
import dialogflow
from script_synthesis.srv import synthesis_service

def recognition(): 
    script_synthesis = rospy.ServiceProxy('script_synthesis', synthesis_service)
    return speech_synthesis(response)


if __name__ == '__main__':
    rospy.wait_for_service('speech_synthesis')
    while(True):
        recognition()
        raw_input("Press Enter to continue...")

