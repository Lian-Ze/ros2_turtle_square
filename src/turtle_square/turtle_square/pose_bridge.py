import math
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import PoseStamped

class PoseBridge(Node):
    def __init__(self):
        super().__init__('pose_bridge')
        self.subscription = self.create_subscription(
            Pose, '/turtle1/pose', self.pose_callback, 10)
        self.publisher = self.create_publisher(
            PoseStamped, '/turtle1/pose_stamped', 10)

    def pose_callback(self, pose):
        msg = PoseStamped()
        msg.header.frame_id = 'world'
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.pose.position.x = pose.x
        msg.pose.position.y = pose.y
        msg.pose.position.z = 0.0
        msg.pose.orientation.z = math.sin(pose.theta / 2.0)
        msg.pose.orientation.w = math.cos(pose.theta / 2.0)
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = PoseBridge()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

