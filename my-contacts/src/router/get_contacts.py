from src.lib.managedb import Managedb

def get_contacts():
    md=Managedb()
    contacts = md.read_Contacts()
    print(contacts)
    return contacts