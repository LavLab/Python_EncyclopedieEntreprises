import os
import json
import sys
import shutil
from fpdf import FPDF

import pgeocode

from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QInputDialog, QLineEdit ,QTreeWidget, QTreeWidgetItem, QFileSystemModel
from PyQt5.QtCore import QDate, QTimer
from PyQt5.QtGui import QIcon, QPixmap

from GenPDF import GenPDF
from cls_Contact import cls_Contact

from uiMainWindow import Ui_uiMainWindow
from uiDialogCONTACT import UiD_uiDialogCONTACT

G_CV=""
G_LM=""
list_contact={}
list_Dialogue=[]

def f_dialogCONTACT():
    dialogCONTACT.ui = UiD_uiDialogCONTACT()
    dialogCONTACT.ui.setupUi(dialogCONTACT)
    dialogCONTACT.ui.contacts_list.setHeaderHidden(False)
    dialogCONTACT.ui.contacts_list.setColumnWidth(0,200)
    dialogCONTACT.ui.contacts_list.setColumnWidth(1,200)
    Tab_ChargerContacts()
    dialogCONTACT.show()

def Tab_ChargerContactsClicked():
    global list_Dialogue   
    list_Dialogue.clear()
    
    for item in dialogCONTACT.ui.contacts_list.selectedIndexes():
        for value in list_contact:
            if str(value) == str(item.data()):
                
                try:
                    ui.contacts_combobox_ville.clear()
                    geocode = pgeocode.Nominatim('fr')
                    code_postal = geocode.query_postal_code(str(list_contact[value].c_codepostal))
                    villes = code_postal.place_name.split(", ")
                    for ville in villes:  
                        ui.contacts_combobox_ville.addItem(ville)
                except Exception as identifier:
                    pass
                
                ui.contacts_input_entreprise.setText(str(list_contact[value].c_entreprise).upper())
                ui.contacts_combobox_sexe.setCurrentIndex(int(list_contact[value].c_sexe))                
                ui.contacts_input_contact.setText(str(list_contact[value].c_contact))
                ui.contacts_textEdit_adresse.setPlainText(str(list_contact[value].c_adresse))
                ui.contacts_input_codepostal.setValue(int(list_contact[value].c_codepostal))
                ui.contacts_combobox_ville.setCurrentIndex(int(list_contact[value].c_ville))
                ui.contacts_input_mail.setText(str(list_contact[value].c_mail))
                ui.contacts_input_telephone.setText(str(list_contact[value].c_telephone))
                
                try:
                    if not ui.contacts_input_entreprise.text() == (""):
                        l_entreprise_directory = "./ressources/"+str(ui.contacts_input_entreprise.text())
                        if os.path.exists(l_entreprise_directory+"/CV.pdf"):
                            ui.contacts_checkbox_cv.setChecked(True)
                        else:
                            ui.contacts_checkbox_cv.setChecked(False)
                        if os.path.exists(l_entreprise_directory+"/LM.pdf"):
                            ui.contacts_checkbox_lm.setChecked(True)
                        else:
                            ui.contacts_checkbox_lm.setChecked(False)
                except Exception as identifier:
                    pass

                break
            
    dialogCONTACT.close()

    
