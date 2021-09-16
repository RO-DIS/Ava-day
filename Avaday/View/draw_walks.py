import pyqtgraph.opengl as gl
import pyqtgraph as pg
from Avaday.config import BOARD_SIZE, np, ROOT_DIR
from Avaday.View.config import LINE_WIDTH, PATH_TO_SAVED_IMAGE, BOARD_HEIGHT, OUT_IMAGE_SIDE_IN_PIXELS
from Avaday.View.get_image import get_image
from Avaday.View.app import widget

class LineDrawer():
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
        height_max = np.amax(hashed)
        return hashed / height_max * BOARD_HEIGHT

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
        num_walks = sum(1 for _ in f)//2
        f = open(f"{ROOT_DIR}/resources/paths/path.csv", "r")
        for _ in range(num_walks):
            xs, ys = np.loadtxt(fname=f, delimiter=",", max_rows=2).astype(int)
            self.draw_walk(xs, ys)


class ScreenSaver():
    def __init__(self):
        d = widget.renderToArray((OUT_IMAGE_SIDE_IN_PIXELS, OUT_IMAGE_SIDE_IN_PIXELS))
        pg.makeQImage(d).save(PATH_TO_SAVED_IMAGE)