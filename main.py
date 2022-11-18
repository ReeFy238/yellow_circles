import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow
from random import randint


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.paint()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            for j in range(randint(1, 10)):
                qp.setBrush(QColor(QColor(randint(0, 255), randint(0, 255), randint(0, 255))))
                n = randint(1, 300)
                qp.drawEllipse(n, n, n, n)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
