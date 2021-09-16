import sys

from PyQt6.QtWidgets import QApplication
from pyqtgraph.Qt import QtCore

# ------- plotting walks
from Avaday.View.draw_point_cloud import draw_point_cloud
from Avaday.View.draw_walks import Draw

def run_view():
    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        Draw()
        QApplication.instance().exec()

if __name__ == "__main__":
    draw_point_cloud()
    QApplication.instance().exec()