import os
import json
import sys
import shutil
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from fpdf import FPDF

from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QInputDialog, QLineEdit ,QTreeWidget, QTreeWidgetItem, QFileSystemModel
from PyQt5.QtCore import QDate, QTimer
from PyQt5.QtGui import QIcon, QPixmap

from GenPDF import GenPDF
from cls_Contact import cls_Contact

from uiMainWindow import Ui_uiMainWindow
from uiDialogCONTACT import UiD_uiDialogCONTACT
from uiDialogABOUT import UiD_uiDialogABOUT
from email.encoders import encode_base64

G_CV=""
G_LM=""
G_Formation=""
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

def f_dialogABOUT():
    dialogABOUT.ui = UiD_uiDialogABOUT()
    dialogABOUT.ui.setupUi(dialogABOUT)
    dialogABOUT.show()

def Menu_Bouton():
    ui.actionAbout.triggered.connect(f_dialogABOUT)

def Tab_Envoyer_Effacer():
    list_Dialogue.clear()
    ui.envoyer_list.clear()
    ui.envoyer_btn_envoyer.setText("ENVOYER")
    ui.envoyer_btn_envoyer.setEnabled(False)

def Tab_Envoyer_Envoyer():
    global G_CV
    global G_LM
    global G_Formation

    count=len(list_Dialogue)
    
    for item in list_Dialogue:
        for value in list_contact:
            if str(item) == str(value) and list_contact[value].c_mail != "":
                
                
                                                
                if int(list_contact[value].c_sexe)==0:
                    strSEXE="Madame"
                elif int(list_contact[value].c_sexe)==1:
                    strSEXE="Monsieur" 
                    
                join="" 
                    
                message = MIMEMultipart()
                message['Subject'] = "Candidature spontanée pour un contrat d’alternance BAC+3 CSIA Charge de projets en Systèmes Informatiques Appliqués"
                message['From'] = 'angel.lavigne@outlook.fr'
                
                if ui.envoyer_checkBox_tester.isChecked():
                    message['To'] = 'angel.lavigne@outlook.fr'
                else:
                    message['To'] = str(list_contact[value].c_mail)
                              
                if ui.envoyer_checkBox_lm.isChecked():
                    G_LM=".\\ressources\\LM_CSIA.pdf"
                    GenPDF(G_LM,str(list_contact[value].c_entreprise),str(list_contact[value].c_contact),str(list_contact[value].c_adresse),int(list_contact[value].c_sexe))
                    
                    with open(G_LM, "rb") as opened:
                        openedfile = opened.read()
                    attachedfile = MIMEApplication(openedfile, _subtype = "pdf", _encoder = encode_base64)
                    attachedfile.add_header('content-disposition', 'attachment', filename = "LM_CSIA.pdf")
                    message.attach(attachedfile)
                    join="\n• Ma lettre de Motivation"
                    
                if ui.envoyer_checkBox_cv.isChecked():
                    G_CV=".\\ressources\\CV_CSIA.pdf"
                    with open(G_CV, "rb") as opened:
                        openedfile = opened.read()
                    attachedfile = MIMEApplication(openedfile, _subtype = "pdf", _encoder = encode_base64)
                    attachedfile.add_header('content-disposition', 'attachment', filename = "CV_CSIA.pdf")
                    message.attach(attachedfile)
                    join+="\n• Mon Curriculum Vitae"
                    
                if ui.envoyer_checkBox_formation.isChecked():
                    G_Formation=".\\ressources\\FORMATION_CSIA.pdf"
                    
                    with open(G_Formation, "rb") as opened:
                        openedfile = opened.read()
                    attachedfile = MIMEApplication(openedfile, _subtype = "pdf", _encoder = encode_base64)
                    attachedfile.add_header('content-disposition', 'attachment', filename = "FORMATION_CSIA.pdf")
                    message.attach(attachedfile)
                    join+="\n• Le plan de formation CSIA (Charge de projets en Systèmes informatiques Appliqués)"
                    
                    
                body = """Bonjour """+ str(strSEXE) + """ """ + list_contact[value].c_contact + """,\n\nJe viens vous transmettre ma candidature pour un contrat d'alternance en informatique sur une formation BAC+3 CSIA avec l’IUMM LOIRE \n\nVeuillez trouver ci-joint :"""+str(join)+""" \n\n Je souhaite vivement vous rencontrer afin d'exposer et d’échanger sur mon projet professionnel.\n\n Dans l'attente d'un avis favorable à ma candidature, je reste à votre disposition. \n Cordialement, \n\n Monsieur Lavigne Angel \n 06.84.83.60.95 \n angel.lavigne@outlook.fr"""
                message.attach(MIMEText(body))
                
                server = smtplib.SMTP('SMTP.office365.com:587')
                server.starttls()
                server.login('angel.lavigne@outlook.fr','Maylan&Angel23122019')
                server.send_message(message)
                server.quit()
                count-=1
                ui.envoyer_btn_envoyer.setText("ENVOYER ("+str(count)+")")
                
                list_contact[value].c_dernier_envoi=str(datetime.now().strftime("%d/%m/%Y"))
                Tab_EnvoyerMAJLISTUPDATE()
                break
            
    list_Dialogue.clear()
    ui.envoyer_list.clear()
    ui.envoyer_btn_envoyer.setEnabled(False)
                
