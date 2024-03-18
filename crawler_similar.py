from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import requests
import base64
import hashlib

def download_images_from_url(url, num_images, save_dir):
    # Create Chrome WebDriver instance
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    try:
        driver.get(url)
        # Get all image elements
        images = driver.find_elements(By.CSS_SELECTOR, "img")
        # Create directory to save images
        os.makedirs(save_dir, exist_ok=True)

        # Download images
        downloaded_images = set()
        for i, image in enumerate(images[:num_images]):
            try:
                image_url = image.get_attribute("src")
                if not image_url:
                    continue
                image_hash = hashlib.sha256(image_url.encode('utf-8')).hexdigest()
                # Check if image has been downloaded
                if image_hash in downloaded_images:
                    print(f"Image {i+1} already downloaded, skipping...")
                    continue

                image_save_path = os.path.join(save_dir, f"image_{i}.jpg")
                # Check if file already exists, if so, change filename
                counter = 0
                while os.path.exists(image_save_path):
                    counter += 1
                    image_save_path = os.path.join(save_dir, f"image_{i}_{counter}.jpg")

                # Handle normal URL and base64 data URI
                if image_url.startswith('data:image/jpeg;base64,'):
                    base64_data = image_url.replace('data:image/jpeg;base64,', '')
                    image_data = base64.b64decode(base64_data)
                    with open(image_save_path, 'wb') as f:
                        f.write(image_data)
                else:
                    response = requests.get(image_url)
                    with open(image_save_path, "wb") as f:
                        f.write(response.content)

                downloaded_images.add(image_hash)
                print(f"Image {i+1} saved successfully")
            except Exception as e:
                print(f"Failed to save image {i+1}: {str(e)}")
    except Exception as e:
        print(f"An error occurred while processing the URL: {str(e)}")

    driver.quit()

if __name__ == "__main__":
    url = input("Enter the URL containing images you want to download: ")
    num_images = int(input("Enter the number of images you want to download: "))
    save_dir = input("Enter the directory to save images: ")
    download_images_from_url(url, num_images, save_dir)