def Tab_ChargerList():
    global list_contact
    
    with open('./ressources/Entreprises.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
    for key, value in data.items():
        for item in value:
            try:
                geocode = pgeocode.Nominatim('fr')
                code_postal = geocode.query_postal_code(str(item['CP']))
                villes = code_postal.place_name.split(", ")
            except Exception as identifier:
                pass
            
            list_contact[str(item['ENTREPRISE'])]=cls_Contact(str(item['ENTREPRISE']),int(item['SEXE']),str(item['CONTACT']),str(item['ADRESSE']),int(item['CP']),int(item['VILLE']),str(villes[int(item['VILLE'])]),str(item['MAIL']),str(item['TELEPHONE']))
    return list_contact


def Tab_ChargerContacts():
    global list_contact
    dialogCONTACT.ui.contacts_btn_selectionner.clicked.connect(Tab_ChargerContactsClicked)
    
    try:                             
        for value in list_contact:                
            dialogCONTACT.ui.contacts_list.addTopLevelItem(QTreeWidgetItem([str(list_contact[value].c_entreprise),str(list_contact[value].c_adresse)+"\n"+str(list_contact[value].c_codepostal)+", "+str(list_contact[value].c_ville_name)]))
            dialogCONTACT.setWindowTitle("Liste des Contacts : "+str(len(list_contact)))
            
    except Exception as error:
        QMessageBox.setIcon(QMessageBox.Information)
        QMessageBox.setText("Une erreur est survenue !")
        QMessageBox.setDetailedText(str(error))
        QMessageBox.exec_()
        
def Tab_SauvegarderContacts():
    global list_contact
    
    if not ui.contacts_input_entreprise.text() == (""):
        try:
            a_dictionary = {
                str(ui.contacts_input_entreprise.text()):[
                    {
                    "ENTREPRISE":str(ui.contacts_input_entreprise.text()).upper(),
                    "SEXE":int(ui.contacts_combobox_sexe.currentIndex()),
                    "CONTACT":str(ui.contacts_input_contact.text()),
                    "ADRESSE":str(ui.contacts_textEdit_adresse.toPlainText()),
                    "CP":int(ui.contacts_input_codepostal.value()),
                    "VILLE":int(ui.contacts_combobox_ville.currentIndex()),
                    "MAIL":str(ui.contacts_input_mail.text()),
                    "TELEPHONE":str(ui.contacts_input_telephone.text())
                    }
                ]
            }
            
            with open("./ressources/Entreprises.json", "r+", encoding="utf-8") as file:
                data = json.load(file)
                data.update(a_dictionary)
                # file.seek(0)
                # json.dump(data, file)
                
            Tab_ContactEffacer()
            
            list_contact=Tab_ChargerList()
            
            QMessageBox.setIcon(QMessageBox.Information)
            QMessageBox.setText("Modifications enregistrées")
            QMessageBox.setDetailedText("")
            QMessageBox.exec_()
        except Exception as error:
            QMessageBox.setIcon(QMessageBox.Information)
            QMessageBox.setText("Une erreur est survenue !")
            QMessageBox.setDetailedText(str(error))
            QMessageBox.exec_()
    else:
        QMessageBox.setIcon(QMessageBox.Information)
        QMessageBox.setText("Veuillez saisir des informations")
        QMessageBox.setDetailedText("")
        QMessageBox.exec_()
    
def Tab_ContactEffacer():
    try:
        ui.contacts_input_entreprise.setText("")                
        ui.contacts_input_contact.setText("")
        ui.contacts_textEdit_adresse.setPlainText("")
        ui.contacts_input_codepostal.setValue(00000)
        ui.contacts_combobox_ville.setCurrentIndex(0)
        ui.contacts_combobox_ville.clear()
        ui.contacts_input_entreprise.setText("")
        ui.contacts_input_mail.setText("")
        ui.contacts_input_telephone.setText("")
    except Exception as error:
        QMessageBox.setIcon(QMessageBox.Information)
        QMessageBox.setText("Une erreur est survenue !")
        QMessageBox.setDetailedText(str(error))
        QMessageBox.exec_()

def Tab_ContactSupprimer():
    global list_contact
    
    try:
        if not ui.contacts_input_entreprise.text() == (""):
            l_entreprise_directory = "./ressources/"+str(ui.contacts_input_entreprise.text())
            if os.path.exists(l_entreprise_directory+"/CV.pdf"):
                os.remove(l_entreprise_directory+"/CV.pdf")
            if os.path.exists(l_entreprise_directory+"/LM.pdf"):
                os.remove(l_entreprise_directory+"/LM.pdf")
            os.remove(l_entreprise_directory)
        else:
            QMessageBox.setIcon(QMessageBox.Information)
            QMessageBox.setText("Veuillez saisir des informations")
            QMessageBox.setDetailedText("")
            QMessageBox.exec_()
    except Exception as error:
        QMessageBox.setIcon(QMessageBox.Information)
        QMessageBox.setText("Une erreur est survenue !")
        QMessageBox.setDetailedText(str(error))
        QMessageBox.exec_()

    Tab_ContactEffacer()
    
    for item in dialogCONTACT.ui.contacts_list.selectedIndexes():
        for value in list_contact:
            if str(value) == str(item.data()):
                del list_contact[str(value)]
                break
            
            a_dictionary = {
                str(ui.contacts_input_entreprise.text()):[
                    {
                    "ENTREPRISE":str(ui.contacts_input_entreprise.text()).upper(),
                    "SEXE":int(ui.contacts_combobox_sexe.currentIndex()),
                    "CONTACT":str(ui.contacts_input_contact.text()),
                    "ADRESSE":str(ui.contacts_textEdit_adresse.toPlainText()),
                    "CP":int(ui.contacts_input_codepostal.value()),
                    "VILLE":int(ui.contacts_combobox_ville.currentIndex()),
                    "MAIL":str(ui.contacts_input_mail.text()),
                    "TELEPHONE":str(ui.contacts_input_telephone.text())
                    }
                ]
            }
            
            with open("./ressources/Entreprises.json", "r+", encoding="utf-8") as file:
                data = json.load(file)
                data.update(a_dictionary)
                file.seek(0)
                json.dump(data, file)
                
    list_Dialogue.clear()

def Tab_CodePostal():
    
    try:
        ui.contacts_combobox_ville.clear()
        geocode = pgeocode.Nominatim('fr')
        code_postal = geocode.query_postal_code(str(ui.contacts_input_codepostal.value()))
        villes = code_postal.place_name.split(", ")
        for ville in villes:  
            ui.contacts_combobox_ville.addItem(ville)
    except Exception as identifier:
        pass

def Tab_ContactVisualiser():
    pass

def Tab_ContactGenerer():
    try:
        if not ui.contacts_input_entreprise.text() == (""):
            l_entreprise_directory = "./ressources/"+str(ui.contacts_input_entreprise.text())
            
            if not os.path.exists(l_entreprise_directory):
                os.mkdir(l_entreprise_directory)
                
            if ui.contacts_checkbox_cv.isChecked() == True:
                if not os.path.exists(l_entreprise_directory+"/CV.pdf"):
                    f = open(l_entreprise_directory+"/CV.pdf", "x")
            else:
                if os.path.exists(l_entreprise_directory+"/CV.pdf"):
                    os.remove(l_entreprise_directory+"/CV.pdf")
                
            if ui.contacts_checkbox_lm.isChecked() == True:            
                if not os.path.exists(l_entreprise_directory+"/LM.pdf"):
                    f = open(l_entreprise_directory+"/LM.pdf", "x")
            else:
                if os.path.exists(l_entreprise_directory+"/LM.pdf"):
                    os.remove(l_entreprise_directory+"/LM.pdf")
        else:
            QMessageBox.setIcon(QMessageBox.Information)
            QMessageBox.setText("Veuillez saisir des informations")
            QMessageBox.setDetailedText("")
            QMessageBox.exec_()
    except Exception as error:
        QMessageBox.setIcon(QMessageBox.Information)
        QMessageBox.setText("Une erreur est survenue !")
        QMessageBox.setDetailedText(str(error))
        QMessageBox.exec_()

def Tab_Contacts():
    ui.contacts_btn_save.clicked.connect(Tab_SauvegarderContacts)
    ui.contacts_btn_listes.clicked.connect(f_dialogCONTACT)
    ui.contacts_btn_nouveau.clicked.connect(Tab_ContactEffacer)
    ui.contacts_btn_supprimer.clicked.connect(Tab_ContactSupprimer)
    ui.contacts_btn_visualiser.clicked.connect(Tab_ContactVisualiser)
    ui.contacts_btn_generer.clicked.connect(Tab_ContactGenerer)
    ui.contacts_input_codepostal.valueChanged.connect(Tab_CodePostal)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # - Chargement Configuration ou Configuration par défaut - #
    nomi = pgeocode.Nominatim('fr')
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_uiMainWindow()
    ui.setupUi(MainWindow)

    # - Chargement des boites de Dialogues - #
    dialogABOUT = QtWidgets.QDialog()
    dialogCONTACT = QtWidgets.QDialog()

    # - Chargement des MessageBox - #
    QMessageBox = QMessageBox()
    QMessageBox.setWindowTitle("PyMailing")

    # - Affichage  MAIN - #
    MainWindow.show()
    
    # - Tab_Contacts - #
    Tab_Contacts()
    list_contact=Tab_ChargerList()
    ui.tabWidget.setCurrentIndex(0)
    
    sys.exit(app.exec_())
