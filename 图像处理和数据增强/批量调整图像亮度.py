import os
import random
from PIL import Image, ImageEnhance

"""
批量调整图像亮度

功能概述:
    该脚本用于批量调整指定文件夹中所有图像的亮度。它使用 PIL 库打开图像并根据指定范围内的随机因子调整亮度，调整后的图像将保存到指定的输出目录。

主要功能:
    1. adjust_brightness: 调整单张图像的亮度。
    2. process_dataset: 批量处理文件夹中的图像，调整亮度并保存。

使用方法:
    1. 设置 input_directory 为输入图像文件夹路径。
    2. 设置 output_directory 为保存调整后图像的文件夹路径。
    3. 设置 brightness_factor_range 为调整亮度的范围。
    4. 运行脚本，处理结果将保存到输出文件夹。

函数说明:
    adjust_brightness(image_path, output_path, factor_range):
        - image_path: str，输入图像的路径。
        - output_path: str，保存调整后图像的路径。
        - factor_range: tuple，调整亮度的范围，例如(0.8, 1.2)表示亮度调整因子将在0.8到1.2之间随机选择。

    process_dataset(input_dir, output_dir, factor_range):
        - input_dir: str，包含输入图像的目录路径。
        - output_dir: str，保存调整后图像的目录路径。
        - factor_range: tuple，调整亮度的范围。

"""

def adjust_brightness(image_path, output_path, factor_range=(0.8, 1.2)):
    """
    调整图像的亮度，通过给定范围内的随机因子。
    
    :param image_path: str, 输入图像的路径
    :param output_path: str, 保存调整后图像的路径
    :param factor_range: tuple, 调整亮度的因子范围
    """
    image = Image.open(image_path)
    enhancer = ImageEnhance.Brightness(image)
    factor = random.uniform(*factor_range)
    enhanced_image = enhancer.enhance(factor)
    enhanced_image.save(output_path)

def process_dataset(input_dir, output_dir, factor_range=(0.8, 1.2)):
    """
    处理给定目录中的所有图像，调整它们的亮度，并将调整后的图像保存到输出目录。
    
    :param input_dir: str, 包含输入图像的目录路径
    :param output_dir: str, 保存调整后图像的目录路径
    :param factor_range: tuple, 调整亮度的因子范围
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            adjust_brightness(input_path, output_path, factor_range)
            print(f"Adjusted brightness of {filename}")

if __name__ == "__main__":
    input_directory = " "
    output_directory = " "
    brightness_factor_range = (0.8, 1.2)  # 可调整的亮度范围

    process_dataset(input_directory, output_directory, brightness_factor_range)
