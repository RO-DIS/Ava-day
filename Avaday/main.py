import sys
from PyQt6.QtWidgets import QApplication
from pyqtgraph.Qt import QtCore

from Avaday.View.draw_walks import LineDrawer

if __name__ == "__main__":
    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        LineDrawer()
        QApplication.instance().exec()