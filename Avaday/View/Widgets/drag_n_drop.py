from Avaday.View.get_image import get_cropped_rgb_image_path
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QDragEnterEvent, QDragMoveEvent, QDropEvent, QPixmap

# Class, responsible for showing text when image is not Drag'n'dropped by a user.
class ImageLabel(QLabel):
    # Setting up our widget.
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

    def setPixmap(self, image):
        super().setPixmap(image)

class DragNDropInput(QWidget):
    # Signal, which responsible for notifying about usage of a new image.
    image_set = pyqtSignal(str)

    # Setting up our widget.
    def __init__(self):
        super().__init__()
        
        self.resize(400, 400)
        self.setAcceptDrops(True)

        mainLayout = QVBoxLayout()

        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)

        self.setLayout(mainLayout)
        self.show()

    # Overwritten for our purposes event from QT
    def dragEnterEvent(self, event: QDragEnterEvent):
        # Check if drap'n'dropped object is an image
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    # Overwritten for our purposes event from QT
    def dragMoveEvent(self, event: QDragMoveEvent):
        # Check if drap'n'dropped object is an image
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    # Overwritten for our purposes event from QT
    def dropEvent(self, event: QDropEvent):
        # Check if drap'n'dropped object is an image
        if event.mimeData().hasImage:
            # Copy the dropped image to our resources folder for further usage.
            event.setDropAction(Qt.DropAction.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            new_path = get_cropped_rgb_image_path(file_path)
            self.set_image(new_path)
            
            event.accept()
        else:
            event.ignore()

    # The function, which notifies our program that we work with the image, stored at the given path.
    # Also it is responsible for showing the inputted image in the predefined place.
    def set_image(self, file_path):
        self.photoViewer.setPixmap(QPixmap(file_path))
        self.image_set.emit(file_path)

if __name__ == "__main__":
    if (sys.flags.interactive != 1):
        app = QApplication(sys.argv)
        demo = DragNDropInput()
        app.exec()
