from re import S
from Avaday.View.Design.gui import Ui_Dialog
import sys
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog, QVBoxLayout, QWidget
from Avaday.View.Widgets.drag_n_drop import DragNDropInput
from Avaday.View.Widgets.generated_picture import GeneratedOutput
from Avaday.View.WidgetHandlers.draw_walks import ImageUpdater
import shutil
from pathlib import Path
from Avaday.config import ROOT_DIR


class MainWidget(QWidget):
    """
    display ui elements

    S - display ui widgets. Doesn't change at all (only its widgets change)

    O - can be extended and adjusted via built-in functions without need for modification

    L - Preserves interface of QWidget

    I - has a single interface inherited from QWidget

    D - does not use lower-level modules
    """
    def __init__(self, ui: Ui_Dialog):
        super().__init__()
        # add drag'n'drop widget to dialog
        self.drag_n_drop = DragNDropInput()
        ui.widget_drag_n_drop.setLayout(QVBoxLayout())
        ui.widget_drag_n_drop.layout().addWidget(self.drag_n_drop)

        # add image updater to dialog
        # connect it to drag'n'drop widget
        self.updater = ImageUpdater(self.drag_n_drop)

        # add generated picture widget to dialog
        # connect it to image updater
        self.picture = GeneratedOutput(self.updater)

        ui.widget_generated_output.setLayout(QVBoxLayout())
        ui.widget_generated_output.layout().addWidget(self.picture)

        self.image_save_dialog = ImageSaveDialog(self.updater)

        ui.button_save_as.clicked.connect(self.image_save_dialog.save_as)

    
class ImageSaveDialog(QWidget):
    """
    handle "Save as" click

    save picture using 
    
    S - open file save dialog. Change only on signal from main window

    O - can be extended and adjusted via built-in functions without need for modification

    L - Preserves interface of QWidget

    I - has a single interface inherited from QWidget

    D - does not use lower-level modules
    """
    def __init__(self, updater: ImageUpdater):
        super().__init__()
        self.updater = updater

    def save_as(self, ev):
        name = Path(self.updater.path_to_generated_image).stem
        file_name, _ = QFileDialog.getSaveFileName(parent=self, caption='Save avatar', directory=f"./{name}.png",
            initialFilter="Images (*.png *.jpg *jpeg)")
        if file_name:
            shutil.copy2(src=self.updater.path_to_generated_image, dst = file_name)



def run():
    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        app = QApplication([])
        Dialog = QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()

        main = MainWidget(ui=ui)

        sys.exit(app.exec())

def test_run():
    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        app = QApplication([])
        Dialog = QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()

        main = MainWidget(ui=ui)

        # set initial picture
        main.drag_n_drop.set_image(f"{ROOT_DIR}/resources/test_images/parrot.png")
        sys.exit(app.exec())

if __name__ == "__main__":
    run()
