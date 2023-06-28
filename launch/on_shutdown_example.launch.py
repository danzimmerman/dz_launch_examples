# from https://robotics.stackexchange.com/questions/24908/how-to-execute-a-script-at-shutdown-of-a-launch-process
# looking into https://github.com/ros2/launch/issues/263 as well 

import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess, LogInfo, RegisterEventHandler
from launch.event_handlers import OnShutdown
from launch_ros.actions import Node
from launch.substitutions import LocalSubstitution


def shutdown_func_with_echo_side_effect(event, context):
    os.system('echo [os.system()] Shutdown callback function can echo this way.')
    return [
        LogInfo(msg='Shutdown callback was called for reason "{}"'.format(event.reason)),
        ExecuteProcess(cmd=['echo However, this echo will fail without shell=True.'], shell=True)]
    
def generate_launch_description():

    talker_node = Node(
            package='demo_nodes_cpp',
            executable='talker',
            name='demo_talker',
        )
    
    talker_node_2 = Node(
            package='demo_nodes_cpp',
            executable='talker',
            name='demo_talker_post_shutdown',
        )
    
    
    ld = LaunchDescription([
        talker_node,
        ExecuteProcess(cmd=['echo blah'], shell=True, output='both'),
        RegisterEventHandler(
            OnShutdown(on_shutdown=shutdown_func_with_echo_side_effect)
        )
    ])

    return ld