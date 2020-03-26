# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\uiDialogABOUT.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogABOUT(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(429, 144)
        self.titre = QtWidgets.QLabel(Dialog)
        self.titre.setGeometry(QtCore.QRect(180, 20, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.titre.setFont(font)
        self.titre.setObjectName("titre")
        self.version = QtWidgets.QLabel(Dialog)
        self.version.setGeometry(QtCore.QRect(200, 50, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.version.setFont(font)
        self.version.setObjectName("version")
        self.titre_2 = QtWidgets.QLabel(Dialog)
        self.titre_2.setGeometry(QtCore.QRect(200, 80, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.titre_2.setFont(font)
        self.titre_2.setObjectName("titre_2")
        self.titre_3 = QtWidgets.QLabel(Dialog)
        self.titre_3.setGeometry(QtCore.QRect(200, 110, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.titre_3.setFont(font)
        self.titre_3.setObjectName("titre_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 121))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.titre.setText(_translate("Dialog", "Python ACCESS/MYSQL Import"))
        self.version.setText(_translate("Dialog", "Version 0.0.0"))
        self.titre_2.setText(_translate("Dialog", "Angel LAVIGNE"))
        self.titre_3.setText(_translate("Dialog", "Copyright (C) 2020"))
        self.label.setText(_translate("Dialog", "TextLabel"))
