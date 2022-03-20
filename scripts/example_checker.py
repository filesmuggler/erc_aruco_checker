#!/usr/bin/env python3

import rospy
import yaml
import numpy as np

from erc_aruco_msg.srv import ErcArucoRequest, ErcArucoResponse, ErcAruco

class ExampleArUcoChecker:
    def __init__(self):
        rospy.init_node("erc_aruco_checker_example",anonymous=True)
        self.check_service = rospy.Service('erc_aruco_score',ErcAruco,self.handle_score)
        rospy.loginfo("Ready to score")
        rospy.spin()

    def handle_score(self,req):
        #TODO: calculate score wrt to gt
        return 10.0

if __name__ == '__main__':
    try:
        c = ExampleArUcoChecker()
    except KeyboardInterrupt:
        print("end")