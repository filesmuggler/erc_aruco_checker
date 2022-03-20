#!/usr/bin/env python3

import rospy
import math
import tf
import time
import geometry_msgs.msg
from tf.transformations import euler_from_quaternion, quaternion_from_euler

from erc_aruco_msg.srv import ErcArucoRequest, ErcArucoResponse, ErcAruco

class TagListener:
    def __init__(self):
        rospy.init_node("erc_aruco_example_2", anonymous=True)
        rospy.loginfo("Ready to call")
        self.call_aruco_checker()

    def call_aruco_checker(self):
        rospy.wait_for_service("erc_aruco_score")

        try:
            service_proxy = rospy.ServiceProxy('erc_aruco_score',ErcAruco)
            service_msg = ErcArucoRequest()
            listener = tf.TransformListener()

            rate = rospy.Rate(1.0)
            timeout = 1

            for tag_no in range(15):
                print(f'Looking for tag {tag_no}')
                timeout_start = time.time()
                while time.time() < timeout_start + timeout:
                    try:
                        tag_name = f'/fiducial_{tag_no}'
                        (trans, _) = listener.lookupTransform(tag_name, '/base', rospy.Time())
                        exec("service_msg.tag" + str(tag_no) + "= trans")

                    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                        exec("service_msg.tag" + str(tag_no) + "= [0,0,0]")
                        continue
                    rate.sleep()

            service_response = service_proxy(service_msg)
            print(f"You received score {service_response.score}")
        except rospy.ServiceException as e:
            print(f"Service call failed: {e}")

if __name__ == "__main__":
    try:
        ex2 = TagListener()
    except KeyboardInterrupt:
        print("end")

