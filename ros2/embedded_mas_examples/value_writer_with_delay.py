import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_srvs.srv import Trigger


class ValueWriterService(Node):
    def __init__(self):
        super().__init__('value_writer_service')

        # Publisher no tópico /value1
        self.publisher = self.create_publisher(Int32, '/value1', 10)

        # Serviço do tipo Trigger
        self.srv = self.create_service(Trigger, 'write_value', self.handle_write_value)

        # Último valor publicado
        self.last_value = 0

        self.get_logger().info('ValueWriterService is ready. Call service "write_value".')

    def handle_write_value(self, request, response):
        """Callback do serviço."""

        # Incrementa valor
        self.last_value += 1
        msg = Int32()
        msg.data = self.last_value

        # Publica no tópico
        self.publisher.publish(msg)
        self.get_logger().info(f'Published: {self.last_value}')

        # Delay de 5 segundos ANTES de retornar resposta
        time.sleep(5)

        # Prepara resposta
        response.success = True
        response.message = f'Value {self.last_value} published (with 5s delay)'
        return response


def main(args=None):
    rclpy.init(args=args)
    node = ValueWriterService()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

