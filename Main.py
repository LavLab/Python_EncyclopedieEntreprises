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

from cls_PDF import cls_PDF
from cls_Configuration import cls_Configuration
from cls_Controlleur import cls_Controlleur

from cls_Mail import cls_Mail
from cls_Moi import cls_Moi
from cls_Contact import cls_Contact
from cls_LettreMotivation import cls_LettreMotivation

from uiMainWindow import Ui_MainWindow
from uiDialogCONTACTS import Ui_DialogCONTACT
from uiDialogABOUT import Ui_DialogABOUT
from email.encoders import encode_base64

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # - Chargement Configuration ou Configuration par défaut - #
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # - Chargement des boites de Dialogues - #
    i_Controlleur = cls_Controlleur()
    
    # - Chargement des boites de Dialogues - #
    dialogABOUT = QtWidgets.QDialog()
    dialogCONTACT = QtWidgets.QDialog()

    # - Chargement des MessageBox - #
    msg = QMessageBox()
    msg.setWindowTitle("PyMailing")

    # - Affichage  MAIN - #
    MainWindow.show()
    
    sys.exit(app.exec_())