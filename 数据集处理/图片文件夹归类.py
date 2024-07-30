import os
import shutil
import re

def classify_images(base_folder):
    """
    这个脚本用于将一个基文件夹中的多个子文件夹按照规则进行归类，将相同类型的图片文件移动到一个新的归类文件夹中。
    主要功能是通过去除子文件夹名称末尾的数字来归类子文件夹，将相同类型的图片文件集中存储。

    参数和用法：
    - base_folder: str, 基础文件夹的路径，包含若干个子文件夹。这些子文件夹的名称可能以不同的数字结尾。
      函数首先扫描基础文件夹中的所有子文件夹，并去掉子文件夹名称末尾的数字来归类。
      如果存在多个属于同一类别的子文件夹，它们的图片文件将被移动到一个新的归类文件夹中。新的归类文件夹以去掉数字后的名称命名。

    注意事项：
    - 运行前，请确保 base_folder 路径正确，以避免误操作。
    - 移动操作会修改文件的原始存储位置，请谨慎操作，避免数据丢失。
    - 脚本仅处理图片文件（扩展名为 .png, .jpg, .jpeg, .bmp, .gif 的文件）。
    """
    # 获取子文件夹列表
    subfolders = [f.path for f in os.scandir(base_folder) if f.is_dir()]
    
    # 创建一个字典用于存储归类后的文件夹名和其对应的原始子文件夹列表
    classified_folders = {}

    for subfolder in subfolders:
        # 获取子文件夹名称
        subfolder_name = os.path.basename(subfolder)
        
        # 去掉最后一个数字的文件夹名称
        classified_name = re.sub(r'\d+$', '', subfolder_name)
        
        if classified_name not in classified_folders:
            classified_folders[classified_name] = []
        
        classified_folders[classified_name].append(subfolder)

    # 遍历归类后的文件夹名，创建新文件夹并移动图片
    for classified_name, folders in classified_folders.items():
        if len(folders) > 1:
            # 创建归类的文件夹
            classified_folder_path = os.path.join(base_folder, classified_name)
            os.makedirs(classified_folder_path, exist_ok=True)
            
            for folder in folders:
                for filename in os.listdir(folder):
                    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                        # 移动图片文件到归类文件夹
                        src_file = os.path.join(folder, filename)
                        dest_file = os.path.join(classified_folder_path, filename)
                        shutil.move(src_file, dest_file)
                        print(f"Moved {src_file} to {dest_file}")

# 示例用法
base_folder = " "  # 替换为包含子文件夹的基础文件夹路径

classify_images(base_folder)
