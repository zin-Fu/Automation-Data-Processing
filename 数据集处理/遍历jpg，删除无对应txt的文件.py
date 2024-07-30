"""
此脚本的功能是遍历指定文件夹中的所有图片文件，并检查每个图片文件是否有对应的标签文件（.txt格式）。如果图片文件没有对应的标签文件，则删除该图片文件。

参数:
- labels_folder (str): 包含标签文件的文件夹路径。标签文件通常是描述图片内容的文本文件。
- images_folder (str): 包含图片文件的文件夹路径。支持的图片格式包括JPG、PNG、JPEG、GIF和BMP。

用法:
1. 将标签文件和图片文件分别放置在labels_folder和images_folder对应的文件夹中。
2. 修改脚本中labels_folder和images_folder变量的值为实际文件夹路径。
3. 运行此脚本。脚本会遍历images_folder中的所有图片文件，如果图片文件没有对应的标签文件，则删除该图片文件。

注意事项:
- 请确保在运行此脚本前备份好重要的图片文件，因为删除操作是不可逆的。
- 该脚本依赖于图片文件名和标签文件名之间的匹配关系：即图片文件名去掉扩展名后，应与标签文件名去掉扩展名后的部分一致。

示例:
- 假设images_folder中有图片文件'cat.jpg'，那么脚本会检查labels_folder中是否有名为'cat.txt'的标签文件。
- 如果没有找到'cat.txt'，则删除'cat.jpg'。

代码逻辑:
1. 遍历images_folder中所有指定类型的图片文件。
2. 对每个图片文件，提取其文件名，并在labels_folder中检查是否存在相应的标签文件。
3. 如果没有找到对应的标签文件，则删除该图片文件。
"""

import os
import glob

# 标签和图片文件夹路径
labels_folder = " "  # 替换为实际标签文件夹路径
images_folder = " "  # 替换为实际图片文件夹路径

# 定义图片文件的类型
image_file_types = ['*.jpg', '*.png', '*.jpeg', '*.gif', '*.bmp']

# 收集所有图片文件路径
image_files = []
for file_type in image_file_types:
    # 遍历文件夹中的所有图片文件
    for img_file in glob.glob(os.path.join(images_folder, file_type)):
        image_files.append(img_file)

# 遍历每一个图片文件
for image_file in image_files:
    # 提取图片文件的文件名（不包含扩展名）
    file_name = os.path.splitext(os.path.basename(image_file))[0]

    # 构建对应的.txt文件路径
    label_file = os.path.join(labels_folder, file_name + ".txt")

    # 检查.txt文件是否存在
    if not os.path.exists(label_file):
        # .txt文件不存在，删除对应的图片文件
        os.remove(image_file)
        print(f"Deleted {image_file}")
