#!/usr/bin/env python

import math

import rospy
from nav_msgs.msg import Odometry

from embedded_mas_examples.srv import GetRobotPose, GetRobotPoseResponse


class GetRobotPoseNode:

    def __init__(self):

        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

        rospy.Subscriber(
            '/odom',
            Odometry,
            self.odom_callback
        )

        rospy.Service(
            '/get_robot_pose',
            GetRobotPose,
            self.get_robot_pose
        )

        rospy.loginfo(
            'Service /get_robot_pose ready'
        )

    def odom_callback(self, msg):

        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y

        q = msg.pose.pose.orientation

        sin_yaw = 2.0 * (q.w * q.z + q.x * q.y)
        cos_yaw = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)

        self.theta = math.atan2(sin_yaw, cos_yaw)

    def get_robot_pose(self, request):

        rospy.loginfo(
            'Pose requested: x=%.3f, y=%.3f, theta=%.3f',
            self.x,
            self.y,
            self.theta
        )

        return GetRobotPoseResponse(
            self.x,
            self.y,
            self.theta
        )


if __name__ == '__main__':

    rospy.init_node('get_robot_pose')

    GetRobotPoseNode()

    rospy.spin()
