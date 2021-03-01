import sys

from random import randint

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic

from UI import Ui_Form


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        # uic.loadUi('UI.ui', self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)

    # Метод срабатывает, когда виджету надо
    # перерисовать свое содержимое,
    # например, при создании формы
    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw_flag(qp)
        # Завершаем рисование
        qp.end()

    def paint(self):
        self.repaint()

    def draw_flag(self, qp):
        # Задаем кисть
        qp.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        # Рисуем
        r = randint(100, 200)
        qp.drawEllipse((self.width() - r) // 2, (self.height() - r) // 2, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())