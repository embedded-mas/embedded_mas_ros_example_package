#!/usr/bin/env python3

import rospy
from embedded_mas_examples.msg import ExampleMsgWithArray
from embedded_mas_examples.srv import PublishMsgWithArray, PublishMsgWithArrayResponse

publisher = None

def handle_publish(req):
    global publisher
    publisher.publish(req.msg)
    rospy.loginfo("Message published to /array_topic")
    return PublishMsgWithArrayResponse(True)

def main():
    global publisher

    rospy.init_node("example_service_publisher")

    publisher = rospy.Publisher(
        "/array_topic",
        ExampleMsgWithArray,
        queue_size=10
    )

    rospy.Service(
        "publish_example_msg",
        PublishMsgWithArray,
        handle_publish
    )

    rospy.loginfo("Service publish_example_msg ready")

    rospy.spin()

if __name__ == "__main__":
    main()
