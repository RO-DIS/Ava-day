from Avaday.View.Handlers.widget_handlers import ImageUpdater
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap


class OutputImage(QLabel):
    """
        show generated picture

        when no picture set, show a hint text

        S - only shows hint or picture. Changes only on a new picture

        O - only extends constructor of QLabel

        L - preserves interface of QLabel and can be used instead

        I - has a single interface inherited from QLabel

        D - does not use lower-level modules
    """
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


class GeneratedOutput(QWidget):
    """
    show a picture, when provided with a file path

    change picture on signal from image updater

    S - Only shows image previews. Changes only on signal from image updater

    O - can be extended and adjusted via built-in functions without need for modification

    L - Preserves interface of QWidget

    I - has a single interface inherited from QWidget

    D - does not use lower-level modules, only an independent class for image updates
    """

    def __init__(self, updater: ImageUpdater):
        super().__init__()
        self.resize(400, 400)
        layout = QVBoxLayout()

        self.photoViewer = OutputImage()
        layout.addWidget(self.photoViewer)

        self.setLayout(layout)
        self.show()

        updater.on_generated_picture.connect(self.update_image)

    def update_image(self, file_path):
        self.photoViewer.setPixmap(QPixmap(file_path))


if __name__ == "__main__":
    if (sys.flags.interactive != 1):
        app = QApplication(sys.argv)
        demo = GeneratedOutput()
        app.exec()
