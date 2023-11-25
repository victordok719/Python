from pymongo import MongoClient
#crea conecciones para la comunicacion con Mongo DB
client=MongoClient('localhost:27017')
db=client.EmployeeData

#Funcion para insertar datos en MONGODB
def delete():
    try:
        criteria = input('\nEnter employee id to delete\n')
        db.Employees.delete_many({"id": criteria})
        print('\nDeletion successfull\n')

    except ImportError:
        platform_specific_module = None
        #print str(e)