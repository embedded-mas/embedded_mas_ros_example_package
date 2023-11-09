import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32
import time

file_path = 'file.txt' #change to your actual file path

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.previous_time = None
        self.subscription = self.create_subscription(
            Int32,
            'value1',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
       #/self.get_logger().info('I heard: "%s"' % msg.data)
       current_time = time.time() * 1000  # Convert time to milliseconds
       if self.previous_time is not None:
          time_diff = current_time - self.previous_time
          self.get_logger().info("Time difference: %.2f ms"+ str(time_diff))
          self.write_to_file(time_diff)
       self.previous_time = current_time

    def write_to_file(self,time_diff):
       with open(file_path, 'a') as file:
          file.write(str(time_diff)+'\n')

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
