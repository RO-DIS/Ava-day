from Avaday.View.get_point_cloud import z_grid, colors
from Avaday.config import BOARD_SIZE, np, ROOT_DIR, NUMBER_OF_PATHS
import Avaday.View.app
from Avaday.View.config import LINE_WIDTH

widget = Avaday.View.app.widget
import pyqtgraph.opengl as gl


def draw_genetic_algorithm_walks():
    """draw walks produced by GA"""
    f = open(f"{ROOT_DIR}/resources/paths/path.csv", "r")
    for _ in range(NUMBER_OF_PATHS):
        xs, ys = np.loadtxt(fname=f, delimiter=",", max_rows=2).astype(int)
        draw_walk(xs, ys)


def draw_walk(xs, ys):
    zs = z_grid[xs * BOARD_SIZE + ys]
    points = np.array([xs, ys, zs]).T
    
    color = colors[xs * BOARD_SIZE + ys]
    
    for i in range(len(points)-1):
        line = gl.GLLinePlotItem()
        # so that points are not transparent
        line.setGLOptions("translucent")
        line.setData(pos=np.array([points[i],points[i+1]]), color=tuple(color[i]), width=LINE_WIDTH)

        widget.addItem(line)

