"""
数据增强图像处理工具

此脚本用于对图像进行多种数据增强处理，如翻转、旋转、添加噪声、高斯模糊、光照调整、仿射变换、平移、随机移动、随机旋转和随机缩放。
用户可以选择需要的增强技术，并对指定文件夹中的所有图像进行批量处理。

功能:
- 提供多种数据增强技术
- 支持用户选择需要的增强技术
- 批量处理指定文件夹中的所有图像

参数:
- input_path (str): 输入图像文件夹路径
- techniques (list): 用户选择的数据增强技术列表

增强技术编号:
1. Flip（翻转）
2. Rotate（旋转）
3. Noise（噪声）
4. Gaussian blur（高斯模糊）
5. Lighting（光照调整）
6. Affine transformation（仿射变换）
7. Translation（平移）
8. Random shift（随机移动）
9. Random rotation（随机旋转）
10. Random zoom（随机缩放）

用法:
1. 将需要处理的图像放置在指定文件夹中。
2. 运行脚本，输入图像文件夹路径。
3. 选择需要的增强技术，多个技术之间用逗号分隔。
4. 脚本会在同一文件夹中保存增强后的图像，文件名会附加"_aug"和序号。

注意事项:
- 请确保图像文件夹路径的正确性。
- 增强后的图像会覆盖在原文件夹中，建议备份原始图像。
- 处理时间可能会根据图像数量和选择的增强技术有所不同。

示例:
假设input_path为"D:\\images"，选择1, 2, 3增强技术，则脚本会处理该文件夹中的所有.jpg图像，并保存增强后的图像。
"""

import numpy as np
import os
import cv2
import glob
import random

def random_shift(image, max_shift=20):
    """随机小范围移动图像"""
    rows, cols, _ = image.shape
    dx, dy = random.randint(-max_shift, max_shift), random.randint(-max_shift, max_shift)
    M = np.float32([[1, 0, dx], [0, 1, dy]])
    shifted_image = cv2.warpAffine(image, M, (cols, rows))
    return shifted_image

def random_rotation(image, max_angle=15):
    """随机从-15°到15°之间旋转图像"""
    rows, cols, _ = image.shape
    angle = random.uniform(-max_angle, max_angle)
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    rotated_image = cv2.warpAffine(image, M, (cols, rows))
    return rotated_image

def random_zoom(image, min_zoom=0.8, max_zoom=1.2):
    """小范围放大和缩小图像"""
    rows, cols, _ = image.shape
    zoom_factor = random.uniform(min_zoom, max_zoom)
    M = cv2.getRotationMatrix2D((cols/2, rows/2), 0, zoom_factor)
    zoomed_image = cv2.warpAffine(image, M, (cols, rows))
    return zoomed_image

def data_augmentation(img, techniques):
    img_list = []
    
    if '1' in techniques:
        # Flip
        img_list.append(cv2.flip(img, 1))  # Horizontal flip
        img_list.append(cv2.flip(img, 0))  # Vertical flip
        img_list.append(cv2.flip(img, -1)) # Horizontal and vertical flip
    
    if '2' in techniques:
        # Rotate
        scale = 1.0
        rows, cols = img.shape[:2]
        center = (cols / 2, rows / 2)  # Image center
        angle = [45, 315]
        for a in angle:
            M = cv2.getRotationMatrix2D(center, a, scale)
            rotated = cv2.warpAffine(img, M, (cols, rows), borderValue=(255, 255, 255))
            img_list.append(rotated)
    
    if '3' in techniques:
        # Noise
        noise_img = img.copy()
        for _ in range(1500):
            noise_img[random.randint(0, noise_img.shape[0] - 1)][random.randint(0, noise_img.shape[1] - 1)][:] = 255
        img_list.append(noise_img)
    
    if '4' in techniques:
        # Gaussian blur
        blur1 = cv2.GaussianBlur(img, (9, 9), 1.5)
        blur2 = cv2.blur(img, (11, 11), (-1, -1))
        img_list.append(blur1)
        img_list.append(blur2)
    
    if '5' in techniques:
        # Lighting
        contrast = 1       # Contrast
        brightness = 100   # Brightness
        light1 = cv2.addWeighted(img, contrast, img, 0, brightness)
        light2 = cv2.addWeighted(img, 1.5, img, 0, 50)
        img_list.append(light1)
        img_list.append(light2)
    
    if '6' in techniques:
        # Affine transformation
        rows, cols = img.shape[:2]
        point1 = np.float32([[50, 50], [300, 50], [50, 200]])
        point2 = np.float32([[10, 100], [300, 50], [100, 250]])
        M = cv2.getAffineTransform(point1, point2)
        affine = cv2.warpAffine(img, M, (cols, rows), borderValue=(255, 255, 255))
        img_list.append(affine)
    
    if '7' in techniques:
        # Translation
        M = np.array([[1, 0, -100], [0, 1, -50]], dtype=np.float32)
        translated = cv2.warpAffine(img, M, (cols, rows))
        img_list.append(translated)
    
    # New techniques
    if '8' in techniques:
        # Random shift
        img_list.append(random_shift(img))
    
    if '9' in techniques:
        # Random rotation
        img_list.append(random_rotation(img))
    
    if '10' in techniques:
        # Random zoom
        img_list.append(random_zoom(img))
    
    return img_list

if __name__ == '__main__':
    input_path = input("Please enter the image path: ")
    print("Please select the data augmentation techniques you want to use, separated by commas: ")
    print("1: Flip")
    print("2: Rotate")
    print("3: Noise")
    print("4: Gaussian blur")
    print("5: Lighting")
    print("6: Affine transformation")
    print("7: Translation")
    print("8: Random shift")
    print("9: Random rotation")
    print("10: Random zoom")
    techniques = input().split(',')
    
    for img_path in glob.glob(os.path.join(input_path, '*.jpg')):
        img = cv2.imread(img_path)
        augmented_images = data_augmentation(img, techniques)
        
        img_name = os.path.basename(img_path).split('.')[0]
        save_dir = os.path.dirname(img_path)
        
        for i, aug_img in enumerate(augmented_images):
            save_path = os.path.join(save_dir, f"{img_name}_aug{i}.jpg")
            cv2.imwrite(save_path, aug_img)
            print(f"Saved augmented image: {save_path}")
