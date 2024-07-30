import os
import shutil

def copy_matching_txt_files(image_folder, txt_folder, output_folder):
    """
    复制图片文件夹中对应的文本文件到指定输出文件夹。

    功能：
    该函数会遍历指定的图片文件夹，对于每一个图片文件，查找txt文件夹中是否存在同名的文本文件（.txt格式）。
    如果找到对应的文本文件，则将其复制到指定的输出文件夹中。

    参数：
    :param image_folder: str, 图片文件夹路径，包含待匹配的图片文件。
    :param txt_folder: str, txt文件夹路径，包含所有的文本文件。
    :param output_folder: str, 输出文件夹路径，用于存放匹配的文本文件。

    注意事项：
    - 确保输出文件夹存在或可以创建，以避免复制文件失败。
    - 图片文件的扩展名可以是.png, .jpg, .jpeg, .bmp, .gif等。
    - 确保文件夹路径正确，以免操作错误文件。
    """
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 遍历图片文件夹中的每一张图片
    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # 获取图片文件名（不含扩展名）
            base_name = os.path.splitext(filename)[0]
            # 构造同名的txt文件路径
            txt_file = os.path.join(txt_folder, base_name + '.txt')
            
            if os.path.exists(txt_file):
                # 复制txt文件到输出文件夹
                shutil.copy(txt_file, output_folder)
                print(f"Copied {txt_file} to {output_folder}")
            else:
                print(f"Text file {txt_file} does not exist")

# 示例用法
image_folder = 'path/to/image/folder'  # 替换为图片文件夹路径
txt_folder = 'path/to/txt/folder'      # 替换为txt文件夹路径
output_folder = 'path/to/output/folder'  # 替换为输出文件夹路径

copy_matching_txt_files(image_folder, txt_folder, output_folder)
