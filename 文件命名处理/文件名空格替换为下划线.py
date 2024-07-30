import os
import shutil

def rename_files_in_folder(folder_path):
    """
    此函数用于遍历指定文件夹中的所有文件，并将文件名中包含的空格替换为下划线。
    可以避免在脚本或程序中因空格引起的路径解析问题。

    参数:
    folder_path (str): 文件夹的路径，其中包含需要重命名的文件。

    用法:
    调用此函数时，需传入目标文件夹的路径。例如：
    rename_files_in_folder('C:\\Users\\YourUserName\\Documents\\YourFolder')
    此调用将遍历'C:\\Users\\YourUserName\\Documents\\YourFolder'文件夹中的所有文件，
    并将其中文件名包含空格的文件进行重命名，将空格替换为下划线。
    """

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 如果文件名中有空格
        if ' ' in filename:
            # 创建一个新的文件名，将空格替换为下划线
            new_filename = filename.replace(' ', '_')
            # 获取原文件和新文件的完整路径
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)
            # 重命名文件
            shutil.move(old_file_path, new_file_path)

# 使用你的文件夹路径调用这个函数
rename_files_in_folder('')  # 在这里填写目标文件夹的路径
