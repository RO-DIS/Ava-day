from pathlib import Path
from PIL import Image

from Avaday.View.config import IMAGE_SIDE, BOARD_SIZE

import numpy as np

from Avaday.config import ROOT_DIR

# TODO

# class ImageAdapter():
#     def __init__(self) -> None:
        
def crop_center_image(img):
    """crop image to get only the central square with given image side"""
    w, h = img.size
    side = min(w, h)
    center_x = w//2
    center_y = h//2
    left_top_x = max(0, center_x-side//2)
    left_top_y = max(0, center_y-side//2)
    img = img.crop((left_top_x, left_top_y, left_top_x +
                   side - 1, left_top_y + side - 1))

    return img


def resize_image(img):
    return img.resize((IMAGE_SIDE, IMAGE_SIDE), Image.ANTIALIAS)


def convert_to_rgb(img):
    img = img.convert('RGBA')
    background = Image.new('RGBA', img.size, (0, 0, 0))
    img = Image.alpha_composite(background, img).convert('RGB')
    return img


def process_image(img):
    img = convert_to_rgb(img)
    img = crop_center_image(img)
    img = resize_image(img)
    return img


def save_image(path, img):
    p = Path(path)
    file_name = p.stem
    Path(f"{ROOT_DIR}/resources/user_images/").mkdir(parents=True, exist_ok=True)

    path_to_png = f"{ROOT_DIR}/resources/user_images/{file_name}.png"
    img.save(path_to_png, bitmap_format='png')
    return path_to_png


def get_transformed_image_path(path):
    img = process_image(Image.open(path))
    new_path = save_image(path, img)
    return new_path