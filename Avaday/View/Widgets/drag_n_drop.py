import sys, os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QDragEnterEvent, QDragMoveEvent, QDropEvent, QPixmap


class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')

    def setPixmap(self, image):
        super().setPixmap(image)

class DragNDropInput(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.setAcceptDrops(True)

        mainLayout = QVBoxLayout()

        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)

        self.setLayout(mainLayout)
        self.show()

        # signal when image is set
        self.image_set = pyqtSignal(str)


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
            self.set_image(file_path)

            self.call_generator(file_path)

            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        self.photoViewer.setPixmap(QPixmap(file_path))
        self.image_set.emit(file_path)



if __name__ == "__main__":
    if (sys.flags.interactive != 1):
        app = QApplication(sys.argv)
        demo = DragNDropInput()
        app.exec()
