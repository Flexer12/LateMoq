import sqlite3
import sys

from main_ui import Ui_MainWindow
from add_edit_coffee_form_ui import Ui_AddEditWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class AddEditWindow(QMainWindow, Ui_AddEditWindow):
    def __init__(self, main_window, title_window, mode_add, id=None):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        if title_window:
            self.setWindowTitle(title_window)
        self.mode_add = mode_add

        self.con = sqlite3.connect("data/coffee.sqlite")
        self.pushButtonSave.clicked.connect(self.save_row)
        self.pushButtonCancel.clicked.connect(self.cancel)

        if id:
            cur = self.con.cursor()
            result = cur.execute(f"SELECT * FROM coffee WHERE id={id}").fetchone()
            if result:
                self.spinBoxId.setValue(result[0])
                self.textEditNameVariety.setText(result[1])
                self.textEditDegreeOfRoasting.setText(result[2])
                self.textEditType.setText(result[3])
                self.textEditDescriptionTaste.setText(result[4])
                self.doubleSpinBoxCost.setValue(result[5])
                self.doubleSpinBoxPackingVolume.setValue(result[6])

    def save_row(self):
        if self.mode_add:
            cur = self.con.cursor()
            cur.execute(
                """INSERT INTO coffee 
                (name_variety, degree_of_roasting, type, description_taste, cost, packing_volume) 
                VALUES (?, ?, ?, ?, ?, ?)""",
                (self.textEditNameVariety.toPlainText(),
                 self.textEditDegreeOfRoasting.toPlainText(),
                 self.textEditType.toPlainText(),
                 self.textEditDescriptionTaste.toPlainText(),
                 self.doubleSpinBoxCost.value(),
                 self.doubleSpinBoxPackingVolume.value()))
            self.con.commit()
            self.main_window.update_table()
            self.main_window.show()
            self.close()
        else:
            cur = self.con.cursor()
            cur.execute(
                """UPDATE coffee 
                SET name_variety=?, degree_of_roasting=?, type=?, description_taste=?, cost=?, packing_volume=? 
                WHERE id=?""",
                (self.textEditNameVariety.toPlainText(),
                 self.textEditDegreeOfRoasting.toPlainText(),
                 self.textEditType.toPlainText(),
                 self.textEditDescriptionTaste.toPlainText(),
                 self.doubleSpinBoxCost.value(),
                 self.doubleSpinBoxPackingVolume.value(),
                 self.spinBoxId.value()))
            self.con.commit()
            self.main_window.update_table()
            self.main_window.show()
            self.close()

    def cancel(self):
        self.main_window.show()
        self.close()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("data/coffee.sqlite")
        self.pushButtonUpdate.clicked.connect(self.update_table)
        self.pushButtonAdd.clicked.connect(self.addWindow)
        self.pushButtonEdit.clicked.connect(self.editWindow)
        self.pushButtonDel.clicked.connect(self.deleteRow)

        self.update_table()

    def addWindow(self):
        self.addEditWindow = AddEditWindow(self, 'Добавление', True)
        self.addEditWindow.show()
        self.hide()

    def editWindow(self):
        selected_row = self.tableWidgetDataCoffee.currentRow()
        if selected_row != -1:
            id = self.tableWidgetDataCoffee.item(selected_row, 0).text()
            self.addEditWindow = AddEditWindow(self, 'Редактирование', False, id)
            self.addEditWindow.show()
            self.hide()

    def deleteRow(self):
        selected_row = self.tableWidgetDataCoffee.currentRow()
        if selected_row != -1:
            id = self.tableWidgetDataCoffee.item(selected_row, 0).text()
            cur = self.con.cursor()
            cur.execute("DELETE FROM coffee WHERE id=?", (id,))
            self.con.commit()
            self.update_table()

    def update_table(self):
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM coffee").fetchall()

        self.tableWidgetDataCoffee.clear()
        self.tableWidgetDataCoffee.setRowCount(len(result))

        if not result:
            return

        self.tableWidgetDataCoffee.setColumnCount(len(result[0]))
        titles = [description[0] for description in cur.description]
        titles_rus = ['номер', 'сорт', 'степень прожарки',
                      'тип', 'описание вкуса', 'цена', 'объем упаковки'][:len(titles)]
        self.tableWidgetDataCoffee.setHorizontalHeaderLabels(titles_rus)

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidgetDataCoffee.setItem(i, j, QTableWidgetItem(str(val)))


def excepthook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
