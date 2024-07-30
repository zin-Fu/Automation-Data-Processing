"""
此脚本的功能是检查两个文件夹中的JPG和XML文件是否存在对应关系，并删除没有匹配对的文件。具体来说：
1. 检查每个JPG文件是否有对应的XML文件，如果没有，则删除该JPG文件。
2. 检查每个XML文件是否有对应的JPG文件，如果没有，则删除该XML文件。

参数和用法：
- jpg_folder: str, 存放JPG文件的目录路径。
- xml_folder: str, 存放XML文件的目录路径。

代码的功能：
1. 列出JPG文件夹中的所有文件名。
2. 列出XML文件夹中的所有文件名。
3. 遍历JPG文件，检查是否有对应的XML文件；如果没有，删除JPG文件。
4. 遍历XML文件，检查是否有对应的JPG文件；如果没有，删除XML文件。

注意事项：
- 请确保提供的文件夹路径正确，以避免误删文件。
- 操作不可逆，删除的文件将无法恢复，请谨慎使用。
- 在执行删除操作前建议备份文件。
"""

import os

jpg_folder = '/path/to/jpg_folder'  # JPG文件所在的文件夹路径
xml_folder = '/path/to/xml_folder'  # XML文件所在的文件夹路径

jpg_files = os.listdir(jpg_folder)
xml_files = os.listdir(xml_folder)

# 检查JPG文件是否有对应的XML文件
for jpg_file in jpg_files:
    jpg_name = os.path.splitext(jpg_file)[0]
    xml_file = jpg_name + '.xml'
    if xml_file not in xml_files:
        jpg_path = os.path.join(jpg_folder, jpg_file)
        os.remove(jpg_path)
        print(f"删除文件: {jpg_file} (没有对应的XML文件)")

# 检查XML文件是否有对应的JPG文件
for xml_file in xml_files:
    xml_name = os.path.splitext(xml_file)[0]
    jpg_file = xml_name + '.jpg'
    if jpg_file not in jpg_files:
        xml_path = os.path.join(xml_folder, xml_file)
        os.remove(xml_path)
        print(f"删除文件: {xml_file} (没有对应的JPG文件)")

print("完成")
