#!/bin/bash 

sudo apt install -y unzip
sudo apt install -y make
sudo apt install -y build-essential g++
mkdir catkin_wsp
wget https://github.com/embedded-mas/embedded_mas_ros_example_package/raw/master/src.zip
unzip src.zip -d catkin_wsp
cd catkin_wsp
catkin_make
cd ..
. /catkin_wsp/devel/setup.bash


# After run this script, ensure that roscore is running and start the example services with the following command:
# rosrun embedded_mas_examples sum_array_server.py
