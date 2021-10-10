from pathlib import Path
from PyQt6.QtWidgets import QWidget
from Avaday.Widgets.drag_n_drop import DragNDropInput
from PyQt6.QtCore import pyqtSlot, pyqtSignal
import pyqtgraph.opengl as gl
import pyqtgraph as pg
from Avaday.config import ROOT_DIR
from Avaday.config import LINE_WIDTH, OUT_IMAGE_SIDE_IN_PIXELS
from Avaday.Widgets.view_space import ViewSpace
from Avaday.Handlers.data_handlers import DataFromImageExtractor, LineComposer

class LineDrawer():
    """
    take widget, path to image

    use image to get 3D-line

    add 3D-line to widget

    S - only adds line to widget. Changes only on creation

    O - can be extended and adjusted via built-in functions without need for modification

    L - Does not participate in inheritance hierarchy

    I - No need for interface. Data can be accessed as any variable

    D - does not use lower-level modules, only an independent class for image updates
    """

    def __init__(self, widget, path):
        self.widget = widget

        # extract data from image
        image_data = DataFromImageExtractor(path)
        colors = image_data.colors
        zs = image_data.zs

        # compose line with given data
        line = LineComposer(zs, colors)
        points = line.points
        colors = line.colors

        self.__draw_walk(points, colors)

    def __draw_walk(self, points, colors):

        line = gl.GLLinePlotItem()
        line.setGLOptions("translucent")

        line.setData(pos=points, color=colors,
                     width=LINE_WIDTH, mode='line_strip')

        self.widget.addItem(line)


class ScreenSaver():
    """
    take widget, path to new image file

    save space view to this new file

    S - only saves an image. Changes only on creation

    O - Is too small to care

    L - Does not participate in inheritance hierarchy

    I - No need for interface. Data can be accessed as any variable

    D - does not use lower-level modules, only an independent class for image updates
    """

    def __init__(self, widget, path):
        d = widget.renderToArray(
            (OUT_IMAGE_SIDE_IN_PIXELS, OUT_IMAGE_SIDE_IN_PIXELS))
        pg.makeQImage(d).save(path)


class ImageUpdater(QWidget):
    """
    re-send signals from drag'n'drop widget and space view widget to output widget

    S - only handles signals from widgets. Changes only on creation

    O - Is too small to care

    L - Does not participate in inheritance hierarchy

    I - No need for interface. Data can be accessed as any variable

    D - does not use lower-level modules, only an independent class for image updates
    """

    # if want to use signals, inherit from QWidget or similar
    def __init__(self, dnd: DragNDropInput):
        super().__init__()

        self.view_space = None
        dnd.image_set.connect(self.on_new_picture)

        Path(f"{ROOT_DIR}/resources/output_images/").mkdir(parents=True, exist_ok=True)

    def handle_view_space(self):
        if self.view_space:
            self.view_space.close()

        self.view_space = ViewSpace()
        self.view_space.mouse_moved.connect(self.update_generated_picture)
        self.view_space.wheel_scrolled.connect(self.update_generated_picture)

    @pyqtSlot(str)
    def on_new_picture(self, path):
        """
        call function to hangle view space

        update path for image saving

        up
        """
        self.handle_view_space()

        LineDrawer(self.view_space, path)

        picture_name = Path(path).stem
        self.path_to_generated_image = f"{ROOT_DIR}/resources/output_images/{picture_name}.png"

        self.update_generated_picture()

    on_generated_picture = pyqtSignal(str)

    def update_generated_picture(self):
        """
        save new image and emit signal with path to this image
        """
        ScreenSaver(self.view_space, self.path_to_generated_image)
        self.on_generated_picture.emit(self.path_to_generated_image)
