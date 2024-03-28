#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class DrawCircle(Node):
    def __init__(self):
        super().__init__('draw_circle')
        self.get_logger().info('draw_circle node is started')
        self.cmd_vel_pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.send_velocity_command)

def send_velocity_command(self):
    msg = Twist()
    msg.linear.x = 1.0
    msg.angular.z = 1.0
    self.cmd_vel_pub.publish(msg)
    self.get_logger().info('Sending velocity command')

def main(args=None):
    rclpy.init(args=args)

    node = DrawCircle()
    node.get_logger().info('This is node for drawing circle using turtle')
    rclpy.spin(node)

    rclpy.shutdown()