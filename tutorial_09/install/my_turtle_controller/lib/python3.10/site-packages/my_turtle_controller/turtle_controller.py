#! usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from time import sleep

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.get_logger().info('Turtle Controller Node has been started')
        self.cmd_vel_publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.pose_subscriber = self.create_subscription(Pose, 'turtle1/pose', self.pose_callback, 10)

    def pose_callback(self, pose: Pose):
        twist = Twist()
        if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
            self.get_logger().info('Turtle has reached the x limit')
            twist.linear.x = 1.0
            twist.angular.z = 0.9
        else:
            twist.linear.x = 5.0
            twist.angular.z = 0.0
        self.cmd_vel_publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)
    rclpy.shutdown()