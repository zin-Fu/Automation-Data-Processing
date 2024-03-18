import numpy as np
import os
import cv2
import glob
import random

def data_augmentation(img, techniques):
    img_list = []
    
    if '1' in techniques:
        # Flip
        img_list.append(cv2.flip(img, 1))  # Horizontal flip
        img_list.append(cv2.flip(img, 0))  # Vertical flip
        img_list.append(cv2.flip(img, -1)) # Horizontal and vertical flip
    
    if '2' in techniques:
        # Rotate
        scale = 1.0
        rows, cols = img.shape[:2]
        center = (cols / 2, rows / 2)  # Image center
        angle = [45, 315]
        for a in angle:
            M = cv2.getRotationMatrix2D(center, a, scale)
            rotated = cv2.warpAffine(img, M, (cols, rows), borderValue=(255, 255, 255))
            img_list.append(rotated)
    
    if '3' in techniques:
        # Noise
        noise_img = img.copy()
        for _ in range(1500):
            noise_img[random.randint(0, noise_img.shape[0] - 1)][random.randint(0, noise_img.shape[1] - 1)][:] = 255
        img_list.append(noise_img)
    
    if '4' in techniques:
        # Gaussian blur
        blur1 = cv2.GaussianBlur(img, (9, 9), 1.5)
        blur2 = cv2.blur(img, (11, 11), (-1, -1))
        img_list.append(blur1)
        img_list.append(blur2)
    
    if '5' in techniques:
        # Lighting
        contrast = 1       # Contrast
        brightness = 100   # Brightness
        light1 = cv2.addWeighted(img, contrast, img, 0, brightness)
        light2 = cv2.addWeighted(img, 1.5, img, 0, 50)
        img_list.append(light1)
        img_list.append(light2)
    
    if '6' in techniques:
        # Affine transformation
        rows, cols = img.shape[:2]
        point1 = np.float32([[50, 50], [300, 50], [50, 200]])
        point2 = np.float32([[10, 100], [300, 50], [100, 250]])
        M = cv2.getAffineTransform(point1, point2)
        affine = cv2.warpAffine(img, M, (cols, rows), borderValue=(255, 255, 255))
        img_list.append(affine)
    
    if '7' in techniques:
        # Translation
        M = np.array([[1, 0, -100], [0, 1, -50]], dtype=np.float32)
        translated = cv2.warpAffine(img, M, (cols, rows))
        img_list.append(translated)
    
    return img_list

if __name__ == '__main__':
    input_path = input("Please enter the image path: ")
    print("Please select the data augmentation techniques you want to use, separated by commas: ")
    print("1: Flip")
    print("2: Rotate")
    print("3: Noise")
    print("4: Gaussian blur")
    print("5: Lighting")
    print("6: Affine transformation")
    print("7: Translation")
    techniques = input().split(',')
    
    for img_path in glob.glob(os.path.join(input_path, '*.jpg')):
        img = cv2.imread(img_path)
        augmented_images = data_augmentation(img, techniques)
        
        img_name = os.path.basename(img_path).split('.')[0]
        save_dir = os.path.dirname(img_path)
        
        for i, aug_img in enumerate(augmented_images):
            save_path = os.path.join(save_dir, f"{img_name}_aug{i}.jpg")
            cv2.imwrite(save_path, aug_img)
            print(f"Saved augmented image: {save_path}")