# -*- coding: utf-8 -*-
"""
# @Time : 9/13/2022 3:18 PM
# @Author : rohan.ijare
"""
import random
import glob
import os
import shutil


def copyfiles(fil, root_dir):
    basename = os.path.basename(fil)
    filename = os.path.splitext(basename)[0]

    temp = fil
    dest = os.path.join(root_dir, image_dir, f"{filename}.jpg")
    shutil.copyfile(temp, dest)

    temp = os.path.join(label_dir, f"{filename}.text")
    dest = os.path.join(root_dir, label_dir, f"{filename}.txt")

    if os.path.exists(temp):
        shutil.copyfile(temp, dest)


label_dir = "labels/"
image_dir = "images/"
lower_limit = 0

files = glob.glob(os.path.join(image_dir, '*.jpg'))

random.shuffle(files)
folders = {"train": 0.8, "val": 0.1, "test": 0.1}
check_sum = sum([folders[x] for x in folders])

assert check_sum == 1.0, "Split proportion is not equal to 0.1"

for folder in folders:
    os.mkdir(folder)
    temp_label_dir = os.path.join(folder, label_dir)
    os.mkdir(temp_label_dir)

    temp_img_dir = os.path.join(folder, image_dir)
    os.mkdir(temp_img_dir)

    limit = round(len(files) * folders[folder])
    for fil in files[lower_limit: lower_limit + limit]:
        copyfiles(fil, folder)
    lower_limit = lower_limit + limit
