from numpy.core.fromnumeric import trace
from Avaday.View.get_point_cloud import z_grid, colors
from Avaday.config import BOARD_SIZE, np, ROOT_DIR, NUMBER_OF_PATHS
from Avaday.View.config import LINE_WIDTH
from vispy import app, visuals, scene
from vispy.scene.visuals import Line

# pyline: disable=no-member
""" plot3d using existing visuals : LinePlotVisual """

import numpy as np
import sys


# build canvas
canvas = scene.SceneCanvas(keys='interactive', title='plot3d', show=True)

# Add a ViewBox to let the user zoom/rotate
view = canvas.central_widget.add_view()
view.camera = 'turntable'
view.camera.fov = 60
view.camera.distance = 100

def draw_genetic_algorithm_walks():
    """draw walks produced by GA"""
    f = open(f"{ROOT_DIR}/resources/paths/path.csv", "r")
    for _ in range(NUMBER_OF_PATHS):
        walk = np.loadtxt(fname=f, delimiter=",", max_rows=2).astype(int)
        draw_walk(*walk)


def draw_walk(xs, ys):
    zs = z_grid[xs * BOARD_SIZE + ys]
    points = np.array([xs, ys, zs]).T
    
    color = colors[xs * BOARD_SIZE + ys]
    
    Line(pos=points, width=5.0, color=color, parent=view.scene)


if __name__ == '__main__':
    draw_genetic_algorithm_walks()
    if sys.flags.interactive != 1:
        app.run()

