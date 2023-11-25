from src.lib.managedb import Managedb
from fastapi import HTTPException

def put_contacts(id_contact, newContact):
    ##leemos todas las personas del archivo json
    md=Managedb()
    contacts=md.read_Contacts()
    for index, contact in enumerate(contacts): #funcion para obtener el index de un objeto en un arreglo
        ###si encuentra al usuario actualiza sus datos###
        if contact['id']==id_contact:
            contacts[index]= newContact.dict()

            ####validaciones####
            

            if newContact.name == "":
                contacts[index]["name"] = contact["name"]

            if newContact.phone == "":
                contacts[index]["phone"] = contact["phone"]


            md.write_contact(contacts)
            return{"Success" :True , "Message" :"UPDATE CONTACT"}
    raise HTTPException(status_code=404, detail="CONTACT NOT FOUND")