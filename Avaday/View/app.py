from PyQt6.uic.properties import QtGui
from PyQt6.QtWidgets import QApplication
import pyqtgraph.opengl as gl

from Avaday.View.config import view_height, elevation, azimuth, background_color, window_width, window_height

application = QApplication([])
widget = gl.GLViewWidget()
from View.config import BOARD_SIZE

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

setCameraPosition(w=widget, distance=view_height, elevation=elevation, azimuth=azimuth)

widget.setBackgroundColor(background_color)
widget.setFixedWidth(window_width)
widget.setFixedHeight(window_height)

widget.show()