# Data Processing Automation Tool 🤖

Aims to provide automated data collection, data augmentation, data renaming, and data splitting functionalities for model training.

这个repo放的是我平常写的一些数据处理脚本，希望能对你有所帮助。

每个脚本里都有详细的注释，介绍其功能、参数用法和一些注意事项。

## Update 🤗

- **2024/7/30:** Added a list of scripts written this semester for image/data processing.
- **2024/3/21:** Added scripts to divide test & train.
- **2024/3/15:** Created the repo

## Directory tree🧐

```
    其他/
        PDF 转 JPG .py
        批量计算文件大小.py
        移动指定天数前的文件.py
        打印指定文件夹下的目录树.py
    图像处理和数据增强/
        图像转视频.py
        批量JPG转PNG.py
        批量PNG 转 JPG.py
        批量图像暖化(调色温).py
        批量调整图像亮度.py
        批量调整图像分辨率.py
        批量调整图像的曝光度.py
        数据增强.py
    数据集处理/
        yolo格式训练集和测试集划分.py
        分离同一文本和图像到指定文件夹.py
        删除txt第一位不是指定数字的txt文件和同一个文件夹下的jpg.py
        删除指定文件夹中的JSON文件.py
        删除空白的TXT文件.py
        图片文件夹归类.py
        复制匹配的文本文件.py
        检查并删除没有匹配文件的JPG和XML.py
        检查训练集，测试集label和img是否一一对应.py
        移动没有对应标签的图片.py
        获取image路径，写进txt文件.py
        遍历jpg，删除无对应txt的文件.py
        遍历txt，删除没有对应jpg的文件.py
    文件命名处理/
        批量图片重命名.py
        文件名空格替换为下划线.py
    标签格式转换与处理yolo/
        XML转YOLO格式批量转换.py
        YOLO标注转VOC标注.py
        修复XML文件中的标签闭合.py
    爬虫/
        谷歌图片关键词抓取.py
        谷歌相似图片抓取.py
    视频处理/
        视频帧提取.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
