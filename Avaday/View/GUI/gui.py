# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 370)
        self.widget_drag_n_drop = QtWidgets.QWidget(Dialog)
        self.widget_drag_n_drop.setGeometry(QtCore.QRect(30, 40, 251, 251))
        self.widget_drag_n_drop.setObjectName("widget_drag_n_drop")
        self.widget_generated_output = QtWidgets.QWidget(Dialog)
        self.widget_generated_output.setGeometry(QtCore.QRect(320, 40, 250, 250))
        self.widget_generated_output.setObjectName("widget_generated_output")
        self.button_save_as = QtWidgets.QPushButton(Dialog)
        self.button_save_as.setGeometry(QtCore.QRect(230, 300, 140, 50))
        self.button_save_as.setObjectName("button_save_as")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.button_save_as.setText(_translate("Dialog", "Save as"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())