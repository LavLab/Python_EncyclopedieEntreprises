import os
import json
import sys
import shutil
from datetime import datetime

from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QInputDialog, QLineEdit ,QTreeWidget, QTreeWidgetItem, QFileSystemModel
from PyQt5.QtCore import QDate, QTimer
from PyQt5.QtGui import QIcon, QPixmap

from uiMainWindow import Ui_MainWindow
from uiDialogContacts import Ui_DialogCONTACT
from uiDialogABOUT import Ui_DialogABOUT

list_contact={}

def f_dialogCONTACT():
    dialogCONTACT.ui = Ui_DialogCONTACT()
    dialogCONTACT.ui.setupUi(dialogCONTACT)
    dialogCONTACT.ui.contacts_list.setHeaderHidden(False)
    dialogCONTACT.ui.contacts_list.setColumnWidth(0,200)
    dialogCONTACT.ui.contacts_list.setColumnWidth(1,200)
    Tab_ChargerContacts()
    dialogCONTACT.show()

def f_dialogABOUT():
    dialogABOUT.ui = Ui_DialogABOUT()
    dialogABOUT.ui.setupUi(dialogABOUT)
    dialogABOUT.show()

def Menu_Bouton():
    ui.actionAbout.triggered.connect(f_dialogABOUT)

def Tab_ChargerContactsClicked(it,col):
    dialogCONTACT.close()
    for key, value in list_contact.items():
        for item in value:
            if str(item['ENTREPRISE'])==str(it.text(col)):
                ui.contacts_input_entreprise.setText(str(item['ENTREPRISE']))                
                ui.contacts_input_contact.setText(str(item['CONTACT']))
                ui.contacts_input_entreprise.setText(str(item['ENTREPRISE']))
                ui.contacts_input_mail.setText(str(item['MAIL']))
                ui.contacts_input_telephone.setText(str(item['TELEPHONE']))
                ui.contacts_textEdit_adresse.setPlainText(str(item['ADRESSE']))
                ui.contacts_textEdit_commentaire.setPlainText(str(item['COMMENTAIRE']))
                ui.contacts_combobox_sexe.setCurrentIndex(int(item['SEXE']))
                break
    

def Tab_ChargerContacts():
    global list_contact
    
    dialogCONTACT.ui.contacts_list.itemClicked.connect(Tab_ChargerContactsClicked)
    with open('./ressources/Entreprises.json') as json_file:
        data = json.load(json_file)
        list_contact=data
    for key, value in data.items():
        for item in value:
            element=QTreeWidgetItem([str(item['ENTREPRISE']),str(item['ADRESSE'])])
            dialogCONTACT.ui.contacts_list.addTopLevelItem(element)

def Tab_SauvegarderContacts():
    a_dictionary = {str(ui.contacts_input_entreprise.text()):[{"ENTREPRISE":str(ui.contacts_input_entreprise.text()),"SEXE":int(ui.contacts_combobox_sexe.currentIndex()),"CONTACT":str(ui.contacts_input_contact.text()),"ADRESSE":str(ui.contacts_textEdit_adresse.toPlainText()),"MAIL":str(ui.contacts_input_mail.text()),"TELEPHONE":str(ui.contacts_input_telephone.text()),"COMMENTAIRE":str(ui.contacts_textEdit_commentaire.toPlainText())}]}
    with open("./ressources/Entreprises.json", "r+") as file:
        data = json.load(file)
        data.update(a_dictionary)
        file.seek(0)
        json.dump(data, file)
    ui.contacts_input_entreprise.setText("")                
    ui.contacts_input_contact.setText("")
    ui.contacts_input_entreprise.setText("")
    ui.contacts_input_mail.setText("")
    ui.contacts_input_telephone.setText("")
    ui.contacts_textEdit_adresse.setPlainText("")
    ui.contacts_textEdit_commentaire.setPlainText("")
    ui.contacts_combobox_sexe.setCurrentIndex(0)
    

def Tab_Contacts():
    ui.contacts_btn_save.clicked.connect(Tab_SauvegarderContacts)
    ui.contacts_btn_rechercher.clicked.connect(f_dialogCONTACT)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # - Chargement Configuration ou Configuration par défaut - #

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # - Chargement des boites de Dialogues - #
    dialogABOUT = QtWidgets.QDialog()
    dialogCONTACT = QtWidgets.QDialog()

    # - Chargement des MessageBox - #
    msg = QMessageBox()
    msg.setWindowTitle("PyMailing")

    # - Affichage  MAIN - #
    MainWindow.show()

    # - Menu_Bouton - #
    Menu_Bouton()
    
    # - Tab_Contacts - #
    Tab_Contacts()

    sys.exit(app.exec_())
