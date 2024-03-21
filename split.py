import os
import shutil
import random

images_folder = " "
labels_folder = " "

train_images_folder = " "
train_labels_folder = " "
test_images_folder = " "
test_labels_folder = " "

split_ratio = 0.8  # Change this to your desired ratio

image_files = [f for f in os.listdir(images_folder) if f.endswith('.jpg')]
label_files = [f for f in os.listdir(labels_folder) if f.endswith('.txt')]

assert set(f[:-4] for f in image_files) == set(f[:-4] for f in label_files)

# Shuffle file list
random.shuffle(image_files)

# Split the files into training set and test set based on the specified ratio
num_train = int(len(image_files) * split_ratio)
train_files = image_files[:num_train]
test_files = image_files[num_train:]

# Copy the files to the corresponding folders
for file in train_files:
    shutil.copy(os.path.join(images_folder, file), train_images_folder)
    shutil.copy(os.path.join(labels_folder, file[:-4] + '.txt'), train_labels_folder)

for file in test_files:
    shutil.copy(os.path.join(images_folder, file), test_images_folder)
    shutil.copy(os.path.join(labels_folder, file[:-4] + '.txt'), test_labels_folder)
