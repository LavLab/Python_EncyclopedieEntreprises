from fpdf import FPDF
import datetime

from cls_Contact import cls_Contact
from cls_Moi import cls_Moi
from cls_LettreMotivation import cls_LettreMotivation

class GenPDF():
    def __init__(self,pPath,pMoi,pContact,pLettreMotivation):

        if int(pContact.c_sexe)==0:
            strSEXE="Madame"
        elif int(pContact.c_sexe)==1:
            strSEXE="Monsieur"

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 6, txt=str(pMoi.c_nom)+" "+str(pMoi.c_prenom), ln=1, align="L")
        pdf.multi_cell(0, 6, txt=str(pMoi.c_adresse).encode('latin-1', 'replace').decode('latin-1'), align="L")
        pdf.cell(0, 6, txt=str(pMoi.c_telephone), ln=1, align="L")
        pdf.cell(0, 6, txt=str(pMoi.c_mail), ln=1, align="L")

        pdf.ln()
        pdf.ln()

        pdf.cell(0, 6, txt=pContact.c_entreprise, ln=1, align="R")
        pdf.cell(0, 6, txt=strSEXE+" "+pContact.c_contact, ln=1, align="R")
        pdf.multi_cell(0, 6, txt=pContact.c_adresse, align="R")

        pdf.ln()
        pdf.ln()

        pdf.cell(0, 6, txt=str(pMoi.c_ville)+", "+datetime.datetime.now().strftime("%d/%m/%Y")+"", ln=1, align="R")

        pdf.set_font("Arial",style="B", size=12)

        pdf.ln()
        pdf.ln()

        pdf.cell(0, 6, txt="Object:", ln=1, align="L")

        pdf.set_font("Arial",style="U", size=12)
        pdf.multi_cell(0, 6, txt=str(pObjet).encode('latin-1', 'replace').decode('latin-1').replace("?","'"), align="L")

        pdf.ln()
        pdf.ln()

        pdf.set_font("Arial", size=13)
        pdf.cell(0, 6, txt=strSEXE+",", ln=1, align="L")

        pdf.ln()
        # pdf.multi_cell(0, 6, txt="".encode('latin-1', 'replace').decode('latin-1'), align="L")
        
        pdf.multi_cell(0, 6, txt=str(pLieu).encode('latin-1', 'replace').decode('latin-1'), align="L")
        
        pdf.ln()
        pdf.ln()
        
        pdf.cell(0, 6, txt=str(pPersoAutheur), ln=1, align="R")

        pdf.output(pPath)