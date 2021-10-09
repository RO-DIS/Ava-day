from Avaday.View.Design.gui import Ui_Dialog
import sys
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog, QVBoxLayout, QWidget
from Avaday.View.Widgets.drag_n_drop import DragNDropInput
from Avaday.View.Widgets.generated_picture import GeneratedPicture
from Avaday.View.draw_walks import ImageUpdater
import shutil
from pathlib import Path

# Class, responsible for changes of default view. Here we set up our view.
class Custom(QWidget):
    def __init__(self, ui: Ui_Dialog):
        super().__init__()
        self._setupDragNDropWidget(ui)
        self._setupImageUpdater()
        self._setupGeneratedPictureWidget()
        self._setupPictureSharingWidget()

    def _setupDragNDropWidget(self, ui: Ui_Dialog):
        self.dnd = DragNDropInput()
        ui.widget_drag_n_drop.setLayout(QVBoxLayout())
        ui.widget_drag_n_drop.layout().addWidget(self.dnd)

    def _setupGeneratedPictureWidget(self, ui: Ui_Dialog):
        self.pic = GeneratedPicture(self.upd)
        ui.widget_generated_output.setLayout(QVBoxLayout())
        ui.widget_generated_output.layout().addWidget(self.pic)

    def _setupPictureSharingWidget(self, ui: Ui_Dialog):
        ui.button_save_as.clicked.connect(self.saveAsOnClickListener)

    def _setupImageUpdater(self):
        self.upd = ImageUpdater(self.dnd)
        
        
    def saveAsOnClickListener(self, ev):
        name = Path(self.upd.path_to_generated_image).stem
        file_name, _ = QFileDialog.getSaveFileName(parent=self, caption='Save avatar', directory=f"./{name}.png",
            initialFilter="Image (*.png *.jpg *jpeg)")
        if file_name:
            shutil.copy2(src=self.upd.path_to_generated_image, dst = file_name)

# Running our app. Mostly preparing and starting of PyQt.
def run():
    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        app = QApplication([])
        Dialog = QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec())

if __name__ == "__main__":
    run()
