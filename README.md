# Data Processing Automation Tool🤖

Aims to provide automated data collection, data augmentation, and data renaming functionalities for deep learning model training.

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

## Script Descriptions

1. `crawler_keyword.py` - A script to download images from Google Image Search based on a keyword.

2. `crawler_similar.py` - A script to download images from a given URL.

3. `DataAugment.py` - A script to perform various data augmentation techniques on images, such as flipping, rotating, adding noise, blurring, and adjusting brightness and contrast.

4. `rename.py` - A script to rename all image files in a specified directory with a given prefix and sequential numbers.

## Detail

#### 1. `crawler_keyword.py`

This script is used to download images from Google Image Search. It utilizes the Selenium library to automate browser operations.

**Usage:**
- Enter the keyword for the search
- Enter the number of images to download
- Enter the directory path to save the images

#### 2. `crawler_similar.py`

This script is used to download images from a specified URL. It also utilizes the Selenium library to automate browser operations.

**Usage:**
- Enter the URL containing the images to download
- Enter the number of images to download
- Enter the directory path to save the images

#### 3. `DataAugment.py`

This script is used to perform data augmentation on images. It provides various data augmentation techniques, such as flipping, rotation, noise addition, Gaussian blurring, brightness and contrast adjustment, affine transformation, and translation.

**Usage:**
- Enter the path containing the original images
- Select the data augmentation techniques to use, separated by commas (1: Flip, 2: Rotate, 3: Noise, 4: Gaussian blur, 5: Brightness and contrast adjustment, 6: Affine transformation, 7: Translation)
- The augmented images will be saved in the same directory as the original images

#### 4. `rename.py`

This script is used to rename all image files in a specified directory.

**Usage:**

- Enter the directory path containing the images to be renamed
- Enter the new prefix for the image names
- The script will rename all images and save them in the format `{new_prefix}_{number}.{extension}`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
