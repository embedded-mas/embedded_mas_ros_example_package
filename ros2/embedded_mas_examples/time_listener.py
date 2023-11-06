#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import time


class TimeListener(Node):
  
   def __init__(self):
      super().__init__('time_listener')
      self.publisher_ = self.create_publisher(Int32,'value1',10)
      timer_period = 0.1 #seconds
      self.timer = self.create_timer(timer_period, self.topic_callback)
      self.i = 0 
      self.previous_time = None
   
   def topic_callback(self):
     current_time = time.time() * 1000  # Convert time to milliseconds
     if self.previous_time is not None:
        time_diff = current_time - self.previous_time
        self.write_to_file(time_diff)
     self.previous_time = current_time

   def write_to_file(self,time_diff):
      with open('file.txt', 'a') as file:
         file.write(str(time_diff) + '\n')

def time_listener(args=None):
   rclpy.init(args=args)
   rclpy.spin(TimeListener())

if __name__ == '__main__':
    try:
        time_listener()
    except rospy.ROSInterruptException:
        pass



