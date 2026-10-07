import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawSquareNode(Node):
    def __init__(self):
        super().__init__('draw_square')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.i = 0
        self.declare_parameter('speed', 1.0)   # ★ 新增：声明参数 speed，默认 1.0

    def timer_callback(self):
        msg = Twist()
        speed = self.get_parameter('speed').value   # ★ 新增：实时读取参数
        if self.i % 2 == 0:
            msg.linear.x = speed                     # 把写死的 1.0 换成参数 speed
            msg.angular.z = 0.0
        else:
            msg.linear.x = 0.0
            msg.angular.z = 1.57
        self.publisher.publish(msg)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    node = DrawSquareNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__&#8203;main__':
    main()

