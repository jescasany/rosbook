#!/usr/bin/env python

import roslib; roslib.load_manifest('basics')

import rospy
from basics.msg import Complex


def callback(msg):
    print 'Real:', msg.real
    print 'Imaginary:', msg.imaginary
    print
    

rospy.init_node('message_subscriber')

sub = rospy.Subscriber('complex', Complex, callback)

rospy.spin()

