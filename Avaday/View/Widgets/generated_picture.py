from Avaday.View.draw_walks import ImageUpdater
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSlot
from PyQt6.QtGui import QPixmap

from Avaday.View.Widgets.view_space import ViewSpace

class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setText('\n\n Output Image Appears Here \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')

    def setPixmap(self, image):
        super().setPixmap(image)

class GeneratedPicture(QWidget):
    """shows a picture, when provided with a file path"""
    def __init__(self, updater: ImageUpdater):
        super().__init__()
        self.resize(400, 400)
        mainLayout = QVBoxLayout()

        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)

        self.setLayout(mainLayout)
        self.show()

        updater.new_generated_picture.connect(self.update_image)
    
    def update_image(self, file_path):
        self.photoViewer.setPixmap(QPixmap(file_path))

if __name__ == "__main__":
    if (sys.flags.interactive != 1):
        app = QApplication(sys.argv)
        demo = GeneratedPicture()
        app.exec()