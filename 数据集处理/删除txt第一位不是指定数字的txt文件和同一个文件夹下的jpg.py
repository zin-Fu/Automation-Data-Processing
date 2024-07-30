import os

def delete_files_not_starting_with(folder_path, start_digit):
    """
    删除文件夹中文件名第一位不是指定数字的所有.txt文件和对应的.jpg文件。

    功能：
    该脚本用于清理指定文件夹中不符合特定命名规则的文件。具体来说，它会删除文件名第一位
    不是指定数字的所有文本文件（.txt）和与这些文本文件同名的图片文件（.jpg）。

    参数：
    :param folder_path: str, 需要处理的文件夹路径。
    :param start_digit: str, 文件名应该以该数字开头的条件字符。

    用法：
    1. 设置 folder_path 为包含目标文件的文件夹路径。
    2. 设置 start_digit 为你希望保留的文件名的首数字字符。
    3. 运行脚本，脚本将删除不符合条件的文件。

    注意事项：
    - 删除操作是不可逆的，请在运行脚本前备份重要文件。
    - 该脚本假设每个文本文件都有一个与之对应的图像文件，且文件名（不包括扩展名）相同。
    """
    if not os.path.exists(folder_path):
        print(f"文件夹不存在: {folder_path}")
        return

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            # 检查文件名的第一位是否为指定数字
            if not filename.startswith(start_digit):
                txt_path = os.path.join(folder_path, filename)
                jpg_path = os.path.join(folder_path, filename.replace('.txt', '.jpg'))

                # 删除txt文件
                os.remove(txt_path)
                print(f"Deleted txt file: {txt_path}")

                # 删除对应的jpg文件（如果存在）
                if os.path.exists(jpg_path):
                    os.remove(jpg_path)
                    print(f"Deleted jpg file: {jpg_path}")

if __name__ == "__main__":
    folder_path = " "  # 替换为你的文件夹路径
    start_digit = "1"  # 替换为你要保留的文件名的首数字字符

    delete_files_not_starting_with(folder_path, start_digit)
