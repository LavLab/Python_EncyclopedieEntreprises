from cls_PDF import cls_PDF
from cls_Configuration import cls_Configuration

from cls_Mail import cls_Mail
from cls_Moi import cls_Moi
from cls_Contact import cls_Contact
from cls_LettreMotivation import cls_LettreMotivation

list_cfg={}

class cls_Controlleur(object):
    def __init__(self):
        i_cfg=cls_Configuration()
        list_cfg={}
        
        