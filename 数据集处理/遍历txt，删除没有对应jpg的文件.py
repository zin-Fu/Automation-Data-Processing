import os
import glob

# 标签和图片文件夹路径
labels_folder = " "
images_folder = " "

# 定义支持的图片文件类型
image_file_types = ['.jpg', '.png', '.jpeg', '.gif', '.bmp']

# 获取labels文件夹中所有的.txt文件
label_files = os.listdir(labels_folder)
label_files = [file for file in label_files if file.endswith(".txt")]

# 遍历每一个.txt文件
for label_file in label_files:
    # 提取.txt文件的文件名（不包含扩展名）
    file_name = os.path.splitext(label_file)[0]
    
    # 初始化一个标志，用于检查是否找到对应的图片文件
    image_exists = False
    
    # 遍历所有的图片文件类型
    for image_type in image_file_types:
        # 构建对应的图片文件路径
        image_file = os.path.join(images_folder, file_name + image_type)
        
        # 检查图片文件是否存在
        if os.path.exists(image_file):
            image_exists = True
            break
    
    # 如果没有找到对应的图片文件，删除对应的.txt文件
    if not image_exists:
        label_path = os.path.join(labels_folder, label_file)
        os.remove(label_path)
        print(f"Deleted {label_file}")

"""
此脚本的功能是遍历指定文件夹中的所有标签文件（.txt格式），并检查是否存在对应的图片文件（支持的图片格式有.jpg, .png, .jpeg, .gif, .bmp）。如果标签文件没有对应的图片文件，则删除该标签文件。

参数:
labels_folder (str): 包含标签文件的文件夹路径。
images_folder (str): 包含图片文件的文件夹路径。

用法:
1. 将标签文件和图片文件放置在各自对应的文件夹中。
2. 修改labels_folder和images_folder变量为实际文件夹路径。
3. 运行此脚本，脚本会删除所有没有对应图片文件的标签文件。

注意:
请确保在运行脚本前备份好重要文件，因为删除操作不可逆。
"""
