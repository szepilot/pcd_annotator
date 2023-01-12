#!/usr/bin/env python

import rospy
import geometry_msgs.msg as geomsg # Point object

gps_x = []
gps_y = []
file1 = open("s1.csv", "a")  # append mode
    
def poseCallBack(msg):
    global gps_x, gps_y, file1
    #gps_x.append(msg.point.x) 
    #gps_y.append(msg.point.y)
    #print(msg)        
    print(msg.pose.position.x, msg.pose.position.y)        
    file1.write(str(msg.pose.position.x) + "," + str(msg.pose.position.y) + "\n")

def alap(): 
    global gps_x, gps_y, file1
 
    rospy.init_node("listener_marker", anonymous=True)  
    rospy.Subscriber("/move_base_simple/goal", geomsg.PoseStamped, poseCallBack)
    print("started")
    rospy.loginfo("started...")
    rospy.spin()
    #file1.close()


if __name__ == '__main__':
    alap()