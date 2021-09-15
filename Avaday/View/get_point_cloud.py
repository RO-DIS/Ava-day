from Avaday.View.config import BOARD_SIZE, board_height
from Avaday.config import np
from Avaday.View.get_image import get_image


def get_coordinate_grid():
    """get x, y grid coordinates"""
    x_grid, y_grid = np.meshgrid(
        np.arange(BOARD_SIZE), np.arange(BOARD_SIZE), indexing="ij"
    )
    return x_grid.ravel(), y_grid.ravel()


def get_rgba_to_height(image):
    """return mapping function from RGBA to height"""

    def rgba_hash(point):
        """example of hash function of rgba point"""
        return point[0] ** 0.2 + point[1] ** 0.5 + point[2] ** 0.6

    height = np.amax(np.apply_along_axis(rgba_hash, 1, image))
    return lambda rgba: rgba_hash(rgba) / height * board_height


def get_z_grid():
    """return z-coordinates of grid points"""
    image = get_image()
    flat_image = np.reshape(image, (image.shape[0] ** 2, 4))
    rgba_to_height = get_rgba_to_height(flat_image)
    z_grid = np.apply_along_axis(rgba_to_height, 1, flat_image)
    return flat_image, z_grid


def normalize_image_colors(image):
    """scale image colors into [0;1] range"""
    return (image / 255.0).astype(np.float32)


def get_point_cloud():
    x_grid, y_grid = get_coordinate_grid()
    flat_image, z_grid = get_z_grid()
    colors = normalize_image_colors(flat_image)
    return x_grid, y_grid, z_grid, colors

x_grid, y_grid, z_grid, colors = get_point_cloud()

# TODO Checked