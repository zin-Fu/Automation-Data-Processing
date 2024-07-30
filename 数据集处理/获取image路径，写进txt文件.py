"""
该脚本的功能是从指定文件夹中获取所有图片文件的文件名，并将每个文件的路径写入一个名为image.txt的文件中。
生成的txt文件每一行包含一个图片的完整路径，用于后续的批量处理或记录。

参数和用法：
- folder_path: str, 指定的文件夹路径，包含待处理的图片文件。

用法：
1. 将folder_path变量设置为包含图片的文件夹路径。
2. 运行脚本后，将在指定的文件夹中生成一个名为image.txt的文件。
3. image.txt文件中的每一行都包含一个图片文件的路径。

注意事项：
- 请确保folder_path变量设置的路径正确，并且文件夹中包含图片文件。
- 此脚本只会处理指定文件夹中的.jpg, .jpeg, .png, .gif格式的图片。
- 生成的image.txt文件将覆盖文件夹中已存在的同名文件，请注意数据备份。
"""

import os

def create_image_txt(folder_path):
    # 获取文件夹中所有图片的文件名
    image_names = [file for file in os.listdir(folder_path) if file.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    # 创建或覆盖image.txt文件
    with open(os.path.join(folder_path, 'image.txt'), 'w') as file:
        # 遍历每张图片，写入txt文件
        for image_name in image_names:
            file.write(f"/home/zllcdl/lzz/Competition/Detect_Road/ALL/{image_name}\n")

    print("image.txt文件已成功创建。")

# 指定文件夹路径
folder_path = " "

# 调用函数创建image.txt文件
create_image_txt(folder_path)
