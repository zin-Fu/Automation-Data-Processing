import os
import sys

"""
此脚本用于计算指定目录及其所有子目录中的文件总大小，并以字节、千字节、兆字节和千兆字节为单位显示结果。

功能说明：
- 该脚本接收一个目录路径作为命令行参数，计算该目录及其所有子目录中所有文件的总大小。
- 结果以不同的单位显示，包括字节、千字节、兆字节和千兆字节。

用法：
1. 在命令行中运行该脚本，并提供一个目录路径作为参数。例如：
   python script.py /path/to/directory
2. 脚本将递归遍历目录中的所有文件，并计算总大小。
3. 输出的结果将以不同单位显示文件大小。

参数：
- directory：需要计算大小的目录路径，必须作为命令行参数提供。

注意事项：
1. 如果未提供目录路径，脚本将退出并提示错误信息。
2. 如果目录中没有文件，总大小将显示为0。
3. 输出结果包括字节、千字节、兆字节和千兆字节四种单位，按单位从大到小排序。

示例：python calculate_directory_size.py /path/to/directory
"""

try:
    directory = sys.argv[1]
except IndexError:
    sys.exit("必须提供一个目录路径作为参数。")

dir_size = 0
fsizedicr = {
    "Bytes": 1,
    "Kilobytes": float(1) / 1024,
    "Megabytes": float(1) / (1024 * 1024),
    "Gigabytes": float(1) / (1024 * 1024 * 1024),
}

for (path, dirs, files) in os.walk(directory):
    for file in files:
        filename = os.path.join(path, file)
        dir_size += os.path.getsize(filename)

fsizeList = [
    str(round(fsizedicr[key] * dir_size, 2)) + " " + key for key in fsizedicr
]

if dir_size == 0:
    print("文件夹为空")
else:
    for units in sorted(fsizeList)[::-1]:
        print("文件夹大小: " + units)
