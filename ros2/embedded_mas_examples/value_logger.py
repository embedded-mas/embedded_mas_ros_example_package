import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32 
import csv
from datetime import datetime

class ValueLogger(Node):
    def __init__(self):
        super().__init__('value_logger')

        # Latest observed value (initially None)
        self.last_value = None

        # Topic name and type
        self.subscription = self.create_subscription(
            Int32,   
            'value1',
            self.listener_callback,
            10
        )

        # CSV file
        self.csv_file = open('value_log.csv', mode='a', newline='')
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow(['Time', 'Value'])  # Header

    def listener_callback(self, msg):
        novo_valor = msg.data
        if novo_valor != self.last_value:
            self.last_value = novo_valor
            timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')
            self.csv_writer.writerow([timestamp, novo_valor])
            #self.get_logger().info(f'Valor alterado: {novo_valor} registrado em {timestamp}')

    def destroy_node(self):
        self.csv_file.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = ValueLogger()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

