# Copyright (c) 2022，Horizon Robotics.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 启动图片发布pkg
        Node(
            package='mipi_cam',
            executable='mipi_cam',
            output='screen',
            parameters=[
                {"out_format": "nv12"},
                {"image_width": 1920},
                {"image_height": 1080},
                {"io_method": "shared_mem"},
                {"video_device": "IMX415"}
            ],
            arguments=['--ros-args', '--log-level', 'error']
        ),
        # 启动HDMI图像显示pkg
        Node(
            package='hobot_hdmi',
            executable='hobot_hdmi',
            output='screen',
            parameters=[
                {"io_method": "shared_mem"},
                {"sub_img_topic": "/hbmem_img"},
            ],
            arguments=['--ros-args', '--log-level', 'error']
        ),
    ])