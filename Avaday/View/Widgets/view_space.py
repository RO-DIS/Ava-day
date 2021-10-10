from PyQt6.QtCore import pyqtSignal
import PyQt6.QtCore
import pyqtgraph.opengl as gl

from Avaday.View.config import BOARD_SIZE, VIEW_HEIGHT, VIEW_ELEVATION, \
    VIEW_AZIMUTH, BACKGROUND_COLOR, WINDOW_WIDTH, WINDOW_HEIGHT

# TODO

class ViewSpace(gl.GLViewWidget):
    def __init__(self):
        super().__init__()
        self.pan(BOARD_SIZE//2,BOARD_SIZE//2,0)
        self.setCameraPosition(distance=VIEW_HEIGHT, elevation=VIEW_ELEVATION, azimuth=VIEW_AZIMUTH)
        self.setBackgroundColor(BACKGROUND_COLOR)
        self.setFixedWidth(WINDOW_WIDTH)
        self.setFixedHeight(WINDOW_HEIGHT)
        self.show()

    def setCameraPosition(self, pos=None, distance=None, elevation=None, azimuth=None):
        if pos is not None:
            self.opts['center'] = pos
        if distance is not None:
            self.opts['distance'] = distance
        if elevation is not None:
            self.opts['elevation'] = elevation
        if azimuth is not None:
            self.opts['azimuth'] = azimuth
        self.update()
    
    mouse_moved = pyqtSignal()
    def mouseReleaseEvent(self, ev):
        self.mouse_moved.emit()

    wheel_scrolled = pyqtSignal()
    def wheelEvent(self, ev):
        delta = ev.angleDelta().x()
        if delta == 0:
            delta = ev.angleDelta().y()
        if (ev.modifiers() & PyQt6.QtCore.Qt.KeyboardModifier.ControlModifier):
            self.opts['fov'] *= 0.999**delta
        else:
            self.opts['distance'] *= 0.999**delta
        self.update()
        self.wheel_scrolled.emit()