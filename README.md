# ERC 2022 ArUco Checker

## Service

Checking service is advertised under `/erc_aruco_score`. It is defined in the `erc_aruco_checker` package (available [here](https://github.com/filesmuggler/erc_aruco_checker)). The request message type is of `ErcAruco`.
It is defined in the `erc_aruco_msg` package as 14 float32 arrays of 3 numbers, which correspond to 14 tag positions (tags from 1 to 14). On the scene. The returned type is a single float32 value with your obtained score. The tag placed inside the box on the panel is not taken into account.

## Test
If you want to test your solution against the checker, you can clone the [repository](https://github.com/filesmuggler/erc_aruco_checker) which consists of the checker node, config files and launch file with parameters. 

