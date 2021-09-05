import sys

from PyQt5.QtWidgets import QApplication
from pyqtgraph.Qt import QtCore

# ------- plotting walks
from view.draw_point_cloud import draw_point_cloud
from view.parameters import are_visible_dots
from view.walk import draw_genetic_algorithm_walks


def run_view():
    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        if are_visible_dots:
            draw_point_cloud()
        draw_genetic_algorithm_walks()
        QApplication.instance().exec_()

if __name__ == "__main__":
    draw_point_cloud()
    QApplication.instance().exec_()