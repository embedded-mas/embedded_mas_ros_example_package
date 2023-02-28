# Install script for directory: /media/maiquel/DATA/maiquel/git/embedded_mas_ros_example_package/src/embedded_mas_examples

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/media/maiquel/DATA/maiquel/git/embedded_mas_ros_example_package/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/embedded_mas_examples/srv" TYPE FILE FILES "/media/maiquel/DATA/maiquel/git/embedded_mas_ros_example_package/src/embedded_mas_examples/srv/SumArray.srv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/embedded_mas_examples/cmake" TYPE FILE FILES "/media/maiquel/DATA/maiquel/git/embedded_mas_ros_example_package/build/embedded_mas_examples/catkin_generated/installspace/embedded_mas_examples-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/media/maiquel/DATA/maiquel/git/embedded_mas_ros_example_package/devel/include/embedded_mas_examples")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/media/maiquel/DATA/maiquel/git/embedded_mas_ros_example_package/devel/share/roseus/ros/embedded_mas_examples")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/media/maiquel/DATA/maiquel/git/embedded_mas_ros_example_package/devel/share/common-lisp/ros/embedded_mas_examples")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/media/maiquel/DATA/maiquel/git/embedded_mas_ros_example_package/devel/share/gennodejs/ros/embedded_mas_examples")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/media/maiquel/DATA/maiquel/git/embedded_mas_ros_example_package/devel/lib/python3/dist-packages/embedded_mas_examples")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/media/maiquel/DATA/maiquel/git/embedded_mas_ros_example_package/devel/lib/python3/dist-packages/embedded_mas_examples")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/media/maiquel/DATA/maiquel/git/embedded_mas_ros_example_package/build/embedded_mas_examples/catkin_generated/installspace/embedded_mas_examples.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/embedded_mas_examples/cmake" TYPE FILE FILES "/media/maiquel/DATA/maiquel/git/embedded_mas_ros_example_package/build/embedded_mas_examples/catkin_generated/installspace/embedded_mas_examples-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/embedded_mas_examples/cmake" TYPE FILE FILES
    "/media/maiquel/DATA/maiquel/git/embedded_mas_ros_example_package/build/embedded_mas_examples/catkin_generated/installspace/embedded_mas_examplesConfig.cmake"
    "/media/maiquel/DATA/maiquel/git/embedded_mas_ros_example_package/build/embedded_mas_examples/catkin_generated/installspace/embedded_mas_examplesConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/embedded_mas_examples" TYPE FILE FILES "/media/maiquel/DATA/maiquel/git/embedded_mas_ros_example_package/src/embedded_mas_examples/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/embedded_mas_examples" TYPE PROGRAM FILES "/media/maiquel/DATA/maiquel/git/embedded_mas_ros_example_package/build/embedded_mas_examples/catkin_generated/installspace/sum_array_client.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/embedded_mas_examples" TYPE PROGRAM FILES "/media/maiquel/DATA/maiquel/git/embedded_mas_ros_example_package/build/embedded_mas_examples/catkin_generated/installspace/sum_array_server.py")
endif()

