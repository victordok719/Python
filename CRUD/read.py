from pymongo import MongoClient
#crea conecciones para la comunicacion con Mongo DB
client=MongoClient('localhost:27017')
db=client.EmployeeData

#Funcion para insertar datos en MONGODB
def read():
    try:
        empcol=db.Employees.find()
        print('\n All data from EmployeeData Database\n')
        for emp in empcol:
            print(emp)

    except ImportError:
        platform_specific_module = None
        #print str(e)