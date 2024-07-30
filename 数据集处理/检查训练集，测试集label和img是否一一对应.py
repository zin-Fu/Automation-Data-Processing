"""
该脚本的功能是检查指定的图像和标签文件夹中，是否每张图像都有对应的标签文件，反之亦然。它适用于图像分类或目标检测等任务中，确保数据集的图像和标签一一对应。

参数和用法：
- train_images_folder: str, 训练集图像文件夹的路径。
- train_labels_folder: str, 训练集标签文件夹的路径。
- test_images_folder: str, 测试集图像文件夹的路径。
- test_labels_folder: str, 测试集标签文件夹的路径。

函数：
- check_correspondence(images_folder, labels_folder): 检查给定图像和标签文件夹中的文件对应关系。
  - 参数:
    - images_folder: str, 包含图像文件的文件夹路径。
    - labels_folder: str, 包含标签文件的文件夹路径。
  - 返回:
    - images_without_labels: list, 没有对应标签的图像文件名列表（不包含扩展名）。
    - labels_without_images: list, 没有对应图像的标签文件名列表（不包含扩展名）。

用法：
1. 设置训练集和测试集图像及标签文件夹的路径。
2. 调用check_correspondence函数检查对应关系。
3. 打印检查结果，显示没有对应标签的图像或没有对应图像的标签。

注意事项：
- 确保图像和标签文件夹中的文件名（不包含扩展名）一致。
- 标签文件应为.txt格式，图像文件支持.jpg, .png, .jpeg, .gif, .bmp等常见格式。
"""

import os

# 文件夹路径设置
train_images_folder = " "
train_labels_folder = " "
test_images_folder =  " "
test_labels_folder = " "

def check_correspondence(images_folder, labels_folder):
    # 获取所有图像文件名（不包含扩展名）
    image_files = [os.path.splitext(f)[0] for f in os.listdir(images_folder) if f.endswith(('.jpg', '.png', '.jpeg', '.gif', '.bmp'))]
    # 获取所有标签文件名（不包含扩展名）
    label_files = [os.path.splitext(f)[0] for f in os.listdir(labels_folder) if f.endswith('.txt')]
    
    # 检查是否每个图像都有对应的标签
    images_without_labels = [f for f in image_files if f not in label_files]
    # 检查是否每个标签都有对应的图像
    labels_without_images = [f for f in label_files if f not in image_files]
    
    return images_without_labels, labels_without_images

# 检查训练集
train_images_without_labels, train_labels_without_images = check_correspondence(train_images_folder, train_labels_folder)
# 检查测试集
test_images_without_labels, test_labels_without_images = check_correspondence(test_images_folder, test_labels_folder)

# 打印结果
if train_images_without_labels:
    print("训练集中以下图像没有对应的标签：")
    for img in train_images_without_labels:
        print(img)
else:
    print("训练集中所有图像都有对应的标签。")

if train_labels_without_images:
    print("训练集中以下标签没有对应的图像：")
    for lbl in train_labels_without_images:
        print(lbl)
else:
    print("训练集中所有标签都有对应的图像。")

if test_images_without_labels:
    print("测试集中以下图像没有对应的标签：")
    for img in test_images_without_labels:
        print(img)
else:
    print("测试集中所有图像都有对应的标签。")

if test_labels_without_images:
    print("测试集中以下标签没有对应的图像：")
    for lbl in test_labels_without_images:
        print(lbl)
else:
    print("测试集中所有标签都有对应的图像。")
