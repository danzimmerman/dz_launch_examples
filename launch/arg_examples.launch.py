# Python launch XML argument declaration examples 

import launch
import launch_ros
launch.frontend
import os

def launch_value_logger(context, *args, **kwargs):
    """
    This Python implementation also shows how to introspect the launch context in
    an OpaqueFunction and how to use launch.actions.LogInfo to log
    messages from a launch file.
    """
    info_log_items = []

    #we can get the absolute path to this launch file. I just want the filename, so I use os.path.sep
    launch_fn = launch.substitutions.ThisLaunchFile().perform(context).split(os.path.sep)[-1]

    info_log_items.append(launch.actions.LogInfo(
        msg=f"\n\n===== {launch_fn} Launch Configuration Values =====")
    )
    
    # The launch context has a dict called .launch_configurations that contains the names 
    # and contextual values of the launch file's LaunchConfiguration objects.
    for argname, argval in context.launch_configurations.items():
        arg_message = f"'{argname}' has a value of {argval}"
        info_log_items.append(launch.actions.LogInfo(msg=arg_message))

    return info_log_items


def generate_launch_description():
    
    declared_args = []
    declared_args.append(
        launch.actions.DeclareLaunchArgument(
            "simple_arg" # Just a name. This arg will be REQUIRED at the command line.
        )
    )

    declared_args.append(
        launch.actions.DeclareLaunchArgument(
            "arg_with_default", 
            default_value="1234"
        )
    )

    declared_args.append(
        launch.actions.DeclareLaunchArgument(
            "arg_with_default_and_description", 
            default_value="some_string_arg_value", 
            description="This argument is used to..."
        )
    )

    declared_args.append(
        launch.actions.DeclareLaunchArgument(
            "arg_with_choices",
            default_value="choice_1",
            description="An argument with several validated choices, defaulting to choice_1.",
            choices=[
                "choice_1", 
                "choice_2", 
                "choice_3",
            ]
        )
    )

    share = launch_ros.substitutions.FindPackageShare(package="dz_launch_examples")
    declared_args.append(
        launch.actions.DeclareLaunchArgument(
            "file_in_package_arg",
            default_value=launch.substitutions.PathJoinSubstitution(
                [share] + "launch/arg_examples.launch.py".split("/") #I really hate this, there must be a way we can use the frontend to do this well in Python
            )
        )
    )

    return launch.LaunchDescription(declared_args + [launch.actions.OpaqueFunction(function=launch_value_logger)])