#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import random
import math

# Inicializa o nó
rospy.init_node('random_cmd_vel_publisher')

# Publisher para o movimento
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(10)  # 10 Hz

# Variável global para armazenar a distância à frente
min_distance_ahead = float('inf')

# Callback para leitura do LiDAR
def scan_callback(scan_msg):
    global min_distance_ahead
    try:
        index_center = int((0.0 - scan_msg.angle_min) / scan_msg.angle_increment)
        distance = scan_msg.ranges[index_center]

        # Valida a distância
        if not math.isinf(distance) and not math.isnan(distance):
            min_distance_ahead = distance
        else:
            min_distance_ahead = float('inf')
    except:
        min_distance_ahead = float('inf')

# Assina o tópico do LiDAR
rospy.Subscriber('/scan', LaserScan, scan_callback)

# Aguarda mensagens do LiDAR antes de começar
rospy.sleep(1.0)

# Loop principal
msg = Twist()
for i in range(10000):
    if rospy.is_shutdown():
        break

    if min_distance_ahead < 0.2:
        # Obstáculo à frente → recuar
        msg.linear.x = -0.2
        msg.angular.z = 0.0
    else:
        # Movimento aleatório
        msg.linear.x = random.uniform(-0.5, 0.5)
        msg.angular.z = random.uniform(-1.0, 1.0)

    pub.publish(msg)
    rate.sleep()

