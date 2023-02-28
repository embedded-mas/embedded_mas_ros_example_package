#!/usr/bin/env python3

from __future__ import print_function

from embedded_mas_examples.srv import SumArray,SumArrayResponse
import rospy

def handle_sum_array(req):
    #print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    #print(req.v)
    sum = 0
    for i in req.v:
       sum = sum+i
    #return SumArrayResponse(req.a + req.b)
    #return sum(req.v)
    return sum

def sum_array_server():
    rospy.init_node('sum_array_server')
    s = rospy.Service('sum_array', SumArray, handle_sum_array)
    print("Ready sum array.")
    rospy.spin()

if __name__ == "__main__":
    sum_array_server()
