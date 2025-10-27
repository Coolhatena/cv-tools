""" Script to take a bunch of images from different folders, and put them in a single folder with unique names """

import os
import shutil
import random
import string

# The names of the folders where images are stored
source_folders = [
    'cable/',
    'caja/',
    'manual/',
    'teclado/',
    'teclado_bolsa/',
]
target_folder = 'images/'
extension = '.jpg' # image type

# Create target folder if it does not exits
os.makedirs(target_folder, exist_ok=True)

def random_name(prefix):
    return prefix + ''.join(random.choices(string.ascii_letters + string.digits, k=6))


for folder in source_folders:
    for img_file in os.listdir(folder):
        file_path = os.path.join(folder, img_file)
        if os.path.isfile(file_path) and img_file.lower().endswith(extension):
            new_name = random_name(folder[:-1]) + extension
            target_path = os.path.join(target_folder, new_name)
            shutil.copy2(file_path, target_path)
            print(f'Copied: {file_path} -> {target_path}')
