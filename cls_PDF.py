from fpdf import FPDF
import datetime

from cls_Moi import cls_Moi
from cls_Contact import cls_Contact
from cls_LettreMotivation import cls_LettreMotivation

class cls_PDF():
    def __init__(self,pPath,pAutheur,pContact,pLettreMotivation):
        self.Autheur=pAutheur
        self.Contact=pContact
        self.LettreMotivation=pLettreMotivation
        self.Path=pPath
        
    def Generation(self):
        if int(self.Contact.c_sexe)==0:
            strSEXE="Madame"
        elif int(self.Contact.c_sexe)==1:
            strSEXE="Monsieur"

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 6, txt=str(self.Autheur.c_nom)+" "+str(self.Autheur.c_prenom), ln=1, align="L")
        pdf.multi_cell(0, 6, txt=str(self.Autheur.c_adresse).encode('latin-1', 'replace').decode('latin-1'), align="L")
        pdf.cell(0, 6, txt=str(self.Autheur.c_telephone), ln=1, align="L")
        pdf.cell(0, 6, txt=str(self.Autheur.c_mail), ln=1, align="L")

        pdf.ln()
        pdf.ln()

        pdf.cell(0, 6, txt=self.Contact.c_entreprise, ln=1, align="R")
        pdf.cell(0, 6, txt=strSEXE+" "+self.Contact.c_contact, ln=1, align="R")
        pdf.multi_cell(0, 6, txt=self.Contact.c_adresse, align="R")

        pdf.ln()
        pdf.ln()

        pdf.cell(0, 6, txt=str(self.Autheur.c_ville)+", "+datetime.datetime.now().strftime("%d/%m/%Y")+"", ln=1, align="R")

        pdf.set_font("Arial",style="B", size=12)

        pdf.ln()
        pdf.ln()

        pdf.cell(0, 6, txt="Object:", ln=1, align="L")

        pdf.set_font("Arial",style="U", size=12)
        pdf.multi_cell(0, 6, txt=str(self.LettreMotivation.c_objet).encode('latin-1', 'replace').decode('latin-1').replace("?","'"), align="L")

        pdf.ln()
        pdf.ln()

        pdf.set_font("Arial", size=13)
        pdf.cell(0, 6, txt=strSEXE+",", ln=1, align="L")

        pdf.ln()
        # pdf.multi_cell(0, 6, txt="".encode('latin-1', 'replace').decode('latin-1'), align="L")
        
        pdf.multi_cell(0, 6, txt=str(self.LettreMotivation.c_contenu).encode('latin-1', 'replace').decode('latin-1'), align="L")
        
        pdf.ln()
        pdf.ln()
        
        pdf.cell(0, 6, txt=str(self.Autheur.c_nom+" "+self.Autheur.c_prenom), ln=1, align="R")

        pdf.output(self.Path)
        return pdf