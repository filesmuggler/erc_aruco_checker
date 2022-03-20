#!/usr/bin/env python3

import rospy
import yaml
import numpy as np

from erc_aruco_msg.srv import ErcArucoRequest, ErcArucoResponse, ErcAruco

class ArUcoChecker:
    def __init__(self,aruco_config: dict):
        self.gt_config = aruco_config
        rospy.init_node("erc_aruco_checker",anonymous=True)
        self.check_service = rospy.Service('erc_aruco_score',ErcAruco,self.handle_score)
        rospy.loginfo("Ready to score")
        rospy.spin()

    def handle_score(self,req):
        #TODO: calculate score wrt to gt
        a = np.array(req.tag0)
        b = np.array(self.gt_config['tag0'])
        dist = np.linalg.norm(a - b)
        return 10.0

if __name__ == '__main__':
    config_file = "/home/krzysztof/Projects/erc_aruco_ws/src/erc_aruco_checker/config/config.yaml"
    try:
        with open(config_file,'r') as file_yaml:
            config = yaml.safe_load(file_yaml)

        c = ArUcoChecker(aruco_config=config)
    except KeyboardInterrupt:
        print("end")