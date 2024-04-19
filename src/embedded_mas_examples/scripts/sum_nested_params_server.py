#!/usr/bin/env python3


# Calculates the euclidian distance between 2 3d points


from __future__ import print_function

from embedded_mas_examples.srv import NestedSum
import rospy

def handle_sum_nested_params(req):
    print(req)

    #print("x.x",req.x.x)
    #print("x.y",req.x.y)
    #print("x.z",req.x.z)
    #print(req.y)
    #print(req.z)
    return ((req.x.x-req.y.x)**2+(req.x.y-req.y.y)**2+(req.x.z-req.y.z)**2)**0.5

def sum_nested_params_server():
    print("----")
    rospy.init_node('sum_nested_params_server')
    s = rospy.Service('sum_nested_params', NestedSum, handle_sum_nested_params)
    print("Ready sum nested params.")
    rospy.spin()

if __name__ == "__main__":
    sum_nested_params_server()
    
#rosservice call sum_nested_params "{'x':[1,2,3],'y':[4,5,6]}"

#"{'x':{'x':1,'y':2,'z':3},'y':{'x':1,'y':2,'z':3}}

#{"x":{"x":1,"y":2,"x":3},"y":{"x":1,"y":2,"x":3}}

#"stamp":{"secs":0,"nsecs":0},"frame_id":"uav1/local_origin"},"reference":{"position":{"x":8.0,"y":8.0,"z":2.0},"heading":0.0}}
