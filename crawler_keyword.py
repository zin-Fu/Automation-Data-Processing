from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import requests
import base64
import hashlib

def google_image_scraper(keyword, num_images, save_dir):
    # Create Chrome WebDriver instance
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    
    # Open Google Image Search page
    driver.get("https://www.google.com/imghp")
    
    from selenium.webdriver.common.by import By

    # Locate the search box and enter the keyword
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)
    
    # Simulate scrolling the page to load more images
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    # Get all image elements
    images = driver.find_elements(By.CSS_SELECTOR, "img.rg_i")
    os.makedirs(save_dir, exist_ok=True)
    
    # Download images
    downloaded_images = set()
    for i, image in enumerate(images[:num_images]):
        try:
            image_url = image.get_attribute("src")
            image_hash = hashlib.sha256(image_url.encode('utf-8')).hexdigest()
            # Check if image has been downloaded
            if image_hash in downloaded_images:
                print(f"Image {i+1} already downloaded, skipping...")
                continue
            # Check if image link is https
            if not image_url.startswith('https://'):
                print(f"Image {i+1} is not from a secure source, skipping...")
                continue
            image_path = os.path.join(save_dir, f"{keyword}_{i}.jpg")
            # Check if file already exists, if so, change filename
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
    
    driver.quit()

if __name__ == "__main__":
    keyword = input("Enter the keyword you want to search: ")
    num_images = int(input("Enter the number of images you want to download: "))
    save_dir = input("Enter the directory to save images: ")
    google_image_scraper(keyword, num_images, save_dir)