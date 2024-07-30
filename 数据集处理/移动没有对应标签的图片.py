import os
import shutil

def move_images_without_txt(source_folder, destination_folder):
    """
    将源文件夹中没有对应.txt标签文件的.jpg图片文件移动到目标文件夹。

    功能：
    该函数会遍历指定的源文件夹，查找所有的.jpg图片文件并检查是否有相应的.txt标签文件。如果没有对应的.txt文件，
    则将这些图片文件移动到指定的目标文件夹中。

    参数：
    :param source_folder: str, 源文件夹路径，包含.jpg图片和.txt标签文件。
    :param destination_folder: str, 目标文件夹路径，用于存放没有对应标签文件的图片文件。

    注意事项：
    - 确保目标文件夹存在或可以创建，以避免移动文件失败。
    - 该操作将物理移动文件，请确保文件不再需要在原位置使用。
    """
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # 获取所有.jpg和.txt文件的文件名（不包括扩展名）
    jpg_files = [f[:-4] for f in os.listdir(source_folder) if f.endswith('.jpg')]
    txt_files = [f[:-4] for f in os.listdir(source_folder) if f.endswith('.txt')]

    # 找出没有对应.txt文件的.jpg文件
    images_without_txt = [f for f in jpg_files if f not in txt_files]

    # 移动这些.jpg文件到指定的目标文件夹
    for image in images_without_txt:
        src_path = os.path.join(source_folder, image + '.jpg')
        dest_path = os.path.join(destination_folder, image + '.jpg')
        shutil.move(src_path, dest_path)
        print(f"Moved {src_path} to {dest_path}")

if __name__ == "__main__":
    source_folder = ' '  # 替换为你的源文件夹路径
    destination_folder = ' '  # 替换为你的目标文件夹路径

    move_images_without_txt(source_folder, destination_folder)
