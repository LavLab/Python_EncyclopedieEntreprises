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

def f_dialogABOUT():
    dialogABOUT.ui = Ui_DialogABOUT()
    dialogABOUT.ui.setupUi(dialogABOUT)
    dialogABOUT.show()

def Menu_Bouton():
    ui.actionAbout.triggered.connect(f_dialogABOUT)

def Tab_ChargerContacts():
    pass

def Tab_SauvegarderContacts(pEntreprise,pSexe,pContact,pAdresse,pMail,pTelephone):
    a_dictionary = {str(pEntreprise):[{"ENTREPRISE":str(pEntreprise),"SEXE":int(pSexe),"CONTACT":str(pContact),"ADRESSE":str(pAdresse),"MAIL":str(pMail),"TELEPHONE":str(pTelephone),}]}
    with open("./ressources/Entreprises.json", "r+") as file:
        data = json.load(file)
        data.update(a_dictionary)
        file.seek(0)
        json.dump(data, file)

def Tab_Contacts():
    Tab_ChargerContacts()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # - Chargement Configuration ou Configuration par défaut - #

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # - Chargement des boites de Dialogues - #
    dialogABOUT = QtWidgets.QDialog()

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
