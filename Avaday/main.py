import sys
from PyQt6.QtWidgets import QApplication
from pyqtgraph.Qt import QtCore

from Avaday.View.draw_walks import LineDrawer, ScreenSaver
from Avaday.View.Widgets.view_space import ViewSpace

if __name__ == "__main__":
    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        app = QApplication([])
        widget = ViewSpace()
        LineDrawer(widget)
        ScreenSaver(widget)
        app.exec()