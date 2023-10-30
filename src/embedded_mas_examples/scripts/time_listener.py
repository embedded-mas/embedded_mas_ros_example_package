#!/usr/bin/python3

import rospy
from std_msgs.msg import Int32
import time

previous_time = None
file_path = '/home/pedro/Git-ROSDevs/ros-devs/ros-devs/examples/Benchmark/Benchmark_logs/file.txt' #change to your actual file path

def topic_callback(data):
    global previous_time
    current_time = time.time() * 1000  # Convert time to milliseconds
    if previous_time is not None:
        time_diff = current_time - previous_time
        rospy.loginfo("Time difference: %.2f ms", time_diff)
        write_to_file(time_diff)
    previous_time = current_time

def write_to_file(time_diff):
    with open(file_path, 'a') as file:
        file.write(str(time_diff) + '\n')

def time_listener():
    rospy.init_node('time_listener_node', anonymous=True)
    rospy.Subscriber('value1', Int32, topic_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        time_listener()
    except rospy.ROSInterruptException:
        pass



