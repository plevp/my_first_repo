#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import time 
from socket_read import *

#import rospy
#from bert2_simulator.msg import *
#from std_msgs.msg import Int8, String

HOSTNAME = 'xn01'

def location_p(x, y, z):
    print "ROS_EVENT Location:", x, y, z

def gaze_p(offset, distance, angle):
    print "ROS_EVENT Gaze:", offset, distance, angle

def human_signals_p(a,b):
    print "ROS_EVENT human_signals:", a, b

def pressure_e2_p(data):
    print "ROS_EVENT pressure_e2:", data

def ros_fatal(fatal_str):
    print "ROS_FATAL:", fatal_str
   

def ros_event_p(topic, vals):
    if topic == 'gaze':
        #gaze_p.Publish(float(vals[0]), float(vals[1]), float(vals[2]))
        gaze_p(float(vals[0]), float(vals[1]), float(vals[2]))
    elif topic == 'human_signals':
        #human_signals_p.Publish(int(vals[0]), int(vals[1]))
        human_signals_p(int(vals[0]), int(vals[1]))
    elif topic == 'pressure_2':
        #pressure_e2_p.Publish(int(vals[0]))
        pressure_e2_p(int(vals[0]))
    elif topic == 'location':
        #location_p.Publish(float(vals[0]), float(vals[1]), float(vals[2]))
        location_p(float(vals[0]), float(vals[1]), float(vals[2]))
    else:
        pass; 
        # FATAL: unknown topic
        
def doit(port):
    """
    rospy.init_node('specman', anonymous=True)
    human_signals_p = rospy.Publisher('human_signals', Human, queue_size=1, latch=True)
    pressure_e2_p = rospy.Publisher('pressure_e2', Int8, queue_size=1, latch=True)
    gaze_p = rospy.Publisher('gaze', Gaze, queue_size=1, latch=True)
    location_p = rospy.Publisher('location', Location, queue_size=1, latch=True)
    ros_fatal_p = rospy.Publisher('ros_fatal', String, queue_size=1, latch=True)
    """
    
    sock = Socket_Read(HOSTNAME, port);

    while True:
        # Look for the response
        (status, topic, vals) = sock.read_event()

        print "Status: ", status
        print "Topic:", topic
        print "Vals:", vals

        if status == Socket_Read.EOF:
            print "ROS_EOF"
            break

        if status == Socket_Read.Fatal:
            # fatal_error(topic)
            break
        # normal
        ros_event_p(topic, vals);
        
    sock.close()

"""
def doit(port):

    sock = Socket_Read(HOSTNAME, port);
    fp = open("tmp.txt", "w");
    while True:
        # Look for the response
        data = sock.read_line()
        if data == None:
            break
        print 'received "%s(%d)"' % (data, len(data))
        
        fp.write(data+"\n");
        
        if data == "It is the last line":
            break;

    fp.close();
    sock.close()
"""

if __name__  == '__main__':
    doit(int(sys.argv[1]))

