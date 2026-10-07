# ROS2 海龟画方框（turtle_square）

基于 ROS2 Humble 编写的 turtlesim 海龟控制节点，让海龟循环画出方框，
并演示 ROS2 的发布/订阅、参数、launch 等核心概念。

## 环境要求

- Ubuntu 22.04
- ROS2 Humble

## 功能说明

| 程序 | 作用 |
|------|------|
| `draw_square` | 控制海龟交替"走直线 / 转 90°"，循环画出方框 |
| `pose_bridge` | 把海龟位姿转换为 RViz2 可显示的 PoseStamped 消息 |

`draw_square` 节点带一个参数 `speed`（前进速度），可在运行时用
`ros2 param set` 实时调整，无需重新编译。

## 编译

```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
运行
方式一：分别启动

bash

ros2 run turtlesim turtlesim_node
ros2 run turtle_square draw_square
方式二：launch 一键启动（海龟 + 画方框 + 默认速度一起拉起）

bash

ros2 launch turtle_square draw_square.launch.py
目录结构
plaintext

ros2_ws/
└── src/
    └── turtle_square/
        ├── turtle_square/
        │   ├── draw_square.py
        │   └── pose_bridge.py
        ├── launch/
        │   └── draw_square.launch.py
        ├── package.xml
        └── setup.py
