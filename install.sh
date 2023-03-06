#!/bin/bash 

apt install -y unzip
apt install -y make
apt install -y build-essential g++
mkdir catkin_wsp
cd catkin_wsp
wget https://github.com/embedded-mas/embedded_mas_ros_example_package/raw/master/src.zip
unzip src.zip
catkin_make
source devel/setup.bash
rosrun embedded_mas_examples sum_array_server.py
