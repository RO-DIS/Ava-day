from PIL import Image

from Avaday.View.parameters import path_to_image, image_side, board_size
from Avaday.globals import np


def read_image():
    """open PNG image and check it for validity"""
    image = Image.open(path_to_image)
    image = np.asarray(image).astype(np.float32)
    return image


def check_image_size(image):
    """check if image is RGBA square with given side"""
    assert image.shape == tuple([image_side, image_side, 4])


def read_valid_image():
    image = read_image()
    check_image_size(image)
    return image


def get_compressed_image():
    """select a sub-image"""
    image = read_valid_image()
    factor = image_side // board_size
    compressed_image = image[::factor][:, ::factor]
    compressed_image = compressed_image[:board_size, :board_size]
    return compressed_image


def get_image():
    """reading RGBA image from file"""
    image = get_compressed_image()
    assert image.shape == (board_size, board_size, 4)
    return image
