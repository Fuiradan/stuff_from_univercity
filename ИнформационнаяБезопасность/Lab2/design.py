# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'des.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 206)
        MainWindow.setMinimumSize(QtCore.QSize(460, 206))
        MainWindow.setMaximumSize(QtCore.QSize(460, 206))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputField = QtWidgets.QTextEdit(self.centralwidget)
        self.inputField.setGeometry(QtCore.QRect(30, 40, 241, 51))
        self.inputField.setObjectName("inputField")
        self.outputField = QtWidgets.QTextEdit(self.centralwidget)
        self.outputField.setGeometry(QtCore.QRect(30, 120, 241, 61))
        self.outputField.setReadOnly(True)
        self.outputField.setObjectName("outputField")
        self.keyField = QtWidgets.QTextEdit(self.centralwidget)
        self.keyField.setGeometry(QtCore.QRect(310, 40, 121, 51))
        self.keyField.setObjectName("keyField")
        self.encodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.encodeButton.setGeometry(QtCore.QRect(320, 110, 90, 28))
        self.encodeButton.setObjectName("encodeButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 20, 58, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 100, 58, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 20, 58, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.decodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.decodeButton.setGeometry(QtCore.QRect(320, 140, 90, 28))
        self.decodeButton.setObjectName("decodeButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lab №2 - Шифр Виженера "))
        self.encodeButton.setText(_translate("MainWindow", "Encode"))
        self.label.setText(_translate("MainWindow", "Ввод"))
        self.label_2.setText(_translate("MainWindow", "Вывод"))
        self.label_3.setText(_translate("MainWindow", "Ключ"))
        self.decodeButton.setText(_translate("MainWindow", "Decode"))
