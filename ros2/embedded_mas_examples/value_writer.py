import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class ValueWriter(Node):
    def __init__(self, max_messages=10, publish_period=1.0):
        super().__init__('value_writer')

        self.publisher = self.create_publisher(Int32, '/value1', 10)
        self.subscription = self.create_subscription(Int32, '/value1', self.listener_callback, 10)

        self.timer = self.create_timer(publish_period, self.publish_value)

        self.last_received_value = None
        self.counter = 0
        self.max_messages = max_messages

        self.get_logger().info(f'ValueWriter started: will publish {max_messages} messages every {publish_period}s')

    def listener_callback(self, msg):
        self.last_received_value = msg.data

    def publish_value(self):        
        if self.counter >= self.max_messages:
            self.get_logger().info('Finished publishing. Shutting down...')
            rclpy.shutdown()
    
        # Define novo valor com base no último valor recebido
        #if self.last_received_value is None:
        #    new_value = 0  # Valor inicial
        #else:
        #    new_value = self.last_received_value + 1
        
        new_value = self.last_received_value + 1

        # Publica
        msg = Int32()
        msg.data = new_value
        self.publisher.publish(msg)
        
        self.counter += 1

        #self.get_logger().info(f'Published: {new_value}')

        #self.counter += 1
        #if self.counter >= self.max_messages:
        #    self.get_logger().info('Finished publishing. Shutting down...')
        #    rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)

    node = ValueWriter(max_messages=6, publish_period=0.5)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

