#!/usr/bin/env python
import roslib; roslib.load_manifest('teleop_bot_keyboard')
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

key_mapping = { 'w': [ 0, 1], 'x': [0, -1], 
                'a': [-1, 0], 'd': [1,  0], 
                's': [ 0, 0] }

def keys_cb(msg, twist_pub):
  if len(msg.data) == 0 or not key_mapping.has_key(msg.data[0]):
    return # unknown key.
  key = msg.data[0]  # todo: handle upper-case
  vels = key_mapping[key]
  t = Twist()
  t.angular.z = vels[0]
  t.linear.x  = vels[1]
  twist_pub.publish(t)

if __name__ == '__main__':
  rospy.init_node('keys_to_twist')
  twist_pub = rospy.Publisher('cmd_vel', Twist)
  rospy.Subscriber('keys', String, keys_cb, twist_pub)
  rospy.spin()
