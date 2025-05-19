#!/usr/bin/env python3

#chmod +x rosrun your_package_name turtlebot3_obstacle_avoider.py && rosrun your_package_name turtlebot3_obstacle_avoider.py

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class ObstacleAvoider:
    def __init__(self):
        rospy.init_node('obstacle_avoider', anonymous=True)

        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/scan', LaserScan, self.laser_callback)

        self.twist = Twist()
        self.obstacle_distance_threshold = 0.5  # metros

        self.rate = rospy.Rate(10)  # 10 Hz

    def laser_callback(self, msg):
        # A faixa de leitura depende do modelo (180 ou 360 graus). Para TurtleBot3 é 360.
        front = min(min(msg.ranges[0:10] + msg.ranges[-10:]), 10.0)  # frente central
        right = min(min(msg.ranges[270:310]), 10.0)  # lado direito
        left = min(min(msg.ranges[50:90]), 10.0)     # lado esquerdo

        if front < self.obstacle_distance_threshold:
            rospy.loginfo("Obstacle detected! Turning right.")
            # recuar levemente e virar para a direita
            self.twist.linear.x = -0.1
            self.twist.angular.z = -0.8
        else:
            # movimento normal para frente
            self.twist.linear.x = 0.2
            self.twist.angular.z = 0.0

        self.cmd_vel_pub.publish(self.twist)

    def run(self):
        while not rospy.is_shutdown():
            self.rate.sleep()

if __name__ == '__main__':
    try:
        node = ObstacleAvoider()
        node.run()
    except rospy.ROSInterruptException:
        pass

