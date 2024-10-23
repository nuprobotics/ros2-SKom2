import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class Publisher(Node):
    def __init__(self):
        super().__init__("publisher")
        self.declare_parameter("topic_name", "default_topic")
        self.declare_parameter("text", "default_text")
        self.topic_name = self.get_parameter("topic_name").get_parameter_value().string_value
        self.text = self.get_parameter("text").get_parameter_value().string_value
        self.publisher = self.create_publisher(String, self.topic_name, 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = self.text
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    publisher_node = Publisher()
    rclpy.spin(publisher_node)
    publisher_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()