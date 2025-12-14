from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    controller_receiver_node = Node(
        package='joy',
        executable='joy_node',
        name='controller_receiver'
    )

    cmd_vel_pad_node = Node(
        package='imrc_pad_cmd_vel',
        executable='pad_cmd_vel',
        name='joy_to_cmd_vel'
    )

    cmd_vel_selector_node = Node(
        package='imrc_cmd_vel_selector',
        executable='cmd_vel_selector',
        name='cmd_vel_selector'
    )

    uart_bridge_node = Node(
        package='uart_bridge',
        executable='bridge',
        name='uart_bridge',
        output='screen'
    )

    return LaunchDescription([
        controller_receiver_node,
        cmd_vel_pad_node,
        cmd_vel_selector_node,
        uart_bridge_node
    ])

