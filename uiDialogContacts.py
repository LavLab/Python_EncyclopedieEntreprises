# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\uiDialogContacts.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogCONTACT(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(515, 456)
        self.contacts_list = QtWidgets.QTreeWidget(Dialog)
        self.contacts_list.setGeometry(QtCore.QRect(10, 10, 491, 441))
        self.contacts_list.setFrameShape(QtWidgets.QFrame.Box)
        self.contacts_list.setFrameShadow(QtWidgets.QFrame.Plain)
        self.contacts_list.setLineWidth(2)
        self.contacts_list.setMidLineWidth(0)
        self.contacts_list.setProperty("showDropIndicator", False)
        self.contacts_list.setAlternatingRowColors(True)
        self.contacts_list.setUniformRowHeights(False)
        self.contacts_list.setAnimated(True)
        self.contacts_list.setObjectName("contacts_list")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "List des Contacts"))
        self.contacts_list.headerItem().setText(0, _translate("Dialog", "ENTREPRISE"))
        self.contacts_list.headerItem().setText(1, _translate("Dialog", "ADRESSE"))
