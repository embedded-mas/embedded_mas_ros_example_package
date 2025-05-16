import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class ValueWriter(Node):
    def __init__(self, max_messages=10, publish_period=1.0):
        super().__init__('value_writer')

        self.publisher = self.create_publisher(Int32, '/value1', 10)
        self.timer = self.create_timer(publish_period, self.publish_value)

        self.last_value = None  # Inicia sem valor
        self.counter = 0
        self.max_messages = max_messages

        self.get_logger().info(f'ValueWriter started: will publish {max_messages} messages every {publish_period}s')

    def publish_value(self):
        # Define próximo valor com base no anterior
        if self.last_value is None:
            new_value = 0
        elif self.last_value == 0:
            new_value = 1
        else:
            new_value = 0

        # Publica
        msg = Int32()
        msg.data = new_value
        self.publisher.publish(msg)

        #self.get_logger().info(f'Published: {new_value}')

        # Atualiza estado
        self.last_value = new_value
        self.counter += 1

        # Encerra se atingiu o limite
        if self.counter >= self.max_messages:
            self.get_logger().info('Finished publishing. Shutting down...')
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)

    # Exemplo: publica 6 vezes, a cada 0.5s
    node = ValueWriter(max_messages=6, publish_period=0.5)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

