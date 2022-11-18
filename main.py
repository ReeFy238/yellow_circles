import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QMainWindow()
    ex.show()
    sys.exit(app.exec())
