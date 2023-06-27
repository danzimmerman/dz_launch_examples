import launch
import launch_ros
import sys

# def prepare_multiple_nodes(context, *args, **kwargs):
#     """
    
#     """
#     N_lc = launch.substitutions.LaunchConfiguration("num_node_pairs")
#     N = int(N_lc.perform(context))

#     nodes = []

#     if N<1 or N>5:
#         message = launch.actions.LogInfo(
#             msg="ERROR: Number of launched node pairs must be between 1 and 5, not launching any."
#         )
#     else:
#         message = launch.actions.LogInfo(msg=f"Starting {N} node pairs.")
#         for i in range(0, N):
#             # launch N talkers in distinct namespaces
#             nodes.append(
#                 launch_ros.actions.Node(
#                     package="demo_nodes_cpp", 
#                     executable="talker", 
#                     output="screen",
#                     namespace=f"ns{i}"
#                 )
#             )
#             # launch N listeners in distinct namespaces
#             nodes.append(
#                 launch_ros.actions.Node(
#                     package="demo_nodes_cpp", 
#                     executable="listener", 
#                     output="screen",
#                     namespace=f"ns{i}"
#                 )
#             )
    
#     return nodes + [message]

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

    return launch.LaunchDescription(declared_args + [message])

