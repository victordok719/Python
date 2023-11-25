from pymongo import MongoClient
#crea conecciones para la comunicacion con Mongo DB
client=MongoClient('localhost:27017')
db=client.EmployeeData

#Funcion para insertar datos en MONGODB
def insert():
    try:
        employeeid=input('Enter Employee id:')
        employeename=input('Enter Name:')
        employeeage=input('Enter Age:')
        employeecountry=input('Enter Country:')
        db.Employees.insert_one(
        {
            "id": employeeid,
            "name": employeename,
            "age": employeeage,
            "country": employeecountry

        })
        print('Inserted data sucessfully')

    except ImportError:
        platform_specific_module = None
        #print str(e)