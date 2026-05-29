import rclpy    # the ROS 2 client library for Python
from rclpy.node import Node    # the ROS 2 Node class
from sensor_msgs.msg import BatteryState, Imu    # the BatteryState message type definition
# from geometry_msgs.msg import Quaternion, Vector3

class sensor_subscriber(Node):
    def __init__(self):
        super().__init__("sensor_subscriber")    # names the node when running

        self.battery_sub = self.create_subscription(
            BatteryState,        # the message type
            "/battery_state",    # the topic name
            self.log_voltage,  # the subscription's callback method
            10              # QOS (will be covered later)
        )

        self.imu_sub = self.create_subscription(
            Imu,
            "/imu",
            self.log_imu,
            10
        )

        self.get_logger().info("initialized sensor subscriber node")

    def log_voltage(self, msg):
        self.voltage = msg.voltage

        # self.get_logger().info("battery voltage: " + str(self.voltage))

        if self.voltage / 4 < 3.0: 
            self.get_logger().warn("unsafe battery voltage!")

    def log_imu(self, msg):
        self.orientation = msg.orientation
        self.angular_velocity = msg.angular_velocity
        self.linear_acceleration = msg.linear_acceleration

        self.get_logger().info(f"orientation: {self.orientation}")
        self.get_logger().info(f"angular velocity: {self.angular_velocity}")
        self.get_logger().info(f"linear acceleration: {self.linear_acceleration}")


def main(args=None):
    rclpy.init(args=args)
    node = sensor_subscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("\nKeyboardInterrupt received, shutting down...")
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()