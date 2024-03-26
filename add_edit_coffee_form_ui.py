# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddEditWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.spinBoxId = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxId.setEnabled(False)
        self.spinBoxId.setMaximum(99999999)
        self.spinBoxId.setObjectName("spinBoxId")
        self.gridLayout.addWidget(self.spinBoxId, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.pushButtonSave = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.gridLayout.addWidget(self.pushButtonSave, 7, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.pushButtonCancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.gridLayout.addWidget(self.pushButtonCancel, 7, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.textEditNameVariety = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditNameVariety.setObjectName("textEditNameVariety")
        self.gridLayout.addWidget(self.textEditNameVariety, 1, 1, 1, 1)
        self.textEditDegreeOfRoasting = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditDegreeOfRoasting.setObjectName("textEditDegreeOfRoasting")
        self.gridLayout.addWidget(self.textEditDegreeOfRoasting, 2, 1, 1, 1)
        self.textEditType = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditType.setObjectName("textEditType")
        self.gridLayout.addWidget(self.textEditType, 3, 1, 1, 1)
        self.textEditDescriptionTaste = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditDescriptionTaste.setObjectName("textEditDescriptionTaste")
        self.gridLayout.addWidget(self.textEditDescriptionTaste, 4, 1, 1, 1)
        self.doubleSpinBoxCost = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxCost.setMaximum(99999999.99)
        self.doubleSpinBoxCost.setObjectName("doubleSpinBoxCost")
        self.gridLayout.addWidget(self.doubleSpinBoxCost, 5, 1, 1, 1)
        self.doubleSpinBoxPackingVolume = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxPackingVolume.setMaximum(99999999.99)
        self.doubleSpinBoxPackingVolume.setObjectName("doubleSpinBoxPackingVolume")
        self.gridLayout.addWidget(self.doubleSpinBoxPackingVolume, 6, 1, 1, 1)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавление"))
        self.label_6.setText(_translate("MainWindow", "Цена"))
        self.pushButtonSave.setText(_translate("MainWindow", "Сохранить"))
        self.label_4.setText(_translate("MainWindow", "Тип"))
        self.label_5.setText(_translate("MainWindow", "Описание вкуса"))
        self.label_2.setText(_translate("MainWindow", "Сорт"))
        self.label.setText(_translate("MainWindow", "Номер"))
        self.label_3.setText(_translate("MainWindow", "Степень прожарки"))
        self.pushButtonCancel.setText(_translate("MainWindow", "Отмена"))
        self.label_7.setText(_translate("MainWindow", "Объем упаковки"))