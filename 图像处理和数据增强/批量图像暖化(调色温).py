import cv2
import os
import numpy as np
import random

def increase_warmth(image, a_adjust, b_adjust):
    """
    增加图像的暖光效果，使其偏黄
    :param image: 输入图像
    :param a_adjust: 调整A通道的值
    :param b_adjust: 调整B通道的值
    :return: 增加暖光效果后的图像
    """
    # 将图像从BGR颜色空间转换为LAB颜色空间
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # 提取LAB图像中的L, A和B通道
    l, a, b = cv2.split(lab)

    # 调整A通道（控制红绿色）
    a = cv2.add(a, a_adjust)
    # 调整B通道（控制蓝黄色）
    b = cv2.add(b, b_adjust)

    # 将调整后的LAB图像合并
    lab = cv2.merge((l, a, b))

    # 将图像从LAB颜色空间转换回BGR
    warmed_image = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    
    return warmed_image

def process_images(input_dir, output_dir, a_adjust=20, b_adjust=30, prob=0.8):
    """
    批量处理图像，将冷色调图像转换为暖色调图像
    :param input_dir: 输入图像文件夹路径
    :param output_dir: 输出图像文件夹路径
    :param a_adjust: 调整A通道的值
    :param b_adjust: 调整B通道的值
    :param prob: 进行色调调整的概率
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            image_path = os.path.join(input_dir, filename)
            image = cv2.imread(image_path)
            if image is None:
                print(f"Failed to read {filename}. Skipping...")
                continue
            
            if random.random() < prob:
                # 以设定的概率进行色调调整
                warmed_image = increase_warmth(image, a_adjust, b_adjust)
                print(f"Processed {filename} with color adjustment")
            else:
                # 保持原样
                warmed_image = image
                print(f"Processed {filename} without color adjustment")
            
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, warmed_image)

# 设置输入和输出文件夹路径
input_dir = ' '  # 替换为冷色调图像的文件夹路径
output_dir = ' '  # 替换为保存暖色调图像的文件夹路径

# 设置调整参数
a_adjust = 1  # 调整A通道的值 red
b_adjust = 15  # 调整B通道的值 yellow

# 设置进行色调调整的概率
prob = 0.7

# 批量处理图像
process_images(input_dir, output_dir, a_adjust, b_adjust, prob)

"""
此脚本用于将给定文件夹中的冷色调图像批量转换为暖色调图像。脚本通过增加图像的红色和黄色通道值来实现暖化效果。图像的处理概率可设置，从而实现部分图像的处理。

参数说明:
1. `input_dir`: 输入图像文件夹路径。
2. `output_dir`: 输出图像文件夹路径。
3. `a_adjust`: 调整A通道（红色）的值。
4. `b_adjust`: 调整B通道（黄色）的值。
5. `prob`: 进行色调调整的概率。

使用方法:
1. 设置输入和输出文件夹路径，以及调整参数和概率。
2. 运行脚本，脚本会将符合条件的图像批量进行暖色调调整，并保存到指定的输出文件夹中。
"""
