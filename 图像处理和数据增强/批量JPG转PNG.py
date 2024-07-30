from PIL import Image
import os

# 指定文件夹路径
folder_path = ' '  # 替换为你的实际文件夹路径

# 遍历文件夹
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.jpeg'):
        # 构建完整的文件路径
        jpg_path = os.path.join(folder_path, filename)

        # 打开JPG图片
        img = Image.open(jpg_path)
        
        # 获取原始文件名（无扩展名）
        base_name = os.path.splitext(filename)[0]
        
        # 构建保存PNG图片的路径
        png_path = os.path.join(folder_path, base_name + '.png')

        # 保存为PNG格式
        img.save(png_path, 'PNG')

        print(f"Converted {filename} to {base_name}.png")

"""
JPG 转 PNG 图像格式转换器：将指定文件夹中的所有JPG图片转换为PNG格式。

功能：
该脚本会遍历指定文件夹中的所有JPG格式的图片，并将它们转换为PNG格式后保存。PNG格式支持透明通道，如果原始图片没有透明通道，则无需特殊处理。

参数：
- folder_path: str, 包含JPG图片的文件夹路径。

用法：
1. 修改folder_path变量为实际的文件夹路径。
2. 将包含JPG图片的文件夹路径赋值给folder_path变量。
3. 运行脚本，程序会将文件夹中的所有JPG图片转换为PNG格式并保存在同一文件夹中。

注意事项：
- 转换后的PNG图片会保存在与原始JPG图片相同的文件夹中，文件名相同但扩展名为.png。
- PNG格式支持透明通道，因此可以保留图片中的透明信息。
- 确保文件夹中确实存在JPG格式的图片。
"""
