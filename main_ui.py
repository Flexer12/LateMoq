# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonEdit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.gridLayout.addWidget(self.pushButtonEdit, 1, 1, 1, 1)
        self.pushButtonDel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDel.setObjectName("pushButtonDel")
        self.gridLayout.addWidget(self.pushButtonDel, 1, 2, 1, 1)
        self.pushButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.gridLayout.addWidget(self.pushButtonAdd, 1, 0, 1, 1)
        self.pushButtonUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonUpdate.setObjectName("pushButtonUpdate")
        self.gridLayout.addWidget(self.pushButtonUpdate, 2, 0, 1, 3)
        self.tableWidgetDataCoffee = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetDataCoffee.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidgetDataCoffee.setObjectName("tableWidgetDataCoffee")
        self.tableWidgetDataCoffee.setColumnCount(0)
        self.tableWidgetDataCoffee.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidgetDataCoffee, 0, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Капучино"))
        self.pushButtonEdit.setText(_translate("MainWindow", "Редактировать"))
        self.pushButtonDel.setText(_translate("MainWindow", "Удалить"))
        self.pushButtonAdd.setText(_translate("MainWindow", "Создать"))
        self.pushButtonUpdate.setText(_translate("MainWindow", "Обновить"))