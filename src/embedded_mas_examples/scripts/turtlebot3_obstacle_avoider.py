#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class ObstacleAvoider:
    def __init__(self):
        rospy.init_node('obstacle_avoider', anonymous=True)

        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/scan', LaserScan, self.laser_callback)

        self.obstacle_detected = False
        self.turning_right = False
        self.backing_up = False
        self.backing_up_steps = 0

        self.rate = rospy.Rate(10)
        self.msg = Twist()

    def laser_callback(self, scan):
        front_index = len(scan.ranges) // 2
        right_index = len(scan.ranges) // 4

        front_range = scan.ranges[front_index]
        right_range = scan.ranges[right_index]

        if front_range < 0.4:
            self.obstacle_detected = True
            if front_range < 0.2:
                self.backing_up = True
                self.backing_up_steps = 5
            else:
                self.turning_right = True
        else:
            self.obstacle_detected = False
            self.turning_right = False
            self.backing_up = False

    def move(self):
        while not rospy.is_shutdown():
            if self.backing_up and self.backing_up_steps > 0:
                self.msg.linear.x = -0.1
                self.msg.angular.z = 0.0
                self.backing_up_steps -= 1
            elif self.turning_right:
                self.msg.linear.x = 0.0
                self.msg.angular.z = -0.5
            else:
                self.msg.linear.x = 0.2
                self.msg.angular.z = 0.0

            self.cmd_pub.publish(self.msg)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        controller = ObstacleAvoider()
        controller.move()
    except rospy.ROSInterruptException:
        pass

