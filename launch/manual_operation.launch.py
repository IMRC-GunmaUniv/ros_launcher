from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    controller_receiver_node = Node(
        package='joy',
        executable='joy_node',
        name='controller_receiver',
        arguments=['--ros-args', '--log-level', 'warn'],
    )

    cmd_vel_pad_node = Node(
        package='imrc_pad_cmd_vel',
        executable='pad_cmd_vel',
        name='joy_to_cmd_vel',
        arguments=['--ros-args', '--log-level', 'warn'],

    )

    cmd_vel_selector_node = Node(
        package='imrc_cmd_vel_selector',
        executable='cmd_vel_selector',
        name='cmd_vel_selector',
        arguments=['--ros-args', '--log-level', 'warn'],

    )

    uart_bridge_node = Node(
        package='uart_bridge',
        executable='bridge',
        name='uart_bridge',
        output='screen',
        arguments=['--ros-args', '--log-level', 'warn'],

    )

    return LaunchDescription([
        controller_receiver_node,
        cmd_vel_pad_node,
        cmd_vel_selector_node,
        uart_bridge_node
    ])

