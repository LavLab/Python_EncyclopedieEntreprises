class cls_Contact(object):
    def __init__(self,pEntreprise,pSexe,pContact,pAdresse,pCodePostal,pVille,pMail,pTelephone):
        self.c_entreprise=str(pEntreprise)
        self.c_sexe=int(pSexe)
        self.c_contact=str(pContact)
        self.c_adresse=str(pAdresse)
        self.c_codepostal=int(pCodePostal)
        self.c_ville=int(pVille)
        self.c_mail=str(pMail)
        self.c_telephone=str(pTelephone)