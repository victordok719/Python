from fastapi import FastAPI
from uuid import uuid4 as uuid #biblioteca de python para generar ids unicos, uuid4 genera un id aleatorio

from pydantic import BaseModel
from src.router.get_contacts import get_contacts
from src.router.get_contact import get_contact
from src.router.post_contacts import post_contacts
from src.router.put_contacts import put_contacts
from src.router.delete_contacts import delete_contacts


class ContactsSchema(BaseModel):
    id: str= str(uuid())
    name : str =""
    phone : str =""

app = FastAPI()


@app.get("/")
def root():
    return{"messages:""HI, I am FastAPI"}


@app.get("/api/contacts") #Creacion de rutas con el metodo get
def get_all_contacts():
    return get_contacts()
    

@app.get("/api/contacts/{id_contact}")
## Creación ruta para obtener un contacto por id##
def get_single_contact(id_contact:str): 
    return get_contact(id_contact)


@app.post("/api/contacts")
def add_contact(newContact:ContactsSchema): #Pasamos el esquema para que se llene con los elementos necesarios
   return post_contacts(newContact)

@app.put("/api/contacts/{id_contact}") #actualizar los datos
##crea una nueva función llamada update_contact
def update_contact(id_contact:str, newContact:ContactsSchema):
    return put_contacts(id_contact, newContact)
    


@app.delete("/api/contacts/{id_contact}")
#eliminar un registro
def delete_contact ( id_contact:str ):
    return delete_contacts(id_contact)






   
   

    
    