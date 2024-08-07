"""
该脚本用于将一个文件夹中的图像和对应的标签文件按指定比例划分为训练集和测试集。
功能包括：
1. 确保每个图像文件都有对应的标签文件，并删除没有匹配的文件。
2. 按照指定比例将图像和标签文件随机划分为训练集和测试集。
3. 将划分后的文件复制到相应的训练集和测试集文件夹中。

参数和用法：
- labels_folder: str, 标签文件的文件夹路径。此文件夹应包含.txt格式的标签文件。
- images_folder: str, 图像文件的文件夹路径。此文件夹应包含.jpg或.png格式的图像文件。
- train_images_folder: str, 训练集图像文件存放的文件夹路径。
- train_labels_folder: str, 训练集标签文件存放的文件夹路径。
- test_images_folder: str, 测试集图像文件存放的文件夹路径。
- test_labels_folder: str, 测试集标签文件存放的文件夹路径。
- split_ratio: float, 训练集和测试集的划分比例。0.8表示80%的数据用于训练，20%用于测试。

注意事项：
- 请确保输入的图像文件和标签文件具有相同的文件名（扩展名除外），并且都存在于指定的文件夹中。
- 删除没有匹配的图像或标签文件时请谨慎操作，避免数据丢失。
- 运行前请确保文件夹路径和权限设置正确。
"""
import os
import shutil
import random

labels_folder = " "
images_folder = " "

train_images_folder = " "
train_labels_folder = " "
test_images_folder = " "
test_labels_folder = " "

if not os.path.exists(train_images_folder):
    os.makedirs(train_images_folder)
if not os.path.exists(train_labels_folder):
    os.makedirs(train_labels_folder)
if not os.path.exists(test_images_folder):
    os.makedirs(test_images_folder)
if not os.path.exists(test_labels_folder):
    os.makedirs(test_labels_folder)

split_ratio = 0.8  # Change this to your desired ratio

image_files = [f for f in os.listdir(images_folder) if any(f.endswith(ext) for ext in ['.jpg', '.png'])]
label_files = [f for f in os.listdir(labels_folder) if f.endswith('.txt')]

# assert set(f[:-4] for f in image_files) == set(f[:-4] for f in label_files)
# 遍历每一个图片文件，提取文件名（不包含扩展名），构建对应的.txt文件路径，检查.txt文件是否存在
for image_file in image_files:
    file_name = os.path.splitext(os.path.basename(image_file))[0]
    label_file = os.path.join(labels_folder, file_name + ".txt")
    if not os.path.exists(label_file):
        os.remove(os.path.join(images_folder, image_file))
        image_files.remove(image_file)
        print(f"Deleted {image_file}")
        print(f"{image_file} has no corresponding label file")

# 遍历每一个.txt文件，提取.txt文件的文件名（不包含扩展名），构建对应的图片文件路径，检查图片文件是否存在
for label_file in label_files:
    file_name = os.path.splitext(label_file)[0]
    image_file = os.path.join(images_folder, file_name + ".jpg")
    if not os.path.exists(image_file):
        os.remove(os.path.join(labels_folder, label_file))
        label_files.remove(label_file)
        print(f"Deleted {label_file}")
        print(f"{label_file} has no corresponding image file")

assert set(f[:-4] for f in image_files) == set(f[:-4] for f in label_files)
# Shuffle file list
random.shuffle(image_files)

# Split the files into training set and test set based on the specified ratio
num_train = int(len(image_files) * split_ratio)
train_files = image_files[:num_train]
test_files = image_files[num_train:]

# Copy the files to the corresponding folders
for file in train_files:
    shutil.copy(os.path.join(images_folder, file), train_images_folder)
    shutil.copy(os.path.join(labels_folder, file[:-4] + '.txt'), train_labels_folder)

for file in test_files:
    shutil.copy(os.path.join(images_folder, file), test_images_folder)
    shutil.copy(os.path.join(labels_folder, file[:-4] + '.txt'), test_labels_folder)
