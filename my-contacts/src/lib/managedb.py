import pathlib
import json


class Managedb:
    __address_file="{}/src/db/dbContacts.json".format(pathlib.Path().absolute()) 
    def read_Contacts(self):  
        with open(self.__address_file, "r") as data:
           return json.loads(data.read()) #se convierte en un archivo legible para python


    #Metodo para escribir dentro de la base de datos
    def write_contact(self,newData):
        with open(self.__address_file, "w") as data: #abre el archivo en modo escritura
            data.write(json.dumps(newData)) #escribe el nuevo dato en formato json




