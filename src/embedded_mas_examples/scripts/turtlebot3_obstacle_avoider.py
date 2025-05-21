#!/usr/bin/env python3

#chmod +x rosrun your_package_name turtlebot3_obstacle_avoider.py && rosrun your_package_name turtlebot3_obstacle_avoider.py

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import math

class ObstacleAvoider:
    def __init__(self):
        rospy.init_node('obstacle_avoider', anonymous=True)

        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/scan', LaserScan, self.laser_callback)

        self.twist = Twist()
        self.obstacle_distance_threshold = 1.0  # obstáculo à frente
        self.side_distance_threshold = 0.2      # obstáculo nas laterais

        self.rate = rospy.Rate(10)
        
        self.max_writings = -1 #set this value to some x > 0 to finish the simulation after x writings
        self.writings = 0
        
    def laser_callback(self, msg):
        if self.max_writings>-1 and self.writings>=self.max_writings:
            rospy.loginfo("Finishing turtlesim simulation as it achieves " + str(self.writings) + " topic writings.")
            rospy.signal_shutdown("Stop condition reached")
     
        front = msg.ranges[0]
        right = msg.ranges[40]
        left = msg.ranges[300]

        # Corrige leituras inválidas
        front = front if math.isfinite(front) else 10.0
        right = right if math.isfinite(right) else 10.0
        left = left if math.isfinite(left) else 10.0

        # Caso obstáculo à frente
        if front < self.obstacle_distance_threshold:
            rospy.loginfo("Obstacle ahead!")
            self.twist.linear.x = -0.1
            self.twist.linear.y = 0.0
            self.twist.linear.z = 0.0
            self.twist.angular.x = 0.0
            self.twist.angular.y = 0.0
            self.twist.angular.z = 0.0
            self.cmd_vel_pub.publish(self.twist)
            self.writings+=1
            self.rate.sleep()
            if right > self.side_distance_threshold:
                rospy.loginfo("Turning right.")
                #self.twist.linear.x = 0.0
                #self.twist.angular.z = -0.8
                self.twist.linear.x = 0.0
                self.twist.linear.y = 0.0
                self.twist.linear.z = 0.0
                self.twist.angular.x = 0.0
                self.twist.angular.y = 0.0
                self.twist.angular.z = -0.2
            else:
                rospy.loginfo("Turning left.")
                #self.twist.linear.x = 0.0
                #self.twist.angular.z = 0.8
                self.twist.linear.x = 0.0
                self.twist.linear.y = 0.0
                self.twist.linear.z = 0.0
                self.twist.angular.x = 0.0
                self.twist.angular.y = 0.0
                self.twist.angular.z = 0.2

        # Caso obstáculo muito próximo nas laterais
        elif right < self.side_distance_threshold:
            rospy.loginfo("Too close on the right. Adjusting left.")
            #self.twist.linear.x = 0.1
            #self.twist.angular.z = 0.3  # vira levemente à esquerda
            self.twist.linear.x = 0.0
            self.twist.linear.y = 0.0
            self.twist.linear.z = 0.0
            self.twist.angular.x = 0.0
            self.twist.angular.y = 0.0
            self.twist.angular.z = 0.2

        elif left < self.side_distance_threshold:
            rospy.loginfo("Too close on the left. Adjusting right.")
            #self.twist.linear.x = 0.1
            #self.twist.angular.z = -0.3  # vira levemente à direita
            self.twist.linear.x = 0.0
            self.twist.linear.y = 0.0
            self.twist.linear.z = 0.0
            self.twist.angular.x = 0.0
            self.twist.angular.y = 0.0
            self.twist.angular.z = -0.2

        # Caminho livre
        else:
            self.twist.linear.x = 0.2
            self.twist.angular.z = 0.0

        self.cmd_vel_pub.publish(self.twist)
        self.writings+=1
           
    def run(self):
        while not rospy.is_shutdown():
            self.rate.sleep()

if __name__ == '__main__':
    try:
        ObstacleAvoider().run()
    except rospy.ROSInterruptException:
        pass

