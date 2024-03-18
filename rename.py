import os
import glob

def rename_images(directory, name):
    images = glob.glob(os.path.join(directory, "*.[pjJ][npNP][gG]*"))
    # Rename each image file
    for i, image in enumerate(images, start=1):
        extension = os.path.splitext(image)[1]
        new_name = f"{name}_{i}{extension}"
        new_path = os.path.join(directory, new_name)
        os.rename(image, new_path)
        print(f"Renamed {image} to {new_path}")

if __name__ == "__main__":
    directory = input("Enter the directory containing images: ")
    name = input("Enter the new name for images: ")
    rename_images(directory, name)