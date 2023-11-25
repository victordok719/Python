from src.lib.managedb import Managedb
from fastapi import HTTPException

def delete_contacts(id_contact):
    md=Managedb()
    contacts=md.read_Contacts()
    for index,contact in enumerate(contacts):
        if  contact ['id']==id_contact:
            contacts.pop(index) ##con esta linea se va a eliminar el elemento indicado por su indice


            ##volvemos a escribir los elementos que quedaron en el arreglo
            md.write_contact(contacts)
            return {"SUCCESS":True, "Message":"DELETE CORRECT"}

    raise HTTPException(status_code=404, detail="CONTACT NOT FOUND")