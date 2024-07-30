"""
此脚本的功能是删除指定文件夹中所有空白的TXT文件。它会遍历指定文件夹中的所有文件，识别并删除那些大小为0字节的TXT文件。

参数和用法：
- folder_path: str, 指定要操作的文件夹路径。

代码的功能：
1. 遍历指定文件夹中的所有文件。
2. 检查每个文件的扩展名是否为“.txt”。
3. 对于每个TXT文件，检查其文件大小是否为0字节。
4. 如果文件是空白的（即大小为0字节），则删除该文件并在控制台输出删除信息。

注意事项：
- 请确保提供的文件夹路径正确，以避免误删文件。
- 操作不可逆，删除的文件将无法恢复，请谨慎使用。
- 建议在删除文件前备份重要数据。
"""

import os

def delete_empty_txt_files(folder_path):
    # 遍历文件夹中的每一个文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            # 检查txt文件是否为空
            if os.path.getsize(file_path) == 0:
                # 删除空白txt文件
                os.remove(file_path)
                print(f"已删除空白txt文件: {file_path}")

    print("空白txt文件删除完成。")

# 使用示例
folder_path = " "
delete_empty_txt_files(folder_path)
