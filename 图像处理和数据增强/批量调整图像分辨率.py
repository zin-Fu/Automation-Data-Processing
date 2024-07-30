from PIL import Image
import os

"""
批量调整图像分辨率

功能概述:
    脚本遍历指定文件夹中的每个图像文件，检查图像的当前分辨率是否符合目标分辨率。如果不符合，则调整其分辨率并保存；如果符合，则跳过该图像。

变量解释:
    folder_path: 指定要处理的图像文件夹路径，用户需替换为实际的文件夹路径。
    target_resolution: 目标分辨率，格式为 (width, height)，表示宽度和高度的像素值。

处理步骤:
    1. 遍历文件夹中的每个文件，检查其是否为文件（忽略文件夹）。
    2. 尝试使用 PIL 库打开图像文件。
    3. 获取图像的当前分辨率。
    4. 如果当前分辨率不等于目标分辨率，则调整图像大小为目标分辨率并保存。
    5. 如果分辨率已符合目标值，则跳过该图像。
    6. 处理过程中如遇错误，捕获并输出错误信息。

使用说明:
    1. 修改 folder_path 为实际的图像文件夹路径。
    2. 设置 target_resolution 为所需的目标分辨率。
    3. 运行脚本，即可自动调整文件夹中所有图像的分辨率。
"""

# 设置文件夹路径和目标分辨率
folder_path = "your_folder_path"  # 替换为你的文件夹路径
target_resolution = (320, 240)

# 遍历文件夹中的文件
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        try:
            # 打开图像文件
            image = Image.open(file_path)

            # 获取当前分辨率
            current_resolution = image.size

            # 调整分辨率
            if current_resolution != target_resolution:
                resized_image = image.resize(target_resolution)
                resized_image.save(file_path)
                print(f"调整分辨率成功：{filename}")
            else:
                print(f"分辨率已符合要求：{filename}")

        except Exception as e:
            print(f"处理文件出错：{filename}，错误信息：{e}")
