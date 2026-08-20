#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist
from embedded_mas_examples.srv import MoveRobot
from embedded_mas_examples.srv import MoveRobotResponse


class MoveRobotNode:

    def __init__(self):

        self.cmd_vel_pub = rospy.Publisher(
            '/cmd_vel',
            Twist,
            queue_size=10
        )

        self.service = rospy.Service(
            '/move_robot',
            MoveRobot,
            self.move_robot
        )

        rospy.loginfo('Service /move_robot ready')

    def move_robot(self, request):

        velocity = Twist()

        velocity.linear.x = request.linear_velocity
        velocity.angular.z = request.angular_velocity

        self.cmd_vel_pub.publish(velocity)

        rospy.loginfo(
            'Robot velocity set to: '
            'linear=%.2f m/s, angular=%.2f rad/s',
            request.linear_velocity,
            request.angular_velocity
        )

        return MoveRobotResponse(True)


if __name__ == '__main__':

    rospy.init_node('move_robot')

    MoveRobotNode()

    rospy.spin()
