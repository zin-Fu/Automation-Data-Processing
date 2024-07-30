"""
此脚本的功能是删除指定文件夹中的所有JSON文件。它会遍历给定文件夹中的所有文件，识别出以“.json”结尾的文件，并将其删除。

参数和用法：
- FOLDER_PATH: str, 指定要操作的文件夹路径。

代码的功能：
1. 遍历指定文件夹中的所有文件。
2. 检查文件的扩展名是否为“.json”。
3. 如果是JSON文件，删除该文件并在控制台输出删除信息。

注意事项：
- 请确保提供的文件夹路径正确，以避免误删文件。
- 操作不可逆，删除的文件将无法恢复，请谨慎使用。
- 在执行删除操作前建议备份文件。
"""

import os

FOLDER_PATH = 'D:\\00study\\Artificial_Intelligence\\HACI\\TCM\\Data\\ALL\\The white tongue is thick and greasy'

def del_json(folder_path):
    for file in os.listdir(folder_path):
        if file.endswith('.json'):
            file_path = os.path.join(folder_path, file)
            os.remove(file_path)
            print("Delete {}".format(file))

if __name__ == '__main__':
    del_json(FOLDER_PATH)
