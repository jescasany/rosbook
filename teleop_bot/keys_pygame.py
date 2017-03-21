#!/usr/bin/env python
import pygame
import rospy
from std_msgs.msg import String

g_key_pub = None

def draw_string(screen, font, x, y, string):
  text = font.render(string, 1, (255,255,255))
  screen.blit(text, (x, y))

def keypress(key):
  print "key: %s" % key
  g_key_pub.publish(String(key))

if __name__ == '__main__':
  pygame.init()
  screen = pygame.display.set_mode((640,480))
  font = pygame.font.Font(None,18)
  pygame.display.set_caption('keyboard driver')
  draw_string(screen, font, 10, 10, "This window must have focus.")
  draw_string(screen, font, 10, 30, "Press [escape] to quit.")
  pygame.display.flip()
  done = False
  g_key_pub = rospy.Publisher('keys', String)
  rospy.init_node("keyboard_driver")
  rate = rospy.Rate(100)
  while not done:
    for event in pygame.event.get():
      if (event.type == pygame.KEYDOWN):
        if event.key == pygame.K_ESCAPE:
          done = True
        elif event.key < 128:
          keypress(chr(event.key))
    rate.sleep()

