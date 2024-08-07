#!/usr/bin/env python3

import random
import time
import subprocess
from std_srvs.srv import Empty
from std_msgs.msg import Int32
import rclpy
from rclpy.node import Node

# Variáveis globais
energy_turtle1 = -1
energy_turtle2 = -1
time_to_wait_min = 1
time_to_wait_max = 5
energy_decrement_max = 5
alarm = 0

pen_turtle1 = [255, 255, 255, 12, 0]
pen_turtle2 = [255, 255, 255, 12, 0]

class TurtleSimNode(Node):
    def __init__(self):
        super().__init__('turtlesim_extended_turtle1')
        self.publisher1 = self.create_publisher(Int32, '/turtle1/energy', 10)
        self.publisher2 = self.create_publisher(Int32, '/turtle2/energy', 10)
        self.create_subscription(Int32, '/turtle1/energy', self.callback_turtle1, 10)
        self.create_subscription(Int32, '/turtle2/energy', self.callback_turtle2, 10)
        self.service = self.create_service(Empty, 'turtle1/consume_energy', self.consume_energy)
        
        # Inicialização do timer
        self.timer = self.create_timer(1.0, self.timer_callback)
        
        self.energy_turtle1 = -1
        self.energy_turtle2 = -1

    def callback_turtle1(self, msg):
        self.energy_turtle1 = msg.data
        self.get_logger().info(f'Recebido energy turtle 1: {self.energy_turtle1}')

    def callback_turtle2(self, msg):
        self.energy_turtle2 = msg.data
        self.get_logger().info(f'Recebido energy turtle 2: {self.energy_turtle2}')

    def consume_energy(self, request, response):
        self.get_logger().info('Iniciando consumo de energia...')
        return Empty.Response()

    def timer_callback(self):
        global alarm
        global pen_turtle1
        global pen_turtle2
        
        if self.energy_turtle1 > 0:
            self.get_logger().info("**** Energy: ", str(self.energy_turtle1) )
            self.energy_turtle1 -= random.uniform(1, energy_decrement_max)
            self.publisher1.publish(Int32(data=int(self.energy_turtle1)))
            if self.energy_turtle1 >= 65:
                pen_turtle1[2] = int((self.energy_turtle1 - 35) * 255 / 65)
            command = f'ros2 service call /turtle1/set_pen turtlesim/srv/SetPen "{pen_turtle1[0]} {pen_turtle1[1]} {pen_turtle1[2]} {pen_turtle1[3]} 0"'
            subprocess.Popen(command, shell=True)

        if self.energy_turtle2 > 0:
            self.energy_turtle2 -= random.uniform(1, energy_decrement_max)
            self.publisher2.publish(Int32(data=int(self.energy_turtle2)))
            if self.energy_turtle2 >= 65:
                pen_turtle2[2] = int((self.energy_turtle2 - 65) * 255 / 35)
            command = f'ros2 service call /turtle2/set_pen turtlesim/srv/SetPen "{pen_turtle2[0]} {pen_turtle2[1]} {pen_turtle2[2]} {pen_turtle2[3]} 0"'
            subprocess.Popen(command, shell=True)

        if alarm == 0:
            move_to_critical = random.uniform(0, 100)
            if move_to_critical <= 4:
                alarm = 1
                command = f'ros2 topic pub /turtle1/alarm std_msgs/msg/String "data: critical"'
                subprocess.Popen(command, shell=True)
            elif move_to_critical <= 9:
                alarm = 2
                command = f'ros2 topic pub /turtle2/alarm std_msgs/msg/String "data: critical"'
                subprocess.Popen(command, shell=True)
            if alarm > 0:
                self.get_logger().info("**** Critical alarm level *****")
                command = f'ros2 param set /turtlesim background_r 255 && ros2 param set /turtlesim background_g 0 && ros2 param set /turtlesim background_b 0 && ros2 service call /clear std_srvs/srv/Empty'
                subprocess.Popen(command, shell=True)
        else:
            move_to_safe = random.uniform(0, 100)
            if move_to_safe <= 20:
                alarm = 0
                command = f'ros2 param set /turtlesim background_r 69 && ros2 param set /turtlesim background_g 86 && ros2 param set /turtlesim background_b 255 && ros2 service call /clear std_srvs/srv/Empty && ros2 topic pub /turtle1/alarm std_msgs/msg/String "data: safe" && ros2 topic pub /turtle2/alarm std_msgs/msg/String "data: safe"'
                subprocess.Popen(command, shell=True)
                self.get_logger().info("**** Safe alarm level *****")

def main(args=None):
    rclpy.init(args=args)
    node = TurtleSimNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

