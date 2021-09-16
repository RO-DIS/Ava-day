from PIL import Image

from Avaday.View.config import PATH_TO_IMAGE, IMAGE_SIDE, BOARD_SIZE, np


def read_image():
    """open PNG image and check it for validity"""
    image = Image.open(PATH_TO_IMAGE)
    image = np.asarray(image).astype(np.float32)
    return image


def check_image_size(image):
    """check if image is RGBA square with given side"""
    assert image.shape == (IMAGE_SIDE, IMAGE_SIDE, 4)


def read_valid_image():
    image = read_image()
    check_image_size(image)
    return image


def get_compressed_image():
    """select a sub-image"""
    image = read_valid_image()
    factor = IMAGE_SIDE // BOARD_SIZE
    compressed_image = image[::factor][:, ::factor]
    compressed_image = compressed_image[:BOARD_SIZE, :BOARD_SIZE]
    return compressed_image


def get_image():
    """reading RGBA image from file"""
    image = get_compressed_image()
    assert image.shape == (BOARD_SIZE, BOARD_SIZE, 4)
    return image
