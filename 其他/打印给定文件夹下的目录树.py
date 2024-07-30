import os

def list_files(startpath):
    """
    打印指定文件夹下的文件和文件夹的层级结构。

    参数:
    startpath (str): 开始遍历的文件夹路径。
    """
    for root, dirs, files in os.walk(startpath):
        # 计算当前目录的层级（用作缩进）
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{subindent}{f}')

if __name__ == "__main__":
    # 设置开始路径
    start_path = input("请输入要生成文件图的文件夹路径：")
    list_files(start_path)
