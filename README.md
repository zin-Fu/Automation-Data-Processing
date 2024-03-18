# Data Processing Automation Tool for Deep Learning

This project aims to provide automated data collection, data augmentation, and data renaming functionalities for deep learning model training. It includes the following Python scripts:

## File List

1. `crawler_keyword.py`
2. `crawler_similar.py`
3. `DataAugment.py`
4. `rename.py`

## Requirements

This project requires the following dependencies:

- Python 3.x
- Selenium
- OpenCV
- NumPy

You can install the required dependencies by running the following command:

```
pip install -r requirements.txt
```

## File Descriptions

### 1. `crawler_keyword.py`

This script is used to download images from Google Image Search. It utilizes the Selenium library to automate browser operations.

**Usage:**

1. Run the script
2. Enter the keyword for the search
3. Enter the number of images to download
4. Enter the directory path to save the images

### 2. `crawler_similar.py`

This script is used to download images from a specified URL. It also utilizes the Selenium library to automate browser operations.

**Usage:**

1. Run the script
2. Enter the URL containing the images to download
3. Enter the number of images to download
4. Enter the directory path to save the images

### 3. `DataAugment.py`

This script is used to perform data augmentation on images. It provides various data augmentation techniques, such as flipping, rotation, noise addition, Gaussian blurring, brightness and contrast adjustment, affine transformation, and translation.

**Usage:**

1. Run the script
2. Enter the path containing the original images
3. Select the data augmentation techniques to use, separated by commas (1: Flip, 2: Rotate, 3: Noise, 4: Gaussian blur, 5: Brightness and contrast adjustment, 6: Affine transformation, 7: Translation)
4. The augmented images will be saved in the same directory as the original images

### 4. `rename.py`

This script is used to rename all image files in a specified directory.

**Usage:**

1. Run the script
2. Enter the directory path containing the images to be renamed
3. Enter the new prefix for the image names
4. The script will rename all images and save them in the format `{new_prefix}_{number}.{extension}`

## Project Introduction

This project aims to simplify the data collection, data augmentation, and data management steps in the deep learning model training process. It provides a set of convenient tools to automatically download images from the internet, perform image enhancement, and rename images. These functionalities can greatly improve the efficiency of data preparation and provide high-quality data for deep learning model training.

## License

This project is licensed under the MIT License, which allows you to freely use, modify, and distribute the code of this project according to the terms of the license.
