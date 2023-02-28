#rosservice call sum_array 1 2 [41,22]
#!/usr/bin/env python3

from __future__ import print_function

import sys
import rospy
from embedded_mas_examples.srv import *

def sum_array_client(v):
    rospy.wait_for_service('sum_array')
    try:
        sum_array = rospy.ServiceProxy('sum_array', SumArray)
        resp1 = sum_array(v)
        return resp1.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        #print("terceiro argumento: ", sys.argv[3], type(sys.argv[3]))
        #x = int(sys.argv[1])
        #y = int(sys.argv[2])
        #v = list(map(int,sys.argv[3]))
        v = sys.argv[1]
        #v = [22,33,40]
    else:
        print(usage())
        sys.exit(1)
    #print("Requesting %s+%s - %s"%(x, y, v))
    #print("%s + %s = %s"%(x, y, sum_array_client(x, y, v)))
