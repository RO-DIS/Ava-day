from re import S
from Avaday.View.Design.gui import Ui_Dialog
import sys
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog, QVBoxLayout, QWidget
from Avaday.View.Widgets.drag_n_drop import DragNDropInput
from Avaday.View.Widgets.generated_picture import GeneratedPicture
from Avaday.View.draw_walks import ImageUpdater
import shutil

class Custom(QWidget):
    def __init__(self, ui: Ui_Dialog):
        super().__init__()
        # add drag'n'drop widget to dialog
        self.dnd = DragNDropInput()
        ui.widget_drag_n_drop.setLayout(QVBoxLayout())
        ui.widget_drag_n_drop.layout().addWidget(self.dnd)

        self.upd = ImageUpdater(self.dnd)

        # add generated picture widget to dialog
        self.pic = GeneratedPicture(self.upd)
        ui.widget_generated_output.setLayout(QVBoxLayout())
        ui.widget_generated_output.layout().addWidget(self.pic)

        ui.button_save_as.clicked.connect(self.save_as)

    def save_as(self, ev):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Open File', './', "Image (*.png *.jpg *jpeg)")
        if file_name:
            shutil.copy2(src=self.upd.path_to_saved_image, dst = file_name)



if __name__ == "__main__":
    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        app = QApplication([])
        Dialog = QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()

        custom = Custom(ui=ui)

        sys.exit(app.exec())

