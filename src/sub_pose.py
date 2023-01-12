#!/usr/bin/env python

import rospy
import geometry_msgs.msg as geomsg # Point object
import visualization_msgs.msg as vismsg

gps_x = []
gps_y = []
file1 = open("new.csv", "a")  # append mode
# marker
mark_p = vismsg.Marker()
mark_p.header.frame_id = "map_zala_0"
mark_p.type = vismsg.Marker().LINE_STRIP
mark_p.action = vismsg.Marker().ADD
mark_p.scale.x = 0.4
mark_p.color.a = 0.8 # visibility
mark_p.pose.orientation.x = mark_p.pose.orientation.y = mark_p.pose.orientation.z = 0.0
mark_p.pose.orientation.w = 1.0
mark_p.pose.position.x = mark_p.pose.position.y = mark_p.pose.position.z = 0.0

pub_s = rospy.Publisher("lane_new", vismsg.Marker, queue_size=1)

def poseCallBack(msg):
    global gps_x, gps_y, file1, mark_p, pub_s
    #gps_x.append(msg.point.x) 
    #gps_y.append(msg.point.y)
    #print(msg)        
    print(msg.pose.position.x, msg.pose.position.y)        
    file1.write(str(msg.pose.position.x) + "," + str(msg.pose.position.y) + "\n")
    md_amber_500_r = 1.00; md_amber_500_g = 0.76; md_amber_500_b = 0.03
    ## https://github.com/jkk-research/colors
    mark_p.color.r = md_amber_500_r; mark_p.color.g = md_amber_500_g; mark_p.color.b = md_amber_500_b
    pl1 = geomsg.Point(); pl1.x = msg.pose.position.x; pl1.y = msg.pose.position.y; pl1.z = 20.0
    mark_p.points.append(pl1)
    pub_s.publish(mark_p)


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