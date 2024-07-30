import cv2
import os
import glob
from tqdm import tqdm

def images_to_video(image_folder, video_name, output_dir):
    """
    将指定文件夹中的所有 .jpeg 图片合成为一个视频文件。
    
    功能：
    该函数将给定文件夹中的所有 .jpeg 图片按文件名排序后，依次合成一个视频文件。
    
    参数：
    :param image_folder: str, 包含图片的文件夹路径。
    :param video_name: str, 生成的视频文件名。
    :param output_dir: str, 视频文件保存的输出目录。

    注意事项：
    - 确保 image_folder 目录中只有需要合成的视频文件的图片。
    - 输出视频文件使用 AVI 格式，帧率为 30 帧/秒。
    - 图片分辨率应一致，否则可能导致视频失真。
    """
    # 仅匹配 .jpeg 文件
    images = [img for img in sorted(glob.glob(os.path.join(image_folder, "*.jpeg")))]
    if not images:
        print(f"No images found in {image_folder}. Skipping...")
        return

    frame = cv2.imread(images[0])
    height, width, layers = frame.shape

    video_path = os.path.join(output_dir, video_name)
    video = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

    for image in images:
        video.write(cv2.imread(image))

    cv2.destroyAllWindows()
    video.release()

def process_all_subfolders(parent_folder, output_dir):
    """
    遍历父文件夹中的所有子文件夹，将每个子文件夹中的图片合成为一个视频。

    功能：
    该函数遍历指定父文件夹中的所有子文件夹，将每个子文件夹中的 .jpeg 图片转换为一个视频文件。

    参数：
    :param parent_folder: str, 包含多个子文件夹的父文件夹路径。
    :param output_dir: str, 视频文件保存的输出目录。

    注意事项：
    - 每个子文件夹中的图片会被单独转换为一个视频文件，视频文件名与子文件夹同名。
    - 确保输出目录存在或可以创建。
    """
    subfolders = [f.path for f in os.scandir(parent_folder) if f.is_dir()]
    total = len(subfolders)
    
    with tqdm(total=total, desc="Processing subfolders") as pbar:
        for subfolder in subfolders:
            video_name = os.path.basename(subfolder) + '.avi'
            images_to_video(subfolder, video_name, output_dir)
            pbar.update()

# 指定父文件夹路径
parent_folder = " "
# 指定输出目录
output_dir = " "

# 调用函数处理所有子文件夹
process_all_subfolders(parent_folder, output_dir)
