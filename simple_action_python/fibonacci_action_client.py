import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from action_tutorials_interfaces.action import Fibonacci


class FibonacciActionClient(Node):

    def __init__(self):
        super().__init__('fibonacci_action_client')
        self._action_client = ActionClient(self, Fibonacci, 'fibonacci')

    # 1번
    def send_goal(self, order):
        goal_msg = Fibonacci.Goal() # action파일의 goal 생성
        goal_msg.order = order # request시 사용할 데이터 지정 

        self._action_client.wait_for_server() # action server가 응답할때까지 대기
        self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.c_feedback_callback)
        self._send_goal_future.add_done_callback(self.c_goal_response_callback)

    # 2번
    def c_goal_response_callback(self, future):
        goal_handle = future.result() # Goal Service에서의 response
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')
        self._get_result_future = goal_handle.get_result_async() # 3번
        self._get_result_future.add_done_callback(self.c_get_result_callback)

    # 5번
    def c_get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.sequence))
        rclpy.shutdown()

    # 4번
    def c_feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback.partial_sequence))


def main(args=None):
    rclpy.init(args=args)
    action_client = FibonacciActionClient()
    action_client.send_goal(10)
    rclpy.spin(action_client)


if __name__ == '__main__':
    main()