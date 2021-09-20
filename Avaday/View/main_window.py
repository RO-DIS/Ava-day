from Avaday.View.GUI.gui import Ui_Dialog
import sys
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout
from Avaday.View.app import GeneratedPictureWidget
from Avaday.View.draw_walks import LineDrawer, ScreenSaver
from Avaday.View.GUI.drag_n_drop import DragNDropWidget, ImageLabel


class Custom():
    def __init__(self, ui: Ui_Dialog):
        # add drag'n'drop widget to dialog
        self.dnd = DragNDropWidget()
        ui.widget_drag_n_drop.setLayout(QVBoxLayout())
        ui.widget_drag_n_drop.layout().addWidget(self.dnd)

        pass


if __name__ == "__main__":
    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        app = QApplication([])
        Dialog = QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()

        Custom(ui=ui)

        sys.exit(app.exec())

