from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import requests
import base64
import hashlib
from urllib.parse import urlparse

def download_images_from_url(url, num_images, save_dir):
    """
    网页图片下载器：从指定的URL下载图片并保存到本地目录。
    
    功能：
    该脚本使用Selenium模拟浏览器操作，从输入的网页URL中下载指定数量的图片，并保存到指定的本地目录。

    参数：
    :param url: str, 包含图片的网页的URL。
    :param num_images: int, 要下载的图片数量。
    :param save_dir: str, 图片保存的本地目录。

    注意事项：
    - 确保已安装Chrome浏览器及其对应版本的ChromeDriver。
    - 提供的URL应包含图片资源。
    - 下载图片时，图片URL的哈希值会用于防止重复下载。
    - 下载的图片将以顺序编号保存到指定的本地目录。
    - 脚本会尝试从非https的链接下载图片，这可能会有安全风险，使用时请注意。

    用法：
    1. 运行脚本后，输入包含图片的网页URL。
    2. 输入要下载的图片数量。
    3. 输入图片保存的本地目录路径。
    4. 程序会自动抓取并保存图片。
    """
    # 创建 Chrome WebDriver 实例
    driver = webdriver.Chrome()
    # 设置等待加载时间
    driver.implicitly_wait(5)

    try:
        # 打开输入的 URL
        driver.get(url)

        # 获取所有图片元素
        images = driver.find_elements(By.CSS_SELECTOR, "img")
        # 创建保存图片的目录
        os.makedirs(save_dir, exist_ok=True)

        # 下载图片
        downloaded_images = set()
        for i, image in enumerate(images[:num_images]):
            try:
                # 获取图片链接
                image_url = image.get_attribute("src")
                # 跳过空链接
                if not image_url:
                    continue
                # 计算图片 URL 的哈希值
                image_hash = hashlib.sha256(image_url.encode('utf-8')).hexdigest()
                # 检查图片是否已经下载
                if image_hash in downloaded_images:
                    print(f"Image {i+1} already downloaded, skipping...")
                    continue
                # 下载图片并保存
                image_save_path = os.path.join(save_dir, f"image_{i}.jpg")
                # 检查文件是否已经存在，如果存在，就修改文件名
                counter = 0
                while os.path.exists(image_save_path):
                    counter += 1
                    image_save_path = os.path.join(save_dir, f"image_{i}_{counter}.jpg")
                response = requests.get(image_url)
                with open(image_save_path, "wb") as f:
                    f.write(response.content)
                downloaded_images.add(image_hash)
                print(f"Image {i+1} saved successfully")
            except Exception as e:
                print(f"Failed to save image {i+1}: {str(e)}")
    except Exception as e:
        print(f"An error occurred while processing the URL: {str(e)}")

    # 关闭浏览器
    driver.quit()

if __name__ == "__main__":
    url = input("Enter the URL containing images you want to download: ")
    num_images = int(input("Enter the number of images you want to download: "))
    save_dir = input("Enter the directory to save images: ")
    download_images_from_url(url, num_images, save_dir)
