import sys

from PySide6.QtWidgets import QApplication

from src.client import MainWindow

app = QApplication(sys.argv)
appversion = '1.0.2'
window = MainWindow()
window.setWindowTitle(f'{window.windowTitle()} {appversion}')
window.show()

for lineEdit in [window.lineEdit_2, window.lineEdit_3, window.lineEdit_4,
                 window.lineEdit_6, window.lineEdit_7,
                 window.lineEdit_8, window.lineEdit_9]:
    lineEdit.textChanged.connect(window.update_textEdit_2)

window.setup_copy_buttons()

app.exec()
