#! /usr/bin/env python3
import rclpy
from rclpy.node import Node


class MyNode(Node):
    def __init__(self):
        super().__init__('my_first_node')
        self.get_logger().info('Hello ROS2')
        self.conter = 0
        self.create_timer(1.0, self.timer_callback)


    def timer_callback(self):
        self.get_logger().info("Hello %d" % self.conter)
        self.conter += 1


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()