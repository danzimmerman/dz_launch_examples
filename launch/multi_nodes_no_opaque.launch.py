import launch
import launch_ros
import sys

def generate_launch_description():
    """
    """
    
    declared_args = []

    declared_args.append(
        launch.actions.DeclareLaunchArgument(
            "num_node_pairs",
            default_value="1",
        )
    )

    context = launch.LaunchContext(argv=sys.argv)
    print("==== context.launch_configurations: ")
    print(context.launch_configurations) #<--- note this is empty

    N_lc = launch.substitutions.LaunchConfiguration("num_node_pairs")
    N = int(N_lc.perform(context))

    message = launch.actions.LogInfo(msg=f"I will launch {N} nodes")

    return launch.LaunchDescription(declared_args + [context, message])

