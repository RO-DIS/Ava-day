from Avaday.View.get_image import get_transformed_image_path
import sys
import os
from PIL.Image import Image
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QDragEnterEvent, QDragMoveEvent, QDropEvent, QPixmap
from Avaday.config import ROOT_DIR


class InputImage(QLabel):
    """ show dropped picture

        when no picture set, show a hint text

        S - only shows hint or picture. Changes only on a new picture

        O - Only extends constructor of QLabel

        L - preserves interface of QLabel and can be used instead

        I - has a single interface inherited from QLabel

        D - does not use lower-level modules
    """

    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')

        self.setScaledContents(True)


class DragNDropInput(QWidget):
    """ widget that handles images drag'n'dropped into it

        signal when image is set

        S - only accepts image drops and signals about it. Changes only on picture drop

        O - can be extended and adjusted via built-in functions without need for modification

        L - Preserves interface of QWidget

        I - has a single interface inherited from QWidget

        D - does not use lower-level modules
    """

    def __init__(self):
        super().__init__()
        # set widget properties
        self.resize(400, 400)
        self.setAcceptDrops(True)

        layout = QVBoxLayout()

        # add image viewer
        self.photoViewer = InputImage()
        layout.addWidget(self.photoViewer)

        self.setLayout(layout)
        self.show()

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event: QDragMoveEvent):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.DropAction.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            new_path = get_transformed_image_path(file_path)
            self.set_image(new_path)
            event.accept()
        else:
            event.ignore()

    # signal when image is set
    image_set = pyqtSignal(str)

    def set_image(self, file_path):
        self.photoViewer.setPixmap(QPixmap(file_path))
        self.image_set.emit(file_path)


if __name__ == "__main__":
    if (sys.flags.interactive != 1):
        app = QApplication(sys.argv)
        demo = DragNDropInput()
        app.exec()
