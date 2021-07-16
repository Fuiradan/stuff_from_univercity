# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'md5.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(439, 248)
        MainWindow.setMinimumSize(QtCore.QSize(439, 248))
        MainWindow.setMaximumSize(QtCore.QSize(439, 248))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 30, 401, 101))
        self.textEdit.setObjectName("textEdit")
        self.outputField = QtWidgets.QTextEdit(self.centralwidget)
        self.outputField.setGeometry(QtCore.QRect(20, 190, 401, 31))
        self.outputField.setReadOnly(True)
        self.outputField.setObjectName("outputField")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(309, 140, 101, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 10, 58, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 170, 58, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lab №5 - md5"))
        self.pushButton.setText(_translate("MainWindow", "Преобразовать"))
        self.label.setText(_translate("MainWindow", "Данные"))
        self.label_2.setText(_translate("MainWindow", "md5 hash"))
