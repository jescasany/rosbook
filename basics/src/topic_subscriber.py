#!/usr/bin/env python

import roslib; roslib.load_manifest('basics')

import rospy
from std_msgs.msg import Int32


def callback(msg):
    print msg.data
    

rospy.init_node('topic_subscriber')

sub = rospy.Subscriber('counter', Int32, callback)

rospy.spin()

