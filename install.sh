apt install wget
apt install unzip
mkdir catkin_wsp
cd catkin_wsp
#mkdir src
catkin_make
source devel/setup.bash

wget https://github.com/embedded-mas/embedded_mas_ros_example_package/raw/master/src.zip
unzip src.zip .
