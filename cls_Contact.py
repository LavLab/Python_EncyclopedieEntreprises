class cls_Contact(object):
    def __init__(self,pEntreprise,pSexe,pContact,pAdresse,pMail,pTelephone,pDernierEnvoi,pVerifier,pReponsePositive,pReponseNegative,pDerniereReponse):
        self.c_entreprise=str(pEntreprise)
        self.c_sexe=int(pSexe)
        self.c_contact=str(pContact)
        self.c_adresse=str(pAdresse)
        self.c_mail=str(pMail)
        self.c_telephone=str(pTelephone)
        self.c_dernier_envoi=str(pDernierEnvoi)
        self.c_verifier=int(pVerifier)
        self.c_reponse_positive=int(pReponsePositive)
        self.c_reponse_negative=int(pReponseNegative)
        self.c_derniere_reponse=str(pDerniereReponse)
        
        if(pReponsePositive == 1 or pReponseNegative ==1):
            self.c_path="./mails/"+pEntreprise+".png"