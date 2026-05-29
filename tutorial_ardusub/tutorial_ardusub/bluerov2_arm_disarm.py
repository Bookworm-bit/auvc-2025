from std_srvs.srv import SetBool

import rclpy    # the ROS 2 client library for Python
from rclpy.node import Node    # the ROS 2 Node class

class arm_disarm(Node):
    def __init__(self):
        super().__init__("arm_disarm")    # names the node when running

        self.cli = self.create_client(
            SetBool,
            "/arming"
        )

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("arming service not available, waiting...")

        self.req = SetBool.Request()

    def send_request(self, data):
        self.req.data = data
        return self.cli.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)
    node = arm_disarm()
    future = node.send_request(True)
    rclpy.spin_until_future_complete(node, future)
    response = future.result()

    if response.success:
        node.get_logger().info("arm successful!")
    else:
        node.get_logger().warn("arm failed!")

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("shutting down!")

        future = node.send_request(False)
        rclpy.spin_until_future_complete(node, future)
        response = future.result()

        # if response == None:
        #     node.get_logger().info("executor was killed by keyboard interrupt. no response was returned but the robot probably disarmed, check the SITL.")
        # elif response.success:
        #     node.get_logger().info("disarm successful!")
        # else:
        #     node.get_logger().warn("disarm failed!")

        node.get_logger().info("no response was returned. robot was likely disarmed")
        node.get_logger().warn("check robot indicator lights before touching")
    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()