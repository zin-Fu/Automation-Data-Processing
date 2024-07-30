import os
import glob

def rename_images(directory, name):
    """
    批量重命名指定目录中的所有图片文件。

    功能：
    该脚本会遍历指定目录中的所有图片文件，并按照指定的格式重命名每个文件。新文件名由指定的前缀和序号组成，保留原有的文件扩展名。

    参数：
    - directory: str, 包含图片文件的目录路径。
    - name: str, 重命名时使用的文件名前缀。

    用法：
    1. 将图片文件存放在一个文件夹中。
    2. 运行脚本时，输入文件夹的路径和新的文件名前缀。
    3. 脚本会自动重命名文件夹中的所有图片文件，并打印重命名信息。

    注意事项：
    - 脚本支持的图片格式包括：jpg, jpeg, png。其他格式的文件不会被处理。
    - 重命名后的文件会覆盖同名文件，请确保不会覆盖重要文件。
    - 在运行脚本前，请备份重要文件，以防意外丢失。
    """
    # 获取目录中的所有图片文件
    images = glob.glob(os.path.join(directory, "*.[pjJ][npNP][gG]*"))
    # 对每个图片文件进行重命名
    for i, image in enumerate(images, start=1):
        # 获取文件的扩展名
        extension = os.path.splitext(image)[1]
        # 创建新的文件名
        new_name = f"{name}_{i}{extension}"
        # 创建新的文件路径
        new_path = os.path.join(directory, new_name)
        # 重命名文件
        os.rename(image, new_path)
        print(f"Renamed {image} to {new_path}")

if __name__ == "__main__":
    directory = input("Enter the directory containing images: ")
    name = input("Enter the new name for images: ")
    rename_images(directory, name)