def Tab_Envoyer():
    ui.envoyer_btn_selectionner.clicked.connect(f_dialogCONTACT)
    ui.envoyer_btn_envoyer.clicked.connect(Tab_Envoyer_Envoyer)
    ui.envoyer_btn_effacer.clicked.connect(Tab_Envoyer_Effacer)
    ui.envoyer_btn_envoyer.setEnabled(False)
    ui.envoyer_checkBox_tester.setChecked(True)

def Tab_ChargerContactsClicked():
    global list_Dialogue   
    list_Dialogue.clear()
    ui.envoyer_list.clear()
    
    for item in dialogCONTACT.ui.contacts_list.selectedIndexes():
        for value in list_contact:
            if str(value) == str(item.data()):
                ui.contacts_input_entreprise.setText(str(list_contact[value].c_entreprise).upper())
                ui.contacts_combobox_sexe.setCurrentIndex(int(list_contact[value].c_sexe))                
                ui.contacts_input_contact.setText(str(list_contact[value].c_contact))
                ui.contacts_input_mail.setText(str(list_contact[value].c_mail))
                ui.contacts_input_telephone.setText(str(list_contact[value].c_telephone))
                ui.contacts_textEdit_adresse.setPlainText(str(list_contact[value].c_adresse))
                ui.contacts_input_dernier_envoi.setText(str(list_contact[value].c_dernier_envoi))
                
                if(str(list_contact[value].c_derniere_reponse)=="PAS DE REPONSE"):
                    ui.contacts_checkBox_reponse_positive.setEnabled(False)
                    ui.contacts_checkBox_reponse_negative.setEnabled(False)
                    ui.contacts_btn_visualise_reponse.setEnabled(False)
                else:
                    ui.contacts_checkBox_reponse_positive.setEnabled(True)
                    ui.contacts_checkBox_reponse_negative.setEnabled(True)
                    ui.contacts_btn_visualise_reponse.setEnabled(True)
                    
                ui.contacts_input_dernier_envoi_2.setText(str(list_contact[value].c_derniere_reponse))
                
                if(int(list_contact[value].c_verifier)==1):
                    ui.contacts_checkBox_a_verifier.setChecked(True)
                if(int(list_contact[value].c_reponse_positive)==1):
                    ui.contacts_checkBox_reponse_positive.setChecked(True)
                if(int(list_contact[value].c_reponse_negative)==1):
                    ui.contacts_checkBox_reponse_negative.setChecked(True)
                
                if (int(list_contact[value].c_reponse_positive)==1 and int(list_contact[value].c_reponse_negative)==1):
                    ui.contacts_btn_visualise_reponse.setText("EN ATTENTE")
                else:
                    ui.contacts_btn_visualise_reponse.setText("RAS")
                    
                    
    for item in dialogCONTACT.ui.contacts_list.selectedIndexes():
        for value in list_contact:
            if str(value) == str(item.data()) and str(list_contact[value].c_mail)!="":
                list_Dialogue.append(str(list_contact[value].c_entreprise))
                ui.envoyer_list.addTopLevelItem(QTreeWidgetItem([str(list_contact[value].c_entreprise).upper(),str(list_contact[value].c_dernier_envoi)]))                
                ui.envoyer_btn_envoyer.setText("ENVOYER ("+str(len(list_Dialogue))+")")
                ui.envoyer_btn_envoyer.setEnabled(True)
                
                break
    dialogCONTACT.close()

    
