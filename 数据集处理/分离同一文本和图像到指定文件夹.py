import os
import shutil

def move_files(source_folder, txt_folder, img_folder):
    """
    将指定文件夹中的文件根据类型移动到不同的目标文件夹

    该函数遍历源文件夹中的所有文件，根据文件扩展名将文本文件和图片文件分别移动到指定的文件夹中。

    参数:
    source_folder (str): 源文件夹路径，包含要移动的文件
    txt_folder (str): 目标文件夹路径，用于存放文本文件 (.txt)
    img_folder (str): 目标文件夹路径，用于存放图片文件 (.jpg, .jpeg, .png, .gif)

    用法:
    - 设置 source_folder 为包含要移动文件的文件夹路径。
    - 设置 txt_folder 为目标文本文件夹的路径。
    - 设置 img_folder 为目标图片文件夹的路径。
    - 运行脚本，文件将根据类型被移动到相应的目标文件夹。
    """
    # 遍历源文件夹中的每一个文件
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # 判断文件类型
        if os.path.isfile(file_path):
            # 如果是txt文件，移动到txt文件夹
            if filename.lower().endswith('.txt'):
                shutil.move(file_path, os.path.join(txt_folder, filename))

            # 如果是图片文件，移动到img文件夹
            elif filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                shutil.move(file_path, os.path.join(img_folder, filename))

# 指定源文件夹路径、txt文件夹路径和img文件夹路径
source_folder = ' '
txt_folder = ' '
img_folder = ' '

# 调用函数移动文件
move_files(source_folder, txt_folder, img_folder)
