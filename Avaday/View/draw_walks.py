from Avaday.View.Widgets.drag_n_drop import DragNDropInput
from _typeshed import Self
import PyQt6
from PyQt6.QtCore import pyqtSlot, pyqtSignal
import pyqtgraph.opengl as gl
import pyqtgraph as pg
from Avaday.config import ROOT_DIR
from Avaday.View.config import \
    LINE_WIDTH, NUMBER_OF_PATHS, PATH_TO_SAVED_IMAGE, BOARD_HEIGHT, \
        OUT_IMAGE_SIDE_IN_PIXELS, BOARD_SIZE, np, \
        NUMBER_OF_PATHS
from Avaday.View.get_image import get_image
from Avaday.View.Widgets.view_space import ViewSpace

class LineDrawer():
    def __init__(self, widget, file_path):
        self.widget = widget
        image = get_image(file_path=file_path)
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

        self.widget.addItem(line)

    def draw_walks(self):
        f = open(f"{ROOT_DIR}/resources/paths/path.csv", "r")
        for _ in range(NUMBER_OF_PATHS):
            xs, ys = np.loadtxt(fname=f, delimiter=",", max_rows=2).astype(int)
            self.draw_walk(xs, ys)

class ScreenSaver():
    def __init__(self, widget):
        d = widget.renderToArray((OUT_IMAGE_SIDE_IN_PIXELS, OUT_IMAGE_SIDE_IN_PIXELS))
        pg.makeQImage(d).save(PATH_TO_SAVED_IMAGE)

class ImageUpdater():
    def __init__(self, dnd: DragNDropInput) -> None:
        dnd.set_image.connect(self.update_saved_picture)
        pass
    
    @pyqtSlot
    def update_saved_picture(self, path):
        space = ViewSpace()
        LineDrawer(space, path)
        ScreenSaver(space)
        self.update_saved_picture(PATH_TO_SAVED_IMAGE)
        pass

    # TODO extract filename
    new_generated_picture = pyqtSignal
    def update_show_picture(self, path):
        self.new_generated_picture.emit(path)