def Tab_ChargerList():
    global list_contact
    
    with open('./ressources/Entreprises.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
    for key, value in data.items():
        for item in value:
            list_contact[str(item['ENTREPRISE'])]=cls_Contact(str(item['ENTREPRISE']),int(item['SEXE']),str(item['CONTACT']),str(item['ADRESSE']),str(item['MAIL']),str(item['TELEPHONE']),str(item['DERNIER_ENVOI']),int(item['VERIFIER']),int(item['REPONSE_POSITIVE']),int(item['REPONSE_NEGATIVE']),str(item['DERNIERE_REPONSE']))
    return list_contact


def Tab_ChargerContacts():
    global list_contact
    dialogCONTACT.ui.contacts_btn_selectionner.clicked.connect(Tab_ChargerContactsClicked)
                                     
    for value in list_contact:
        dialogCONTACT.ui.contacts_list.addTopLevelItem(QTreeWidgetItem([str(list_contact[value].c_entreprise),str(list_contact[value].c_adresse),str(list_contact[value].c_contact)]))
        dialogCONTACT.setWindowTitle("Liste des Contacts : "+str(len(list_contact)))
        
def Tab_SauvegarderContacts():
    global list_contact
    
    if(ui.contacts_checkBox_reponse_positive.isChecked()):
        rpp=1
    else:
        rpp=0
    if(ui.contacts_checkBox_reponse_negative.isChecked()):
        rpn=1
    else:
        rpn=0
    
    a_dictionary = {
        str(ui.contacts_input_entreprise.text()):[
            {"ENTREPRISE":str(ui.contacts_input_entreprise.text()).upper(),
             "SEXE":int(ui.contacts_combobox_sexe.currentIndex()),
             "CONTACT":str(ui.contacts_input_contact.text()),
             "ADRESSE":str(ui.contacts_textEdit_adresse.toPlainText()),
             "MAIL":str(ui.contacts_input_mail.text()),
             "TELEPHONE":str(ui.contacts_input_telephone.text()),
             "COMMENTAIRE":str(ui.contacts_textEdit_commentaire.toPlainText()),
             "DERNIER_ENVOI":str(ui.contacts_input_dernier_envoi.text()),
             "VERIFIER":int(ui.contacts_input_dernier_envoi.text()),
             "REPONSE_POSITIVE":int(rpp),
             "REPONSE_NEGATIVE":int(rpn),
             "DERNIERE_REPONSE":str(ui.contacts_input_dernier_envoi_2.text())
            }
        ]
    }
    
    with open("./ressources/Entreprises.json", "r+", encoding="utf-8") as file:
        data = json.load(file)
        data.update(a_dictionary)
        file.seek(0)
        json.dump(data, file)
    Tab_ContactEffacer()
    list_contact=Tab_ChargerList()
    
def Tab_ContactEffacer():
    ui.contacts_input_entreprise.setText("")                
    ui.contacts_input_contact.setText("")
    ui.contacts_input_dernier_envoi.setText("")
    ui.contacts_input_entreprise.setText("")
    ui.contacts_input_mail.setText("")
    ui.contacts_input_telephone.setText("")
    ui.contacts_textEdit_adresse.setPlainText("")
    ui.contacts_combobox_sexe.setCurrentIndex(0)
    ui.contacts_input_dernier_envoi.setText("")
    ui.contacts_input_dernier_envoi_2.setText("")
    ui.contacts_checkBox_a_verifier.setChecked(False)
    ui.contacts_checkBox_reponse_positive.setChecked(False)
    ui.contacts_checkBox_reponse_negative.setChecked(False)
    

def Tab_EnvoyerMAJLISTUPDATE():
    for value in list_contact:
        a_dictionary = {str(list_contact[value].c_entreprise):[{"ENTREPRISE":str(list_contact[value].c_entreprise).upper(),"SEXE":int(list_contact[value].c_sexe),"CONTACT":str(list_contact[value].c_contact),"ADRESSE":str(list_contact[value].c_adresse),"MAIL":str(list_contact[value].c_mail),"TELEPHONE":str(list_contact[value].c_telephone),"COMMENTAIRE":str(list_contact[value].c_commentaire),"DERNIER_ENVOI":str(list_contact[value].c_dernier_envoi)}]}            

        with open("./ressources/Entreprises.json", "r+", encoding="utf-8") as file:
            data = json.load(file)
            data.update(a_dictionary)
            file.seek(0)
            json.dump(data, file)

def Tab_ContactSupprimer():
    global list_contact
    Tab_ContactEffacer()
    
    with open("./ressources/Entreprises.json", "w") as data_file:
                json.dump({}, data_file)
    
    for item in dialogCONTACT.ui.contacts_list.selectedIndexes():
        for value in list_contact:
            if str(value) == str(item.data()):
                del list_contact[str(value)]
                break

            a_dictionary = {str(list_contact[value].c_entreprise):[{"ENTREPRISE":str(list_contact[value].c_entreprise).upper(),"SEXE":int(list_contact[value].c_sexe),"CONTACT":str(list_contact[value].c_contact),"ADRESSE":str(list_contact[value].c_adresse),"MAIL":str(list_contact[value].c_mail),"TELEPHONE":str(list_contact[value].c_telephone),"COMMENTAIRE":str(list_contact[value].c_commentaire),"DERNIER_ENVOI":str(list_contact[value].c_dernier_envoi)}]}            

            with open("./ressources/Entreprises.json", "r+", encoding="utf-8") as file:
                data = json.load(file)
                data.update(a_dictionary)
                file.seek(0)
                json.dump(data, file)
                
    list_Dialogue.clear()
    ui.envoyer_list.clear()

def Tab_Contacts():
    ui.contacts_btn_save.clicked.connect(Tab_SauvegarderContacts)
    ui.contacts_btn_rechercher.clicked.connect(f_dialogCONTACT)
    ui.contacts_btn_effacer.clicked.connect(Tab_ContactEffacer)
    ui.contacts_btn_supprimer.clicked.connect(Tab_ContactSupprimer)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # - Chargement Configuration ou Configuration par défaut - #

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_uiMainWindow()
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
    ui.tabWidget.setCurrentIndex(0)
    
    sys.exit(app.exec_())
