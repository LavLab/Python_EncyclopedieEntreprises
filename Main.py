import os
import json
import sys
import shutil
from datetime import datetime
from fpdf import FPDF

from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QInputDialog, QLineEdit ,QTreeWidget, QTreeWidgetItem, QFileSystemModel
from PyQt5.QtCore import QDate, QTimer
from PyQt5.QtGui import QIcon, QPixmap

from GenPDF import GenPDF
from cls_Contact import cls_Contact

from uiMainWindow import Ui_MainWindow
from uiDialogCONTACTS import Ui_DialogCONTACT
from uiDialogABOUT import Ui_DialogABOUT

G_CV=""
G_LM=""
G_Formation=""
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

def Tab_Envoyer_Envoyer():
    global G_CV
    global G_LM
    global G_Formation
    
    ui.envoyer_label_pdf.setText("ENVOYER")
    
    if ui.envoyer_checkBox_cv.isChecked():
        G_CV=".\\ressources\\CV_CSIA.pdf"
    if ui.envoyer_checkBox_lm.isChecked():
        G_LM=".\\ressources\\LM_CSIA.pdf"
        GenPDF(G_LM,ui.contacts_input_entreprise.text(),ui.contacts_input_contact.text(),ui.contacts_textEdit_adresse.toPlainText(),ui.contacts_combobox_sexe.currentIndex())
    if ui.envoyer_checkBox_formation.isChecked():
        G_Formation=".\\ressources\\FORMATION_CSIA.pdf"

def Tab_Envoyer_Visualiser():
    global G_CV
    global G_LM
    global G_Formation
    
    if ui.envoyer_checkBox_cv.isChecked():
        G_CV=".\\ressources\\CV_CSIA.pdf"
    if ui.envoyer_checkBox_lm.isChecked():
        G_LM=".\\ressources\\LM_CSIA.pdf"
        GenPDF(G_LM,ui.contacts_input_entreprise.text(),ui.contacts_input_contact.text(),ui.contacts_textEdit_adresse.toPlainText(),ui.contacts_combobox_sexe.currentIndex())
    if ui.envoyer_checkBox_formation.isChecked():
        G_Formation=".\\ressources\\FORMATION_CSIA.pdf"
    
    select=dialogCONTACT.ui.contacts_list
        
    ui.envoyer_label_pdf.setText("VISUALISER")

def Tab_Envoyer():
    ui.envoyer_btn_selectionner.clicked.connect(f_dialogCONTACT)
    ui.envoyer_btn_visualiser.clicked.connect(Tab_Envoyer_Visualiser)
    ui.envoyer_btn_envoyer.clicked.connect(Tab_Envoyer_Envoyer)

def Tab_ChargerContactsClicked(it,col):
    dialogCONTACT.close()
    for value in list_contact:
        if str(value) == str(it.text(col)):
            ui.contacts_input_entreprise.setText(str(list_contact[value].c_entreprise))
            ui.contacts_combobox_sexe.setCurrentIndex(int(list_contact[value].c_sexe))                
            ui.contacts_input_contact.setText(str(list_contact[value].c_contact))
            ui.contacts_input_mail.setText(str(list_contact[value].c_mail))
            ui.contacts_input_telephone.setText(str(list_contact[value].c_telephone))
            ui.contacts_textEdit_adresse.setPlainText(str(list_contact[value].c_adresse))
            ui.contacts_textEdit_commentaire.setPlainText(str(list_contact[value].c_commentaire))
            break
    
def Tab_ChargerList():
    global list_contact
    
    with open('./ressources/Entreprises.json') as json_file:
        data = json.load(json_file)
    for key, value in data.items():
        for item in value:
            list_contact[str(item['ENTREPRISE'])]=cls_Contact(str(item['ENTREPRISE']),int(item['SEXE']),str(item['CONTACT']),str(item['ADRESSE']),str(item['MAIL']),str(item['TELEPHONE']),str(item['COMMENTAIRE']))
    return list_contact

def Tab_ChargerContacts():
    global list_contact
    
    dialogCONTACT.ui.contacts_list.itemClicked.connect(Tab_ChargerContactsClicked)
    
    for value in list_contact:
        ui.contacts_input_entreprise.setText(str(list_contact[value].c_entreprise))
        ui.contacts_combobox_sexe.setCurrentIndex(int(list_contact[value].c_sexe))                
        ui.contacts_input_contact.setText(str(list_contact[value].c_contact))
        ui.contacts_input_mail.setText(str(list_contact[value].c_mail))
        ui.contacts_input_telephone.setText(str(list_contact[value].c_telephone))
        ui.contacts_textEdit_adresse.setPlainText(str(list_contact[value].c_adresse))
        ui.contacts_textEdit_commentaire.setPlainText(str(list_contact[value].c_commentaire))
        dialogCONTACT.ui.contacts_list.addTopLevelItem(QTreeWidgetItem([str(list_contact[value].c_entreprise),str(list_contact[value].c_adresse)]))

def Tab_SauvegarderContacts():
    global list_contact
    
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
    list_contact=Tab_ChargerList()
    

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
    
    # - Tab_Envoyer - #
    Tab_Envoyer()
    
    # - Tab_Contacts - #
    Tab_Contacts()
    list_contact=Tab_ChargerList()
    
    sys.exit(app.exec_())
