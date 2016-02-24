#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from datetime import datetime

import csv

def callback(data):
   c = csv.writer(open("/home/jinahadam/catkin_ws/src/joy_logger/joy.csv", "ab"))
   c.writerow([str(datetime.now()),data.axes[0],data.axes[1],data.axes[2],data.axes[3],data.axes[4],data.axes[5],data.axes[6],data.axes[7]])


    
def logger():
    rospy.init_node('joy_logger', anonymous=True)
    rospy.Subscriber("joy", Joy, callback)
    rospy.spin()

if __name__ == '__main__':
    c = csv.writer(open("/home/jinahadam/catkin_ws/src/joy_logger/joy.csv", "wb"))
    print("joy_logger started. data logged to \n /home/jinahadam/catkin_ws/src/joy_logger/joy.csv")
    logger()
