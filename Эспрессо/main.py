import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.reload_table()

    def reload_table(self):
        result = self.con.cursor().execute(
            f"""SELECT DISTINCT coffe.id, coffe.name, roasting.degree, state.state,
                    coffe.taste, coffe.price, coffe.volume
                FROM coffe 
                    JOIN roasting ON roasting.id = coffe.roasting
                    JOIN state ON state.id = coffe.state_type""").fetchall()
        for i in result:
            print(i)
        title = ["ID", "Сорт", "Обжарка", "Состояние", "Вкус", "Цена", "Объём"]
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setHorizontalHeaderLabels(title)
        for i, row in enumerate(result):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())
