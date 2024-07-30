import os
from pdf2image import convert_from_path

def convert_pdf_to_jpg(pdf_folder, output_folder):
    """
    PDF 转 JPG 图片转换器：将指定文件夹中的所有PDF文件转换为JPG格式的图片。

    功能：
    该脚本将指定文件夹中的PDF文件转换为一系列JPG图片，并将这些图片保存到指定的输出文件夹中。

    参数：
    :param pdf_folder: str, 包含PDF文件的文件夹路径。
    :param output_folder: str, 用于保存转换后的JPG图片的文件夹路径。

    用法：
    1. 将待转换的PDF文件放置在指定的pdf_folder中。
    2. 修改pdf_folder和output_folder变量为实际的输入和输出文件夹路径。
    3. 运行脚本，程序会将每个PDF文件的每一页转换为单独的JPG图片，并保存到output_folder中。
    
    注意事项：
    - 确保pdf_folder中的文件确实是PDF格式。
    - 输出的JPG图片文件名将保持与PDF文件名一致，只是会附加页码后缀以区分不同页。
    - 使用前请确保已安装pdf2image库和相应的PDF转换器支持库（如poppler）。

    示例用法：
    pdf_folder = 'path/to/pdf/folder'  # 替换为包含PDF文件的文件夹路径
    output_folder = 'path/to/output/folder'  # 替换为保存JPG图片的文件夹路径
    convert_pdf_to_jpg(pdf_folder, output_folder)
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # 遍历pdf_folder中的所有文件
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            # 使用convert_from_path函数将PDF转换为一系列的图像
            images = convert_from_path(os.path.join(pdf_folder, filename))

            for i, image in enumerate(images):
                # 保存每个图像为JPG，文件名与PDF相同，但扩展名不同
                image.save(f'{output_folder}/{os.path.splitext(filename)[0]}_{i}.jpg', 'JPEG')

if __name__ == "__main__":
    convert_pdf_to_jpg(' ', ' ')
