from pathlib import Path
from PIL import Image

from Avaday.config import IMAGE_SIDE, BOARD_SIZE

from Avaday.config import ROOT_DIR


# Almost pure functions -> no need to create a class to hold state

# Input: image path 
# Output: this transformed image path 

# Add underscores to prevent importing with 
# from M import *
# https://www.python.org/dev/peps/pep-0008/#id34

def _crop_center_image(img):
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


def _resize_image(img):
    """
    resize image to have valid sides
    """
    return img.resize((IMAGE_SIDE, IMAGE_SIDE), Image.ANTIALIAS)


def _convert_to_rgb(img):
    """
    convert to RGB, neglecting initial image properties

    set default background to black
    """
    img = img.convert('RGBA')
    background = Image.new('RGBA', img.size, (0, 0, 0))
    img = Image.alpha_composite(background, img).convert('RGB')
    return img


def _process_image(img):
    """
    apply image transformations
    """
    img = _convert_to_rgb(img)
    img = _crop_center_image(img)
    img = _resize_image(img)
    return img


def _save_image(path, img):
    """
    get image name from path

    save image in a local folder
    """
    p = Path(path)
    file_name = p.stem
    Path(f"{ROOT_DIR}/resources/user_images/").mkdir(parents=True, exist_ok=True)

    path_to_png = f"{ROOT_DIR}/resources/user_images/{file_name}.png"
    img.save(path_to_png, bitmap_format='png')
    return path_to_png


def get_transformed_image_path(path):
    """
    process image, save, and return path to the new image
    """
    img = _process_image(Image.open(path))
    new_path = _save_image(path, img)
    return new_path