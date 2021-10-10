from pathlib import Path
from PyQt6.QtWidgets import QWidget
from Avaday.View.Widgets.drag_n_drop import DragNDropInput
from PyQt6.QtCore import pyqtSlot, pyqtSignal
import pyqtgraph.opengl as gl
import pyqtgraph as pg
from Avaday.config import ROOT_DIR
from Avaday.View.config import \
    LINE_WIDTH, NUMBER_OF_PATHS, BOARD_HEIGHT, \
    OUT_IMAGE_SIDE_IN_PIXELS, BOARD_SIZE, IMAGE_SIDE,\
    NUMBER_OF_PATHS
from Avaday.View.Widgets.view_space import ViewSpace
import numpy as np
from PIL import Image

# TODO split into files


class DataFromImageExtractor():
    """
    take image path

    extract z-coordinates and colors from image

    S - only extracts data from image. Changes only on creation

    O - can be extended and adjusted via built-in functions without need for modification

    L - Does not participate in inheritance hierarchy

    I - No need for interface. Does not have public functions, only a couple of public variables

    D - does not use lower-level modules
    """

    def __init__(self, path):
        image = self.__get_scaled_down_image(path=path)
        flat_image = self.__get_flat_image(image)

        self.colors = self.__get_normalized_colors(flat_image)
        self.zs = self.__get_zs(flat_image)

    def __get_scaled_down_image(self, path):
        img = Image.open(path)
        img = np.asarray(img).astype(np.float32)

        factor = IMAGE_SIDE // BOARD_SIZE
        img = img[::factor][:, ::factor]
        img = img[:BOARD_SIZE, :BOARD_SIZE]

        return img

    def __get_flat_image(self, image):
        return np.reshape(a=image, newshape=(image.shape[0] ** 2, 3))

    def __get_normalized_colors(self, image):
        return (image / 255.).astype(np.float32)

    def __get_zs(self, image):
        r, g, b = image.T
        hashed = r ** 0.2 + g ** 0.5 + b ** 0.6
        height_max = np.amax(hashed)
        return hashed / height_max * BOARD_HEIGHT


class LineComposer():
    """
    take z-coordinates and colors of grid points

    read x,y-coordinates 

    compose line points and colors

    S - only produces a line: points + colors. Changes only on creation

    O - is not intended to support polymorphic arguments

    L - Does not participate in inheritance hierarchy

    I - No need for interface. Does not have public functions, only a couple of public variables

    D - does not use lower-level modules
    """

    def __init__(self, zs, colors) -> None:
        xs, ys, alpha = self.__read_path()

        self.points = self.__prepare_points(xs, ys, zs, alpha)
        self.colors = self.__prepare_colors(xs, ys, colors, alpha)

    def __read_path(self):
        f = open(f"{ROOT_DIR}/resources/paths/path.csv", "r")

        X = np.array([])
        Y = np.array([])
        alpha = np.array([])

        for _ in range(NUMBER_OF_PATHS):
            xs, ys = np.loadtxt(fname=f, delimiter=",", max_rows=2).astype(int)
            xs = np.repeat(xs, 2)
            ys = np.repeat(ys, 2)
            X = np.concatenate([X, xs, xs[-1:]])
            Y = np.concatenate([Y, ys, ys[-1:]])
            alpha = np.concatenate(
                [alpha, np.array([0]), np.full((len(xs)-2), 1), np.array([0, 0])])

        return X.astype(int), Y.astype(int), alpha.astype(int)

    def __prepare_points(self, xs, ys, zs, alpha):
        zs = zs[xs * BOARD_SIZE + ys]
        for i in range(1, len(alpha)-1):
            if alpha[i-1] == 0 and alpha[i+1] == 0:
                zs[i] = -1000
        points = np.array([xs, ys, zs]).T
        return points

    def __prepare_colors(self, xs, ys, colors, alpha):
        alpha = np.array([alpha]).T
        colors = colors[xs * BOARD_SIZE + ys]
        colors = np.concatenate([np.array([[0, 0, 0]]), colors[:-1]])
        colors = np.hstack((colors, alpha))
        return colors
