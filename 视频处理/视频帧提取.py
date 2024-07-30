import cv2
import os

def video_to_images(video_path, output_dir, frame_rate=1):
    """
    将视频转换为图片，并保存每帧图像。

    :param video_path: str, 输入视频文件的路径
    :param output_dir: str, 保存图片的目录路径
    :param frame_rate: int, 每隔多少帧保存一张图片
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    cap = cv2.VideoCapture(video_path)
    
    # 检查视频是否成功打开
    if not cap.isOpened():
        print(f"错误: 无法打开视频 {video_path}")
        return

    frame_count = 0
    image_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        if frame_count % frame_rate == 0:
            image_filename = os.path.join(output_dir, f"{os.path.basename(video_path).split('.')[0]}_frame{frame_count:04d}.jpg")
            cv2.imwrite(image_filename, frame)
            image_count += 1
            print(f"已保存 {image_filename}")

    cap.release()
    print(f"总共处理帧数: {frame_count}, 总共保存图片: {image_count}")

def process_all_videos(input_dir, output_dir, frame_rate=1):
    """
    处理给定目录中的所有视频，将每个视频转换为图片。

    :param input_dir: str, 包含输入视频的目录路径
    :param output_dir: str, 保存图片的目录路径
    :param frame_rate: int, 每隔多少帧保存一张图片
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv', '.flv')):
            video_path = os.path.join(input_dir, filename)
            video_output_dir = os.path.join(output_dir, os.path.splitext(filename)[0])
            video_to_images(video_path, video_output_dir, frame_rate)

if __name__ == "__main__":
    input_directory = " "  # 替换为你的视频文件夹路径
    output_directory = " "   # 替换为你希望保存图像的文件夹路径
    frame_rate = 1  # 每隔多少帧保存一张图片

    process_all_videos(input_directory, output_directory, frame_rate)
