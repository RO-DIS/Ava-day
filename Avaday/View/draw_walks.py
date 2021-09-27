from PyQt6.QtWidgets import QWidget
from Avaday.View.Widgets.drag_n_drop import DragNDropInput
from PyQt6.QtCore import pyqtSlot, pyqtSignal
import pyqtgraph.opengl as gl
import pyqtgraph as pg
from Avaday.config import ROOT_DIR
from Avaday.View.config import \
    LINE_WIDTH, NUMBER_OF_PATHS, BOARD_HEIGHT, \
        OUT_IMAGE_SIDE_IN_PIXELS, BOARD_SIZE, np, \
        NUMBER_OF_PATHS
from Avaday.View.get_image import get_scaled_down_image
from Avaday.View.Widgets.view_space import ViewSpace

class LineDrawer():
    def __init__(self, widget, path):
        self.widget = widget
        image = get_scaled_down_image(path=path)
        flat_image = self.get_flat_image(image)
        self.colors = self.get_normalized_colors(flat_image)
        self.zs = self.get_zs(flat_image)
        self.draw_walks()

    def get_flat_image(self, image):
        return np.reshape(a=image, newshape=(image.shape[0] ** 2, 3))

    def get_normalized_colors(self, image):
        return (image / 255.).astype(np.float32)

    def get_zs(self, image):
        r,g,b = image.T
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

        self.widget.addItem(line)

    def draw_walks(self):
        f = open(f"{ROOT_DIR}/resources/paths/path.csv", "r")
        for _ in range(NUMBER_OF_PATHS):
            xs, ys = np.loadtxt(fname=f, delimiter=",", max_rows=2).astype(int)
            self.draw_walk(xs, ys)

class ScreenSaver():
    def __init__(self, widget, path):
        d = widget.renderToArray((OUT_IMAGE_SIDE_IN_PIXELS, OUT_IMAGE_SIDE_IN_PIXELS))
        pg.makeQImage(d).save(path)

from pathlib import Path

class ImageUpdater(QWidget):
    """re-sends signals from drag'n'drop and big view to small preview, manages new views and pictures"""
    # if want to use signals, inherit from QWidget or similar
    def __init__(self, dnd: DragNDropInput):
        super().__init__()
        dnd.image_set.connect(self.on_new_picture)

    view_space = None

    @pyqtSlot(str)
    def on_new_picture(self, path):
        """close old big view, set new to show a new picture, connect it to pic saver, update path"""
        if self.view_space:
            self.view_space.close()
            
        self.view_space = ViewSpace()
        self.view_space.mouse_moved.connect(self.update_generated_picture)
        self.view_space.wheel_scrolled.connect(self.update_generated_picture)

        LineDrawer(self.view_space, path)

        Path(f"{ROOT_DIR}/resources/output_images/").mkdir(parents=True, exist_ok=True)
        picture_name = Path(path).stem
        self.path_to_generated_image = f"{ROOT_DIR}/resources/output_images/{picture_name}.png"

        self.update_generated_picture()

    on_generated_picture = pyqtSignal(str)
    def update_generated_picture(self):
        """save new picture and emit"""
        ScreenSaver(self.view_space, self.path_to_generated_image)
        self.on_generated_picture.emit(self.path_to_generated_image)
