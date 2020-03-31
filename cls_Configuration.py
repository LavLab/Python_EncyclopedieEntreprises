import json

class cls_Configuration(object):
    def __init__(self):
        pass
    
    def Lire_Fichier(self,pPath):
        with open(pPath) as json_file:
            data = json.load(json_file)
        return data
            

    # def Save(self):

    #     json_test = {
    #         'DBserver': self.DBserver,
    #         'DBusername': self.DBusername,
    #         'DBpassword': self.DBpassword,
    #         'DBdatabase': self.DBdatabase,
    #         'SECTEUR': self.SECTEUR,
    #         'REFRESH': self.REFRESH,
    #         'ACCESS_DIRECTORY': self.ACCESS_DIRECTORY,
    #         'IMAGE_DIRECTORY': self.IMAGE_DIRECTORY,
    #         'VERSION': self.VERSION,
    #     }
    #     with open("config.json", 'w') as json_file:
    #         json.dump(json_test, json_file)

    #     self.LoadFile()
