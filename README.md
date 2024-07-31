# Data Processing Automation Tool 🤖

**_🚀Aims to provide scripts for image processing, data augmentation, dataset handling, file renaming, label format conversion, and web crawling to facilitate various data processing needs.🚀_**

This repo contains some of the data processing scripts I write. Hope it'll help you.

Each script has detailed comments describing its functionality, parameter usage, and considerations.

这个repo放的是我平常写的一些数据处理脚本，希望能对你有所帮助。

每个脚本里都有详细的注释，介绍其功能、参数用法和一些注意事项。

## Update 🤗

- **2024/7/30:** Added a list of scripts written this semester for image/data processing.
- **2024/3/21:** Added scripts to divide test & train.
- **2024/3/15:** Created the repo

## Directory tree🧐

```
├── 其他 (Others)
│   ├── PDF 转 JPG.py (PDF to JPG)
│   ├── 批量计算文件大小.py (Batch Calculate File Size)
│   ├── 移动指定天数前的文件.py (Move Files Older Than Specified Days)
│   └── 打印指定文件夹下的目录树.py (Print Directory Tree)
├── 图像处理和数据增强 (Image Processing and Data Augmentation)
│   ├── 图像转视频.py (Image to Video)
│   ├── 批量JPG转PNG.py (Batch Convert JPG to PNG)
│   ├── 批量PNG 转 JPG.py (Batch Convert PNG to JPG)
│   ├── 批量图像暖化(调色温).py (Batch Image Warming (Adjust Color Temperature))
│   ├── 批量调整图像亮度.py (Batch Adjust Image Brightness)
│   ├── 批量调整图像分辨率.py (Batch Adjust Image Resolution)
│   ├── 批量调整图像的曝光度.py (Batch Adjust Image Exposure)
│   └── 数据增强.py (Data Augmentation)
├── 数据集处理 (Dataset Processing)
│   ├── yolo格式训练集和测试集划分.py (YOLO Format Train-Test Split)
│   ├── 分离同一文本和图像到指定文件夹.py (Separate Text and Image to Specific Folders)
│   ├── 删除txt第一位不是指定数字的txt文件和同一个文件夹下的jpg.py (Delete TXT Files Not Starting with a Specified Digit and Corresponding JPGs in the Same Folder)
│   ├── 删除指定文件夹中的JSON文件.py (Delete JSON Files in Specific Folder)
│   ├── 删除空白的TXT文件.py (Delete Empty TXT Files)
│   ├── 图片文件夹归类.py (Classify Image Folders)
│   ├── 复制匹配的文本文件.py (Copy Matching Text Files)
│   ├── 检查并删除没有匹配文件的JPG和XML.py (Check and Delete Unmatched JPG and XML Files)
│   ├── 检查训练集，测试集label和img是否一一对应.py (Check if Train and Test Labels Match Images)
│   ├── 移动没有对应标签的图片.py (Move Images Without Corresponding Labels)
│   ├── 获取image路径，写进txt文件.py (Get Image Paths and Write to TXT File)
│   ├── 遍历jpg，删除无对应txt的文件.py (Traverse JPGs and Delete Unmatched TXT Files)
│   └── 遍历txt，删除没有对应jpg的文件.py (Traverse TXTs and Delete Unmatched JPG Files)
├── 文件命名处理 (File Naming)
│   ├── 批量图片重命名.py (Batch Rename Images)
│   └── 文件名空格替换为下划线.py (Replace Spaces in Filenames with Underscores)
├── 标签格式转换与处理yolo (Label Format Conversion and YOLO Processing)
│   ├── XML转YOLO格式批量转换.py (Batch Convert XML to YOLO Format)
│   ├── YOLO标注转VOC标注.py (Convert YOLO Annotations to VOC Annotations)
│   └── 修复XML文件中的标签闭合.py (Fix Label Closure in XML Files)
├── 爬虫 (Web Crawling)
│   ├── 谷歌图片关键词抓取.py (Google Image Keyword Scraping)
│   └── 谷歌相似图片抓取.py (Google Similar Image Scraping)
└── 视频处理 (Video Processing)
    └── 视频帧提取.py (Extract Video Frames)

```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
