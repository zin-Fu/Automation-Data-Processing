from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import requests
import base64
import hashlib

def google_image_scraper(keyword, num_images, save_dir):
    """
    谷歌图片抓取器：根据关键词抓取谷歌图片搜索结果的图片并保存到指定目录。
    
    功能：
    该函数使用Selenium模拟浏览器操作，在谷歌图片搜索页面根据输入的关键词搜索图片，并将搜索结果中的图片下载保存到本地。

    参数：
    :param keyword: str, 搜索关键词。
    :param num_images: int, 要下载的图片数量。
    :param save_dir: str, 图片保存的目录。

    注意事项：
    - 确保已安装Chrome浏览器及其对应版本的ChromeDriver。
    - 确保有良好的网络连接，以便从谷歌图片下载图片。
    - 下载图片时会过滤非https链接和已下载的图片，确保下载的图片安全且不重复。
    - 如果图片以base64编码形式存在，会进行解码并保存图片。
    - 使用Selenium时请注意谷歌的使用政策，不要频繁请求以避免被封锁。

    用法：
    1. 运行此脚本后，输入要搜索的关键词。
    2. 输入要下载的图片数量。
    3. 输入图片保存的目录路径。
    4. 程序会自动抓取并保存图片。
    """
    # 创建 Chrome WebDriver 实例
    driver = webdriver.Chrome()
    # 设置等待加载时间
    driver.implicitly_wait(5)
    
    # 打开 Google 图片搜索页面
    driver.get("https://www.google.com/imghp")
    
    from selenium.webdriver.common.by import By

    # 定位搜索框并输入关键词
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)
    
    # 模拟滚动页面，加载更多图片
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    # 获取所有图片元素
    images = driver.find_elements(By.CSS_SELECTOR, "img.rg_i")
    # 创建保存图片的目录
    os.makedirs(save_dir, exist_ok=True)
    
    # 下载图片
    downloaded_images = set()
    for i, image in enumerate(images[:num_images]):
        try:
            # 获取图片链接
            image_url = image.get_attribute("src")
            # 计算图片 URL 的哈希值
            image_hash = hashlib.sha256(image_url.encode('utf-8')).hexdigest()
            # 检查图片是否已经下载
            if image_hash in downloaded_images:
                print(f"Image {i+1} already downloaded, skipping...")
                continue
            # 检查图片链接是否为 https
            if not image_url.startswith('https://'):
                print(f"Image {i+1} is not from a secure source, skipping...")
                continue
            # 下载图片并保存
            image_path = os.path.join(save_dir, f"{keyword}_{i}.jpg")
            # 检查文件是否已经存在，如果存在，就修改文件名
            counter = 0
            while os.path.exists(image_path):
                counter += 1
                image_path = os.path.join(save_dir, f"{keyword}_{i}_{counter}.jpg")
            if image_url.startswith('data:image/jpeg;base64,') or image_url.startswith('data:image/gif;base64,'):
                base64_data = image_url.split(',', 1)[1]
                image_data = base64.b64decode(base64_data)
                with open(image_path, 'wb') as f:
                    f.write(image_data)
            else:
                response = requests.get(image_url)
                with open(image_path, "wb") as f:
                    f.write(response.content)
            downloaded_images.add(image_hash)
            print(f"Image {i+1} saved successfully")
        except Exception as e:
            print(f"Failed to save image {i+1}: {str(e)}")
    
    # 关闭浏览器
    driver.quit()

if __name__ == "__main__":
    keyword = input("Enter the keyword you want to search: ")
    num_images = int(input("Enter the number of images you want to download: "))
    save_dir = input("Enter the directory to save images: ")
    google_image_scraper(keyword, num_images, save_dir)
