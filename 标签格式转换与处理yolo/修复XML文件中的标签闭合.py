"""
此脚本的功能是检查并修复指定目录下的XML文件中`<annotation>`标签的闭合问题。它会遍历目录中的所有XML文件，解析每个文件的内容，并检查根标签`<annotation>`的闭合情况。如果发现不闭合的问题，将尝试修复并保存修改后的文件。

参数和用法：
- xml_dir: str, 存放XML文件的目录路径。

代码的功能：
1. 遍历指定目录中的所有XML文件。
2. 使用lxml库解析每个XML文件。
3. 检查根标签`<annotation>`的闭合情况。
4. 如果发现根标签不闭合的问题，尝试修复。
5. 保存修正后的XML文件。

注意事项：
- 此脚本仅修复根标签`<annotation>`的闭合问题，其他类型的标签闭合问题不会处理。
- 解析和修复过程中可能会修改XML文件的格式，因此建议备份文件。
- 请确保lxml库已安装：`pip install lxml`。
"""

import os
from lxml import etree

# 生成的XML文件所在目录
xml_dir = 'annotations'

for xml_file in os.listdir(xml_dir):
    # 解析XML文件
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(os.path.join(xml_dir, xml_file), parser)
    root = tree.getroot()

    # 检查annotation闭合
    try:
        if root.tag != root.tail.split('}')[-1]:
            print(f'{xml_file} annotation not aligned')
            root.tail = root.tail.replace('/annotation', '') + '/annotation'
            print(f'{xml_file} annotation fixed')

    except AttributeError:
        pass

    # 保存修正后的XML文件
    xml_content = etree.tostring(root, pretty_print=True).decode()
    with open(os.path.join(xml_dir, xml_file), 'w') as f:
        f.write(xml_content)

print('Annotation check completed.')
