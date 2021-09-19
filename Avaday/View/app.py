from PyQt6.QtWidgets import QApplication
import pyqtgraph.opengl as gl

from Avaday.View.config import BOARD_SIZE, VIEW_HEIGHT, VIEW_ELEVATION, \
    VIEW_AZIMUTH, BACKGROUND_COLOR, WINDOW_WIDTH, WINDOW_HEIGHT

application = QApplication([])
widget = gl.GLViewWidget()

# move frame of reference
widget.pan(BOARD_SIZE//2,BOARD_SIZE//2,0)

def setCameraPosition(w, pos=None, distance=None, elevation=None, azimuth=None):
    if pos is not None:
        w.opts['center'] = pos
    if distance is not None:
        w.opts['distance'] = distance
    if elevation is not None:
        w.opts['elevation'] = elevation
    if azimuth is not None:
        w.opts['azimuth'] = azimuth
    w.update()

setCameraPosition(w=widget, distance=VIEW_HEIGHT, elevation=VIEW_ELEVATION, azimuth=VIEW_AZIMUTH)

widget.setBackgroundColor(BACKGROUND_COLOR)
widget.setFixedWidth(WINDOW_WIDTH)
widget.setFixedHeight(WINDOW_HEIGHT)

widget.show()