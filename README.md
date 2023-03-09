# embedded_mas_ros_example_package

This package contains some ROS services used in the examples of embedded-mas framework. 

To install the package, use the following sequence of commands. Make sure that ROS noetic is installed and started (with *roscore* command)

```
sudo apt-get update -y
sudo apt install -y wget
wget https://raw.githubusercontent.com/embedded-mas/embedded_mas_ros_example_package/master/install.sh
chmod +x install.sh
./install.sh
. /catkin_wsp/devel/setup.bash
rosrun embedded_mas_examples sum_array_server.py 
```
