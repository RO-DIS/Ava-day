from PyQt5.QtWidgets import QApplication
import pyqtgraph.opengl as gl

from view.parameters import view_height, elevation, azimuth, background_color, window_width, window_height

application = QApplication([])
widget = gl.GLViewWidget()
widget.show()
widget.setCameraPosition(distance=view_height, elevation=elevation, azimuth=azimuth)
widget.setBackgroundColor(background_color)
# widget.setFixedWidth(window_width)
# widget.setFixedHeight(window_height)