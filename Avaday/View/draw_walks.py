from Avaday.View.get_point_cloud import z_grid, colors
from Avaday.config import BOARD_SIZE, np, ROOT_DIR, NUMBER_OF_PATHS
import Avaday.View.app
from Avaday.View.config import LINE_WIDTH

widget = Avaday.View.app.widget
from Avaday.View.get_image import get_image
import pyqtgraph.opengl as gl

class Draw():
    MAX_HEIGHT = 20

    def __init__(self):
        self.image = get_image()
        self.z_grid = self.get_z_grid(self.image)
        self.draw_genetic_algorithm_walks()

    def hash_rgba_to_height(self, image):
        r,g,b,a = image.T
        hashed = r ** 0.2 + g ** 0.5 + b ** 0.6
        max_height = np.amax(hashed)
        return hashed / max_height * self.MAX_HEIGHT

    def get_z_grid(self, image):
        """return z-coordinates of grid points"""
        flat_image = np.reshape(a=image, newshape=(image.shape[0] ** 2, 4))
        z_grid = self.hash_rgba_to_height(flat_image)
        return z_grid

    def draw_walk(self, xs, ys):
        zs = z_grid[xs * BOARD_SIZE + ys]
        points = np.array([xs, ys, zs]).T
        color = colors[xs * BOARD_SIZE + ys]
        
        for i in range(len(points)-1):
            line = gl.GLLinePlotItem()
            line.setGLOptions("translucent")
            line.setData(pos=np.array([points[i],points[i+1]]), color=tuple(color[i]), width=LINE_WIDTH)

            widget.addItem(line)

    def draw_genetic_algorithm_walks(self):
        """draw walks produced by GA"""
        f = open(f"{ROOT_DIR}/resources/paths/path.csv", "r")
        for _ in range(NUMBER_OF_PATHS):
            xs, ys = np.loadtxt(fname=f, delimiter=",", max_rows=2).astype(int)
            self.draw_walk(xs, ys)