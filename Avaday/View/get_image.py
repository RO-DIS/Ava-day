from PIL import Image

from Avaday.View.config import PATH_TO_IMAGE, IMAGE_SIDE, BOARD_SIZE, np


def read_image(file_path):
    """open PNG image and check it for validity"""
    image = Image.open(file_path)
    image = np.asarray(image).astype(np.float32)
    return image


def check_image_size(image):
    """check if image is RGBA square with given side"""
    assert image.shape == (IMAGE_SIDE, IMAGE_SIDE, 4)


def read_valid_image(file_path):
    image = read_image(file_path)
    check_image_size(image)
    return image


def get_compressed_image(file_path):
    """select a sub-image"""
    image = read_valid_image(file_path)
    factor = IMAGE_SIDE // BOARD_SIZE
    compressed_image = image[::factor][:, ::factor]
    compressed_image = compressed_image[:BOARD_SIZE, :BOARD_SIZE]
    return compressed_image


def get_image(file_path):
    """reading RGBA image from file"""
    image = get_compressed_image(file_path)
    assert image.shape == (BOARD_SIZE, BOARD_SIZE, 4)
    return image
