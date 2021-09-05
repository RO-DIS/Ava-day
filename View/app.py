from PyQt6.QtWidgets import QApplication
import pyqtgraph.opengl as gl

from View.parameters import view_height, elevation, azimuth, background_color, window_width, window_height

application = QApplication([])
widget = gl.GLViewWidget()
widget.setCameraPosition(distance=view_height, elevation=elevation, azimuth=azimuth)
widget.setBackgroundColor(background_color)
widget.show()
# widget.setFixedWidth(window_width)
# widget.setFixedHeight(window_height)