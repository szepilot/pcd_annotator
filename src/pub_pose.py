#!/usr/bin/env python

import rospy, rospkg
import visualization_msgs.msg as vismsg
import geometry_msgs.msg as geomsg




gps_x = []
gps_y = []

def alap(): 
    global gps_x, gps_y
    import csv
    rospy.init_node("pubbb", anonymous=True)
    rospack = rospkg.RosPack()
    path_pkg = rospack.get_path("pcd_annotator")
    csv_path = path_pkg + "/src/" + rospy.get_param("~csv")
    rospy.loginfo("Opening " + csv_path)
    with open(csv_path) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            print(row[0] + " -- " + row[1])
            gps_x.append(float(row[0])) 
            gps_y.append(float(row[1])) 
    tag = (rospy.get_param("~csv")).split(".")[0]
    pub_s = rospy.Publisher("lane" + tag, vismsg.Marker, queue_size=1)
    rate=rospy.Rate(5)
    rospy.logdebug("started...")

    # marker
    mark_p = vismsg.Marker()
    mark_p.header.frame_id = "map_zala_0"
    mark_p.type = vismsg.Marker().LINE_STRIP
    mark_p.action = vismsg.Marker().ADD
    mark_p.scale.x = 0.4
    ## https://github.com/jkk-research/colors
    md_red_500_r = 0.96; md_red_500_g = 0.26; md_red_500_b = 0.21
    md_pink_500_r = 0.91; md_pink_500_g = 0.12; md_pink_500_b = 0.39
    md_deep_purple_500_r = 0.40; md_deep_purple_500_g = 0.23; md_deep_purple_500_b = 0.72
    md_blue_500_r = 0.13; md_blue_500_g = 0.59; md_blue_500_b = 0.95
    md_cyan_500_r = 0.00; md_cyan_500_g = 0.74; md_cyan_500_b = 0.83
    md_green_500_r = 0.30; md_green_500_g = 0.69; md_green_500_b = 0.31
    md_yellow_500_r = 1.00; md_yellow_500_g = 0.92; md_yellow_500_b = 0.23
    md_amber_500_r = 1.00; md_amber_500_g = 0.76; md_amber_500_b = 0.03
    md_orange_500_r = 1.00; md_orange_500_g = 0.60; md_orange_500_b = 0.00
    md_brown_500_r = 0.47; md_brown_500_g = 0.33; md_brown_500_b = 0.28
    md_grey_500_r = 0.62; md_grey_500_g = 0.62; md_grey_500_b = 0.62
    color = "blue"
    color = rospy.get_param("~color")
    if (color == "red"): mark_p.color.r = md_red_500_r; mark_p.color.g = md_red_500_g; mark_p.color.b = md_red_500_b
    elif (color == "deep_purple"): mark_p.color.r = md_deep_purple_500_r; mark_p.color.g = md_deep_purple_500_g; mark_p.color.b = md_deep_purple_500_b
    elif (color == "pink"): mark_p.color.r = md_pink_500_r; mark_p.color.g = md_pink_500_g; mark_p.color.b = md_pink_500_b
    elif (color == "blue"): mark_p.color.r = md_blue_500_r; mark_p.color.g = md_blue_500_g; mark_p.color.b = md_blue_500_b
    elif (color == "cyan"): mark_p.color.r = md_cyan_500_r; mark_p.color.g = md_cyan_500_g; mark_p.color.b = md_cyan_500_b
    elif (color == "green"): mark_p.color.r = md_green_500_r; mark_p.color.g = md_green_500_g; mark_p.color.b = md_green_500_b
    elif (color == "yellow"): mark_p.color.r = md_yellow_500_r; mark_p.color.g = md_yellow_500_g; mark_p.color.b = md_yellow_500_b
    elif (color == "amber"): mark_p.color.r = md_amber_500_r; mark_p.color.g = md_amber_500_g; mark_p.color.b = md_amber_500_b
    elif (color == "orange"): mark_p.color.r = md_orange_500_r; mark_p.color.g = md_orange_500_g; mark_p.color.b = md_orange_500_b
    elif (color == "brown"): mark_p.color.r = md_brown_500_r; mark_p.color.g = md_brown_500_g; mark_p.color.b = md_brown_500_b
    elif (color == "grey"): mark_p.color.r = md_grey_500_r; mark_p.color.g = md_grey_500_g; mark_p.color.b = md_grey_500_b
    else: mark_p.color.r = md_red_500_r; mark_p.color.g = md_red_500_g; mark_p.color.b = md_red_500_b
    mark_p.color.a = 0.8 # visibility
    mark_p.pose.orientation.x = mark_p.pose.orientation.y = mark_p.pose.orientation.z = 0.0
    mark_p.pose.orientation.w = 1.0
    mark_p.pose.position.x = mark_p.pose.position.y = mark_p.pose.position.z = 0.0

    while not rospy.is_shutdown():
        mark_p.points = []
        i = 0
        for i in range(len(gps_x)):
            pl1 = geomsg.Point(); pl1.x = gps_x[i]; pl1.y = gps_y[i]; pl1.z = 20.0
            mark_p.points.append(pl1)
        pub_s.publish(mark_p)
        rate.sleep()


if __name__ == '__main__':
    alap()
