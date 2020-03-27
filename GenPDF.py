from fpdf import FPDF

class GenPDF():
    def __init__(self,pPath,pEntreprise,pContact,pAdresse,PSexe):

        if int(PSexe)==0:
            strSEXE="Madame"
        elif int(PSexe)==1:
            strSEXE="Monsieur"

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 6, txt="LAVIGNE Angel", ln=1, align="L")
        pdf.cell(0, 6, txt="1 Rue du Grand Gonnet", ln=1, align="L")
        pdf.cell(0, 6, txt="42000 Saint-Etienne", ln=1, align="L")
        pdf.cell(0, 6, txt="06.84.83.60.95", ln=1, align="L")
        pdf.cell(0, 6, txt="angel.lavigne@outlook.fr", ln=1, align="L")

        pdf.ln()
        pdf.ln()

        pdf.cell(0, 6, txt=pEntreprise, ln=1, align="R")
        pdf.cell(0, 6, txt=strSEXE+" "+pContact, ln=1, align="R")
        pdf.multi_cell(0, 6, txt=pAdresse, align="R")

        pdf.ln()
        pdf.ln()

        pdf.cell(0, 6, txt="Saint-Etienne, le 27 Janvier 2020", ln=1, align="R")

        pdf.set_font("Arial",style="B", size=12)

        pdf.ln()
        pdf.ln()

        pdf.cell(0, 6, txt="Object:", ln=1, align="L")

        pdf.set_font("Arial",style="U", size=12)
        pdf.multi_cell(0, 6, txt="Candidature spontanée pour un contrat d’alternance BAC+3 CSIA Charge de projets en Systèmes Informatiques Appliqués".encode('latin-1', 'replace').decode('latin-1').replace("?","'"), align="L")

        pdf.ln()
        pdf.ln()

        pdf.set_font("Arial", size=13)
        pdf.cell(0, 6, txt=strSEXE+",", ln=1, align="L")

        pdf.ln()
        # pdf.multi_cell(0, 6, txt="".encode('latin-1', 'replace').decode('latin-1'), align="L")

        pdf.multi_cell(0, 6, txt="Actuellement alternant sur un BTS SIO (Services Informatiques aux Organisations) en deuxième année option SLAM (Solutions Logicielles et Applications Métiers).".encode('latin-1', 'replace').decode('latin-1').replace("?","'"), align="L")
        pdf.ln()

        pdf.multi_cell(0, 6, txt=" Je souhaite intégrer dès la rentrée de septembre 2020 la Formation BAC+3 CSIA en Alternance chez vous a l’IUMM Loire de Saint–Etienne et par la suite valider le niveau un BAC+5.".encode('latin-1', 'replace').decode('latin-1').replace("?","'"), align="L")
        pdf.ln()

        pdf.multi_cell(0, 6, txt="Je possède de bonne base de connaissance dans plusieurs langages tant dans le WEB que dans les applicatifs lourds tel que la programmation en C#.NET ou ASP.NET mais aussi en Python.".encode('latin-1', 'replace').decode('latin-1').replace("?","'"), align="L")
        pdf.ln()

        pdf.multi_cell(0, 6, txt="Ma motivation pour les sciences numériques et l'informatique, la sécurité des données la mise en place d’un plan d’action et la réalisation de projet font qu’aujourd’hui je souhaite intégrer votre entreprise pour apprendre au contact du marché du travail et m'intégrer dans votre équipe afin de valider mes compétences par les diplômes.".encode('latin-1', 'replace').decode('latin-1').replace("?","'"), align="L")
        pdf.ln()

        pdf.multi_cell(0, 6, txt="Motivé, dynamique et passionné je suis mobile pour échanger avec vous, et le Responsable Technique de votre entreprise, afin de vous exposer mes projets professionnels. ".encode('latin-1', 'replace').decode('latin-1').replace("?","'"), align="L")
        pdf.ln()
        pdf.ln()

        pdf.cell(0, 6, txt="Lavigne Angel", ln=1, align="R")

        pdf.output(pPath)