#!/usr/bin/env python

# rosparam set /turtlesim/background_r 200
# rosservice call /clear

from __future__ import print_function

from std_srvs.srv import Empty, EmptyResponse  
from std_msgs.msg import Int32
import rospy
import random
import time
import subprocess


#energy = 100
energy_turtle1 = -1
energy_turtle2 = -1
time_to_wait_min = 1
time_to_wait_max = 5
energy_decrement_max = 5
alarm = 0;

pen_turtle1 = [255,255,255,12, 0]


def consume_energy(req):
    global energy
    global time_to_wait_min
    global time_to_wait_min
    global energy_decrement_max
    global energy_turtle1
    global energy_turtle2
    global alarm
    global pen_turtle1
    
    # Cria o tópico para publicar mensagens de tipo Int32
    publisher1 = rospy.Publisher('/turtle1/energy', Int32, queue_size=10)
    publisher2 = rospy.Publisher('/turtle2/energy', Int32, queue_size=10)
    
    while True:
       if(energy_turtle1>0):
          energy1 = int(energy_turtle1 - random.uniform(1,energy_decrement_max))
          print("Current energy 1: ", energy1)
       
          publisher1.publish(energy1)
          
          if(energy1>=65):
             pen_turtle1[2] = int((energy1-65)*255/35)
             
          command = f'rosservice call /turtle1/set_pen '+ pen_turtle1[0] +' ' + pen_turtle1[1] + ' ' + pen_turtle1[2] + ' ' + pen_turtle1[3] +' 0'
          subprocess.Popen(command, shell=True)   
          
          
       if(energy_turtle2>0):
          energy2 = int(energy_turtle2 - random.uniform(1,energy_decrement_max))
          print("Current energy 2: ", energy2)
       
          publisher2.publish(energy2)   
       
       
       
       if alarm==0:
          move_to_critical = random.uniform(0, 100)
          # 5% of chance to move from safe to critical
          if move_to_critical <= 4: 
             alarm=1
             command = f'rostopic pub turtle1/alarm std_msgs/String critical'
             subprocess.Popen(command, shell=True)
          elif move_to_critical <= 9:
             alarm=2
             command = f'rostopic pub turtle2/alarm std_msgs/String critical'
             subprocess.Popen(command, shell=True)
          if alarm > 0:
             # Set the /turtlesim/background_r parameter to 200
             rospy.set_param('/turtlesim/background_r', 255)

             # Create a service proxy for the /clear service
             clear_service = rospy.ServiceProxy('/clear', Empty) 
             
             # Montar o comando a ser executado
             command = f'rosparam set /turtlesim/background_r 255 && rosparam set /turtlesim/background_0 86 &&  rosparam set /turtlesim/background_b 0 &&rosservice call /clear'

             # Executar o comando de forma não bloqueante
             subprocess.Popen(command, shell=True)
             
             print( "**** Critical alarm level *****")
       else:
          move_to_safe = random.uniform(0, 100)
          if move_to_safe <= 20: # 20% of chance to move from critical to safe
             alarm = 0
             command = f'rosparam set /turtlesim/background_r 69 && rosparam set /turtlesim/background_g 86 &&  rosparam set /turtlesim/background_b 255 && rosservice call /clear && rostopic pub turtle1/alarm std_msgs/String safe && rostopic pub turtle2/alarm std_msgs/String safe'
             subprocess.Popen(command, shell=True)
             print( "**** Safe alarm level *****")
          
          
       
       time_to_wait = random.uniform(time_to_wait_min, time_to_wait_max)
       rospy.sleep(time_to_wait)        
    return EmptyResponse()  # Retornando uma resposta vazia


def consume_energy_server():
    rospy.init_node('turtlesim_extended_turtle1')
    s = rospy.Service('turtle1/consume_energy', Empty, consume_energy)
    rospy.spin()


def callback_turtle1(data):
    global energy_turtle1
    energy_turtle1 = data.data  # Armazena o valor Int32 em uma variável
    rospy.loginfo(f"Recebido energy turtle 1: {energy_turtle1}")
    
def callback_turtle2(data):
    global energy_turtle2
    energy_turtle2 = data.data  # Armazena o valor Int32 em uma variável
    rospy.loginfo(f"Recebido energy turtle 2: {energy_turtle2}")    

if __name__ == "__main__":
  
     # Subscreve ao tópico para ler valores Int32
    rospy.Subscriber('/turtle1/energy', Int32, callback_turtle1)
    rospy.Subscriber('/turtle2/energy', Int32, callback_turtle2)

    consume_energy_server()
