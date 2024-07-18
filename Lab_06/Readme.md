# Lab 06 - Ros Bag

## Table of Contents
1. [What This Lab is About](#what-this-lab-is-about)
2. [Prerequisites](#prerequisites)
3. [Required Packages](#required-packages)
4. [Installation](#installation)
5. [Running the Lab](#running-the-lab)
6. [Use Cases](#use-cases)
7. [Working Screenshots](#working-screenshots)
8. [Additional Resources](#additional-resources)

## What This Lab is About

This lab is about using the `rosbag` tool to record and play back data from a ROS system. The `rosbag` tool is a command-line tool that allows you to record and play back data in ROS. It is useful for debugging and testing your ROS system. In this lab, you will learn how to record data from a ROS system using the `rosbag` tool and play back the recorded data.

## Prerequisites

- Basic knowledge of ROS
- A working ROS installation
- A working colcon workspace

## Required Packages

- ROS2
- `rosbag`

## Installation

- If you are using ROS2 Humble, ros2 bag installed as a part of your regular ROS 2 setup.
- If you are using ROS2 Foxy, you can install the `rosbag` tool using the following command:

    ```bash
    sudo apt-get install ros-foxy-ros2bag
    ```
- For the demonstration we’ll be using the turtle bot simulation,
Open up a new terminal and run turtlebot simulation using,

    ```bash
    ros2 run turtlesim turtlesim_node
    ```
- The turtle bot will be controlled using the telop keyboard commands so in another terminal window, run; 

    ```bash
    ros2 run turtlesim turtle_teleop_key
    ```

- Also for saving the data create a folder and locate to that using;

    ```bash
    mkdir bag_files
    cd bag_files
    ```
- Since now th turtle bot simulation is running you can find out which topics are published in the noe using the simple command; 

    ```bash
    ros2 topic list
    ```

- You will find a list of topics. During the previous lab session you learned that /turtle_teleop node publishes commands on the /turtle1/cmd_vel topic to make the turtle move in turtlesim. So let's dig into that using the command, 

    ```bash
    ros2 topic echo /turtle1/cmd_vel
    ```


- Now you will be able to see the data published on the node and lets capture these using, `ros2 bag record <topic>`

    ```bash
    ros2 bag record /turtle1/cmd_vel
    ```
- The data will be saved in a bag file and you can find the file in the folder you created earlier.

Here this captures the data published on the topic cmd_vel. 

- In the following command we will be capturing multiple topics. We also can provide a name for the bag file using -o <name>, and multiple topics need to captured and be listed with a space in between; 

    ```bash
    ros2 bag record -o subset /turtle1/cmd_vel /turtle1/pose
    ```


- Once recorded the bag file info can be obtained using `ros2 bag info <name>` and as for the example;

    ```bash
    ros2 bag info subset
    ```


- After retrieving the data it could be displayed using the command `ros2 bag play <name>` ;

    ```bash
    ros2 bag play subset
    ```

## Use Cases
- The `rosbag` tool is useful for debugging and testing your ROS system. You can record data from a ROS system using the `rosbag` tool and play back the recorded data to see what happened during the recording. This can help you identify problems in your ROS system and fix them.

## Working Screenshots
Include screenshots of the setup, code execution, and any output or results.

## Additional Resources
Provide links to additional resources that can help users understand the concepts covered in this tutorial.

