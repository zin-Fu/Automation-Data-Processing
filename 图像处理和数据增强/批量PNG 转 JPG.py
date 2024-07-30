from PIL import Image
import os

# 指定文件夹路径
folder_path = 'teargas'

# 遍历文件夹
for filename in os.listdir(folder_path):
    if filename.endswith('.png'):
        # 打开PNG图片
        img = Image.open(os.path.join(folder_path, filename))
        # 转换为RGB格式（JPG不支持透明通道）
        rgb_img = img.convert('RGB')
        # 保存为JPG格式
        rgb_img.save(os.path.join(folder_path, os.path.splitext(filename)[0] + '.jpg'))

"""
PNG 转 JPG 图像格式转换器：将指定文件夹中的所有PNG图片转换为JPG格式。

功能：
该脚本会遍历指定文件夹中的所有PNG格式的图片，并将它们转换为JPG格式后保存。JPG格式不支持透明通道，因此在转换过程中，图片会被转换为RGB格式。

参数：
- folder_path: str, 包含PNG图片的文件夹路径。

用法：
1. 修改folder_path变量为实际的文件夹路径。
2. 将包含PNG图片的文件夹路径赋值给folder_path变量。
3. 运行脚本，程序会将文件夹中的所有PNG图片转换为JPG格式并保存在同一文件夹中。

注意事项：
- 转换后的JPG图片会保存在与原始PNG图片相同的文件夹中，文件名相同但扩展名为.jpg。
- JPG格式不支持透明通道，因此转换后的图片不再具有透明度信息，透明部分会变为白色或其他背景色。
- 确保文件夹中确实存在PNG格式的图片。
"""
