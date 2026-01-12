from launch import LaunchDescription
from launch_ros.actions import Node

from ros_launcher.serial_resolver import *

def generate_launch_description():
    odom_serial_number = "066DFF3530384E5043175544" # test
    bridge_serial_number = "066CFF545052836687063813" # test
    lidar_serial_number = "f42d0bf576b32a45adcf5faec7c8ea2d"

    display_device_list()

    odom_dev = get_tty_by_serial(odom_serial_number)
    if(odom_dev == None):
        print(">>> Serial device \"odom\" is not connected.")
    else:
        print(f"Serial device \"odom\" found at: {odom_dev}")


    bridge_dev = get_tty_by_serial(bridge_serial_number)
    if(bridge_dev == None):
        print(">>> Serial device \"bridge\" is not connected.")
    else:
        print(f"Serial device \"bridge\" found at: {bridge_dev}")

    lidar_dev = get_tty_by_serial(lidar_serial_number)
    if(lidar_dev == None):
        print(">>> Serial device \"lidar\" is not connected.")
    else:
        print(f"Serial device \"bridge\" found at: {lidar_dev}")


    controller_receiver_node = Node(
        package='joy',
        executable='joy_node',
        name='controller_receiver',
        arguments=['--ros-args', '--log-level', 'info'],
    )

    cmd_vel_pad_node = Node(
        package='imrc_pad_cmd_vel',
        executable='pad_cmd_vel',
        name='joy_to_cmd_vel',
        arguments=['--ros-args', '--log-level', 'info'],

    )

    cmd_vel_selector_node = Node(
        package='imrc_cmd_vel_selector',
        executable='cmd_vel_selector',
        name='cmd_vel_selector',
        arguments=['--ros-args', '--log-level', 'info'],

    )

    uart_bridge_node = Node(
        package='uart_bridge',
        executable='bridge',
        name='uart_bridge',
        output='screen',
        arguments=['--ros-args', '--log-level', 'info'],
        parameters=[{
            'port' : bridge_dev,
        }]
    )

    return LaunchDescription([
        controller_receiver_node,
        cmd_vel_pad_node,
        cmd_vel_selector_node,
        uart_bridge_node
    ])

