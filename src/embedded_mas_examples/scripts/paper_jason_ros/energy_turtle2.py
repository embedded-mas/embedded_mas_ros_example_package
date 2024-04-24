#!/usr/bin/env python

from __future__ import print_function

from std_srvs.srv import Empty, EmptyResponse  
from std_msgs.msg import Int32
import rospy
import random
import time


#energy = 100
energy_turtle2 = -1
time_to_wait_min = 1
time_to_wait_max = 5
energy_decrement_max = 5

def consume_energy(req):
    global energy
    global time_to_wait_min
    global time_to_wait_min
    global energy_decrement_max
    global energy_turtle2
    
    # Cria o tópico para publicar mensagens de tipo Int32
    publisher1 = rospy.Publisher('/turtle2/energy', Int32, queue_size=10)
    
    while True:
       if(energy_turtle2>0):
          energy1 = int(energy_turtle2 - random.uniform(1,energy_decrement_max))
          print("Current energy 1: ", energy1)
       
          publisher1.publish(energy1)
       
       time_to_wait = random.uniform(time_to_wait_min, time_to_wait_max)
       rospy.sleep(time_to_wait)        
    return EmptyResponse()  # Retornando uma resposta vazia


def consume_energy_server():
    rospy.init_node('turtlesim_extended_turtle2')
    s = rospy.Service('turtle2/consume_energy', Empty, consume_energy)
    rospy.spin()


def callback_turtle2(data):
    global energy_turtle2
    energy_turtle2 = data.data  # Armazena o valor Int32 em uma variável
    rospy.loginfo(f"Recebido: {energy_turtle2}")

if __name__ == "__main__":
  
     # Subscreve ao tópico para ler valores Int32
    rospy.Subscriber('/turtle2/energy', Int32, callback_turtle2)

    consume_energy_server()
