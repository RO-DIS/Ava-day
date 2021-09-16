from Avaday.config import BOARD_SIZE, np, ROOT_DIR, NUMBER_OF_PATHS
import Avaday.View.app
from Avaday.View.config import LINE_WIDTH, PATH_TO_SAVED_IMAGE

widget = Avaday.View.app.widget
from Avaday.View.get_image import get_image
import pyqtgraph.opengl as gl
import pyqtgraph as pg

class LineDrawer():
    MAX_HEIGHT = 20

    def __init__(self):
        image = get_image()
        flat_image = self.get_flat_image(image)
        self.colors = self.get_normalized_colors(flat_image)
        self.zs = self.get_zs(flat_image)
        self.draw_walks()

    def get_flat_image(self, image):
        return np.reshape(a=image, newshape=(image.shape[0] ** 2, 4))

    def get_normalized_colors(self, image):
        return (image / 255.).astype(np.float32)

    def get_zs(self, image):
        r,g,b,a = image.T
        hashed = r ** 0.2 + g ** 0.5 + b ** 0.6
        max_height = np.amax(hashed)
        return hashed / max_height * self.MAX_HEIGHT

    def draw_walk(self, xs, ys):
        zs = self.zs[xs * BOARD_SIZE + ys]
        points = np.array([xs, ys, zs]).T
        color = self.colors[xs * BOARD_SIZE + ys]
        
        line = gl.GLLinePlotItem()
        line.setGLOptions("translucent")
        line.setData(pos=points, color=color, width=LINE_WIDTH)

        widget.addItem(line)

    def draw_walks(self):
        """draw walks produced by GA"""
        f = open(f"{ROOT_DIR}/resources/paths/path.csv", "r")
        for _ in range(NUMBER_OF_PATHS):
            xs, ys = np.loadtxt(fname=f, delimiter=",", max_rows=2).astype(int)
            self.draw_walk(xs, ys)


class ScreenSaver():
    def __init__(self):
        d = widget.renderToArray((2048, 2048))
        pg.makeQImage(d).save(PATH_TO_SAVED_IMAGE)