#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import time 
from socket_read import *

import rospy
from bert2_simulator.msg import *
from std_msgs.msg import Int8, String

def ros_fatal(fatal_str):
    print "ROS_FATAL:", fatal_str
   

def ros_event_p(topic, vals):
    if topic == 'gaze':
        gaze_p.Publish(float(vals[0]), float(vals[1]), float(vals[2]))
    elif topic == 'human_signals':
        human_signals_p.Publish(int(vals[0]), int(vals[1]))
    elif topic == 'pressure_e2':
        pressure_e2_p.Publish(int(vals[0]))
    elif topic == 'location':
        location_p.Publish(float(vals[0]), float(vals[1]), float(vals[2]))
    else:
        pass; 
        # FATAL: unknown topic
        
def doit(port):

    rospy.init_node('specman', anonymous=True)
    human_signals_p = rospy.Publisher('human_signals', Human, queue_size=1, latch=True)
    pressure_e2_p = rospy.Publisher('pressure_e2', Int8, queue_size=1, latch=True)
    gaze_p = rospy.Publisher('gaze', Gaze, queue_size=1, latch=True)
    location_p = rospy.Publisher('location', Location, queue_size=1, latch=True)
    ros_fatal_p = rospy.Publisher('ros_fatal', String, queue_size=1, latch=True)
    
    sock = Socket_Read(HOSTNAME, port);

    while True:
        # Look for the response
        (status, topic, vals) = sock.read_event()

        #print "Status: ", status
        #print "Vals:", vals

        if status == Socket_Read.EOF:
            break

        if status == Socket_Read.Fatal:
            # fatal_error(topic)
            break
        
        # normal ros_event
        ros_event_p(topic, vals);
        
    sock.close()

if __name__  == '__main__':
    doit(int(sys.argv[1]))

