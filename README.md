# mostly_local_kinect_rtab

files for ros melodic on ubuntu 18 and commands which gathered the data at the time
These instructions allow you to have a mostly self contained rtab and kinect set up and generate a mesh file from it.
I used this to make a point cloud of my buildings hallway for fun.
!( point cloud of my hallway )[./media/my_hallway_pointcloud.gif "point cloud of my hallway"]

## an absurdly easy set up instructions I made
I assume you are using ros melodic
```
sudo whoami

mkdir -p kinect_mapping_workspace/src
cd kinect_mapping_workspace/src
git clone https://github.com/ros-drivers/freenect_stack.git
# rtabmap_ros
git clone https://github.com/introlab/rtabmap_ros.git
cd rtabmap_ros ; git checkout melodic-devel ; cd ../
# navigation - move_base
git clone https://github.com/ros-planning/navigation.git
cd navigation ; git checkout melodic-devel ; cd ../
# geometry2 - tf2
git clone https://github.com/ros/geometry2.git
cd geometry2 ; git checkout melodic-devel ; cd ../
# navigation_msgs is already made for kinetic and above - move_base_msgs
git clone https://github.com/ros-planning/navigation_msgs.git
# octomap msgs
git clone https://github.com/OctoMap/octomap_msgs.git
cd octomap_msgs/ ; git checkout melodic-devel ; cd ../
# apriltag_ros
git clone https://github.com/AprilRobotics/apriltag_ros.git  # Clone Apriltag ROS wrapper
# find-object
git clone https://github.com/introlab/find-object.git
cd find-object/ ; git checkout melodic-devel ; cd ../
# rgbd_launch
git clone https://github.com/ros-drivers/rgbd_launch.git

# To install to a different directory than /usr/local: DO --> PREFIX=/some/path sudo make install
# install to usr/local
cd ../
git clone https://github.com/AprilRobotics/apriltag.git      # Clone Apriltag library
cd apriltag
cmake .
sudo make install
cd ../

# rtabmap
git clone https://github.com/introlab/rtabmap.git
cd rtabmap ; git checkout melodic-devel
cmake . # Build files have been written to: $HOME/workspace/kinect_mapping_workspace/rtabmap
sudo make install
cd ../


sudo apt-get install libsdl-image1.2-dev
sudo apt-get install libsdl-dev

# use VVV instead of catkin_make because there are catkin and cmake packages ( apriltag )
# catkin_make_isolated
catkin_make
```



