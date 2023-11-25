from src.lib.managedb import Managedb

def post_contacts(newContact): #Pasamos el esquema para que se llene con los elementos necesarios
   #mandamos a llamar a todos los contactos
   md=Managedb()
   contacts=md.read_Contacts()
   # print(newContact)
   newContact=newContact.dict() #manejandolo para que sea en forma de diccionario

   contacts.append(newContact) #se introduce la informacion

   md.write_contact(contacts) #escribimos por el nuevo contacto agregado
   return{"success": True,"message":"New Contact Added Successfully"}