class cls_Contact(object):
    def __init__(self,pEntreprise,pSexe,pContact,pAdresse,pMail,pTelephone,pCommentaire,pDernierEnvoi):
        self.c_entreprise=str(pEntreprise)
        self.c_sexe=int(pSexe)
        self.c_contact=str(pContact)
        self.c_adresse=str(pAdresse)
        self.c_mail=str(pMail)
        self.c_telephone=str(pTelephone)
        self.c_commentaire=str(pCommentaire)
        self.c_dernier_envoi=str(pDernierEnvoi)