import sys

from PyQt6.QtWidgets import QApplication
from pyqtgraph.Qt import QtCore

# ------- plotting walks
from Avaday.View.draw_point_cloud import draw_point_cloud
from Avaday.View.config import IS_VISIBLE_DOTS, IS_VISIBLE_WALKS
# from Avaday.View.walk import draw_genetic_algorithm_walks
from Avaday.View.draw_walks import draw_genetic_algorithm_walks

def run_view():
    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        if IS_VISIBLE_DOTS:
            draw_point_cloud()
        if IS_VISIBLE_WALKS:
            draw_genetic_algorithm_walks()
        QApplication.instance().exec()

if __name__ == "__main__":
    draw_point_cloud()
    QApplication.instance().exec()