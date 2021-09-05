from globals.globals import np
from view.parameters import default_shift
import pyqtgraph.opengl as gl

from view.get_point_cloud import x_grid, y_grid, z_grid, colors
from view.parameters import dot_opaqueness, dot_size


def set_opaqueness_of_image_dots():
    colors[:, 3] = dot_opaqueness


def shift_points(points, shift=default_shift):
    """shifts points along some axis by given length"""
    return points - shift


def get_centered_board():
    return np.array([shift_points(x_grid), shift_points(y_grid), z_grid]).T


import view.app

widget = view.app.widget


def draw_point_cloud():
    set_opaqueness_of_image_dots()
    pos = get_centered_board()
    sp2 = gl.GLScatterPlotItem(pos=pos, color=colors, size=dot_size)
    sp2.setGLOptions("translucent")

    widget.addItem(sp2)
