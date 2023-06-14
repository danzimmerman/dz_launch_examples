# dz_launch_examples

Some examples of ROS 2 launch files in Python, XML, and YAML.

## Argument declaration examples

The launch files `arg_examples.launch.py`, `arg_examples.launch.xml`, and `arg_examples.launch.yaml` show off some features
of argument declaration.

These were developed to try to understand https://github.com/ros2/launch/issues/698

They simply declare and print a set of arguments. 

Run (with `.py`, `.xml`, or, `yaml` in place of `<extension>`):

```
ros2 launch dz_launch_examples arg_examples.launch.<extension> simple_arg:=<some value>
```

The Python version also demonstrates:
 - Iteration over a launch context's configuration to get the names and values of 
declared launch arguments
 - Use of `launch.actions.LogInfo` to log information from the log file.

To see the declared arguments and their descriptions and valid choices, run:

```
ros2 launch dz_launch_examples arg_examples.launch.<extension> --show-args
```

## Node preparation in Python `OpaqueFunction`

This provides an example of returning several talker/listener node pairs in consecutively numbered namespaces, inspired by [this post](https://answers.ros.org/question/416438/adding-node-from-within-opaquefunction-in-ros2-python-launch-file/).

To launch three node pairs, for example, run:

```
ros2 launch dz_launch_examples opaque_multi_nodes.launch.py num_node_pairs:=3
```





