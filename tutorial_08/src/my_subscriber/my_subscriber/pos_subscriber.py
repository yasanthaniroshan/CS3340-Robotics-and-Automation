#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


class MySubscriber(Node):

    def __init__(self):
        super().__init__('my_subscriber')
        self.get_logger().info('MySubscriber node has been started')
        self.pos_subscriber = self.create_subscription(Pose,'turtle1/pose',self.listener_callback,10)


    def listener_callback(self, msg: Pose):
        self.get_logger().info('I heard: "%s"' % msg)



def main(args=None):
    rclpy.init(args=args)
    node = MySubscriber()
    rclpy.spin(node)
    rclpy.shutdown()
