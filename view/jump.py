from globals.globals import np
from PyQt5 import QtTest

from view.get_point_cloud import z_grid
from view.parameters import board_size, min_speed_boost, max_speed_boost, time_frames_in_jump, g, shortest_jump, line_width, \
    real_time_path_drawing_enabled, line_delay, default_shift

from view.get_point_cloud import colors
import pyqtgraph.opengl as gl


def shift_points(points, shift=default_shift):
    """shifts points along some axis by given length"""
    return points - shift


def signed_height_difference(x1, y1, x2, y2):
    return z_grid[x2 * board_size + y2] - z_grid[x1 * board_size + y1]


def unsigned_height_difference(self, x1, y1, x2, y2):
    return np.abs(self.signed_height_difference(x1, y1, x2, y2))


def sufficient_speed(height_difference):
    """selects appropriate random speeds
    for jumps from higher to lower blocks and vice-versa"""
    return sufficient_vertical_speed(
        (2 if height_difference < 0 else height_difference) + np.random.randint(min_speed_boost, max_speed_boost))


def sufficient_vertical_speed(height):
    """sufficient speed to reach given height if launched vertically"""
    return np.sqrt(2 * g * height)


def get_points_of_jump(x, y, x_next, y_next):
    xs = shift_points(np.linspace(x, x_next, time_frames_in_jump))
    ys = shift_points(np.linspace(y, y_next, time_frames_in_jump))
    zs = get_jump_zs(x, x_next, y, y_next)
    return np.array([xs, ys, zs]).T


def get_jump_zs(x, x_next, y, y_next):
    dx, dy = x_next - x, y_next - y
    dz = signed_height_difference(x, y, x_next, y_next)
    speed = sufficient_speed(dz)
    euclidean_distance = np.sqrt(dx ** 2 + dy ** 2)
    if euclidean_distance > 2:
        print(x, x_next, y, y_next)
    theta = calculate_theta(dz, euclidean_distance, speed)
    times = np.linspace(0, euclidean_distance / (np.cos(theta) * speed), time_frames_in_jump)

    def z(time):
        return speed * np.sin(theta) * time - (g * time ** 2) / 2

    zs = z_grid[x * board_size + y] + z(times)

    return zs


def shorten_trajectory():
    """select trajectory modifier"""
    return -1 if shortest_jump else 1


def calculate_theta(dz, euclidean_distance, speed):
    """calculate launch angle"""
    jump_trajectory_shortener = shorten_trajectory()
    return np.arctan(
        (
                speed ** 2
                + jump_trajectory_shortener
                * np.sqrt(
            speed ** 4 - g * (g * euclidean_distance ** 2 + 2 * dz * speed ** 2)
        )
        )
        / (g * euclidean_distance)
    )


def get_coordinate_color(x, y):
    return colors[x * board_size + y]


import view.app

widget = view.app.widget


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
