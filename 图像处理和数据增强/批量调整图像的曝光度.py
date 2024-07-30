from PIL import Image, ImageEnhance
import os

def batch_adjust_exposure(input_dir, output_dir, exposure_factor):
    """
    批量调整图像的曝光度

    该函数读取指定目录下的所有图片文件，调整它们的曝光度并将处理后的图像保存到输出目录。

    参数:
    input_dir (str): 输入图片文件夹路径
    output_dir (str): 输出图片文件夹路径
    exposure_factor (float): 曝光调整因子。值大于1会增加亮度，小于1会减少亮度。

    用法:
    - 设置 input_dir 为输入图片文件夹的路径。
    - 设置 output_dir 为保存调整后图片的文件夹路径。
    - 设置 exposure_factor 为曝光调整因子。
    - 运行脚本，处理后的图片将保存在 output_dir 中。
    """
    # 创建输出目录（如果不存在）
    os.makedirs(output_dir, exist_ok=True)
    
    # 获取输入目录下的所有文件
    file_list = os.listdir(input_dir)
    
    # 遍历每个文件
    for filename in file_list:
        # 检查文件扩展名是否为图片格式
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            # 构建输入和输出文件的完整路径
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            # 打开图像文件
            image = Image.open(input_path)
            
            # 调整曝光
            enhancer = ImageEnhance.Brightness(image)
            enhanced_image = enhancer.enhance(exposure_factor)
            
            # 保存调整后的图像
            enhanced_image.save(output_path)

# 输入目录
input_directory = r" "

# 输出目录
output_directory = r" "

# 曝光调整因子
exposure_factor = 18

# 调用批量调整曝光函数
batch_adjust_exposure(input_directory, output_directory, exposure_factor)
print("Done!")
