import os
import xml.etree.ElementTree as ET

def convert_xml_to_yolo(xml_path, output_path, classes):
    """
    将单个XML文件转换为YOLO格式的标注文件。

    参数:
    - xml_path: str, 输入的XML文件路径。
    - output_path: str, 输出的YOLO格式txt文件保存路径。
    - classes: list, 包含所有类别名称的列表，用于确定类别ID。

    用法:
    该函数解析输入的XML文件，读取图片的尺寸和标注的边界框信息，然后将这些信息转换为YOLO格式，并保存为txt文件。

    注意事项:
    - 确保提供的类别列表（classes）与标注文件中的类别一致。
    - 输出文件的名称与输入XML文件的名称相同，但扩展名为.txt。
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()

    image_filename = os.path.splitext(os.path.basename(xml_path))[0] + ".txt"
    output_file = os.path.join(output_path, image_filename)

    image_width = int(root.find('size/width').text)
    image_height = int(root.find('size/height').text)

    with open(output_file, 'w') as f:
        for obj in root.findall('object'):
            class_name = obj.find('name').text
            if class_name not in classes:
                continue

            class_id = classes.index(class_name)

            bbox = obj.find('bndbox')
            xmin = int(bbox.find('xmin').text)
            ymin = int(bbox.find('ymin').text)
            xmax = int(bbox.find('xmax').text)
            ymax = int(bbox.find('ymax').text)

            x = min(1.0, (xmin + xmax) / (2 * image_width))
            y = min(1.0, (ymin + ymax) / (2 * image_height))
            width = min(1.0, (xmax - xmin) / image_width)
            height = min(1.0, (ymax - ymin) / image_height)

            f.write(f"{class_id} {x} {y} {width} {height}\n")

def batch_convert_xml_to_yolo(input_folder, output_folder, classes):
    """
    批量将文件夹中的所有XML文件转换为YOLO格式的标注文件。

    参数:
    - input_folder: str, 包含XML文件的文件夹路径。
    - output_folder: str, 保存转换后YOLO格式文件的文件夹路径。
    - classes: list, 包含所有类别名称的列表，用于确定类别ID。

    用法:
    该函数遍历输入文件夹中的所有XML文件，调用`convert_xml_to_yolo`函数进行转换，并将结果保存在输出文件夹中。

    注意事项:
    - 输入文件夹应包含所有需要转换的XML文件。
    - 输出文件夹路径应存在或可创建。
    """
    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        if file.endswith(".xml"):
            xml_path = os.path.join(input_folder, file)
            convert_xml_to_yolo(xml_path, output_folder, classes)

# 示例用法
input_folder = " "
output_folder = " "
classes = [ ' ',
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
          ]

batch_convert_xml_to_yolo(input_folder, output_folder, classes)
