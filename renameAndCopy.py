# Script to take a bunch of images from different folders, and put them in a single folder with unique names
import os
import shutil
import random
import string

source_folders = [
    'small0/',
    'small1/'
]
target_folder = 'images_9ago/'
prefix = ''

# Create target folder if it does not exits
os.makedirs(target_folder, exist_ok=True)


def random_name():
    return prefix.join(random.choices(string.ascii_letters + string.digits, k=6))

# Recorre todas las carpetas origen
for folder in source_folders:
    for img_file in os.listdir(folder):
        file_path = os.path.join(folder, img_file)
        if os.path.isfile(file_path) and img_file.lower().endswith('.png'):
            new_name = random_name() + '.png'
            target_path = os.path.join(target_folder, new_name)
            shutil.copy2(file_path, target_path)
            print(f'Copied: {file_path} -> {target_path}')
