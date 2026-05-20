import sys

from PySide6.QtWidgets import QApplication

from scr.client import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()

for lineEdit in [window.lineEdit_2, window.lineEdit_3, window.lineEdit_4,
                 window.lineEdit_5, window.lineEdit_6, window.lineEdit_7,
                 window.lineEdit_8, window.lineEdit_9]:
    lineEdit.textChanged.connect(window.update_textEdit_2)

window.setup_copy_buttons()

app.exec()