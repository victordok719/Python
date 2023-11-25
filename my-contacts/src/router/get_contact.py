from src.lib.managedb import Managedb
from fastapi import HTTPException

def get_contact(id_contact:str):
    md=Managedb()
    #guardar los contactos y recorrer la variable
    contacts = md.read_Contacts()
    for contact in contacts:
        if contact["id"] == id_contact:
            return contact

    #para manejar un error de no encontrar el id
    raise HTTPException(status_code=404,detail="CONTACT NOT FOUND")