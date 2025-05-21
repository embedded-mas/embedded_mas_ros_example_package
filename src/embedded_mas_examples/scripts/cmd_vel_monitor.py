#!/usr/bin/env python3

'''
This program logs timestamp and the incremental counter of every writing in the topic /cmd_vel.
It is useful to evaluate the performance of programs that write in this topic.

'''

import rospy
from geometry_msgs.msg import Twist
from datetime import datetime

class CmdVelLogger:
    def __init__(self):
        self.counter = 0
        self.log_file = open("cmd_vel_log.txt", "a")  
        self.log_file.write("id;time;linear.x;linear.y;linear.z;angular.x;angular.y;angular.z")
        self.log_file.flush()

        rospy.Subscriber("/cmd_vel", Twist, self.callback)
        rospy.loginfo("Monitorando /cmd_vel...")

    def callback(self, msg):
        self.counter += 1
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        log_entry = (
            f"{self.counter};{now};{msg.linear.x:.2f},{msg.linear.y:.2f},{msg.linear.z:.2f};"
            f"{msg.angular.x:.2f},{msg.angular.y:.2f},{msg.angular.z:.2f}\n"
        )
        self.log_file.write(log_entry)
        self.log_file.flush()  # garante que o log seja gravado imediatamente

    def run(self):
        rospy.spin()
        self.log_file.close()

if __name__ == "__main__":
    rospy.init_node("cmd_vel_logger")
    logger = CmdVelLogger()
    logger.run()

