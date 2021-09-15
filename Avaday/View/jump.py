from PyQt6 import QtTest

from Avaday.globals import np
from Avaday.View.get_point_cloud import z_grid
from Avaday.View.parameters import board_size, MINIMAL_SPEED_BOOST, MAXIMAL_SPEED_BOOST, time_frames_in_jump, g, shortest_jump, line_width, \
    real_time_path_drawing_enabled, line_delay, default_shift
from Avaday.View.get_point_cloud import colors

import pyqtgraph.opengl as gl


def shift_points(points, shift=default_shift):
    """shifts points along some axis by given length"""
    return points - shift


def get_points_of_jump(x, y, x_next, y_next):
    xs = shift_points(np.linspace(x, x_next, time_frames_in_jump))
    ys = shift_points(np.linspace(y, y_next, time_frames_in_jump))
    # zs = get_jump_zs(x, x_next, y, y_next)
    zs = z_grid[x*board_size+y]

    return np.array([xs, ys, zs]).T

def get_coordinate_color(x, y):
    return colors[x * board_size + y]


import View.app

widget = View.app.widget


def draw_jump(x, y, x_next, y_next):
    points = get_points_of_jump(x, y, x_next, y_next)
    colors = np.full((points.shape[0], 4), get_coordinate_color(x, y))

    line = gl.GLLinePlotItem()
    # so that points are not transparent
    line.setGLOptions("translucent")
    line.setData(pos=points, color=colors, width=line_width)

    widget.addItem(line)

    if real_time_path_drawing_enabled:
        QtTest.QTest.qWait(ms=line_delay)
