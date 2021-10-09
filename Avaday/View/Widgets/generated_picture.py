from Avaday.View.draw_walks import ImageUpdater
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

# Class, responsible for showing text when image is not Drag'n'dropped by a user.
class ImageLabel(QLabel):
    # Setting up our widget.
    def __init__(self):
        super().__init__()
        
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setText('\n\n Output Image Appears Here \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa;
            }
        ''')
        self.setScaledContents(True)

    def setPixmap(self, image):
        super().setPixmap(image)

# Class, responsible for showing generated image in the prepared place in the main window.
class GeneratedPicture(QWidget):
    # Setting up our widget.
    def __init__(self, updater: ImageUpdater):
        super().__init__()
        
        self.resize(400, 400)
        mainLayout = QVBoxLayout()
        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)
        self.setLayout(mainLayout)
        self.show()

        updater.on_generated_picture.connect(self.update_image)

    # Function, responsible for showing the given image in the defined place.
    def update_image(self, file_path):
        self.photoViewer.setPixmap(QPixmap(file_path))

if __name__ == "__main__":
    if (sys.flags.interactive != 1):
        app = QApplication(sys.argv)
        demo = GeneratedPicture()
        app.exec()