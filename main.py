import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


def draw_ellipse(qp):
    qp.setBrush(QColor('yellow'))
    r = random.randint(10, 300)
    qp.drawEllipse(30, 30, r + 30, r + 30)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi('UI.ui', self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Окружность')
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            draw_ellipse(qp)

    def paint(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
