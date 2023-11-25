from pymongo import MongoClient
#crea conecciones para la comunicacion con Mongo DB
client=MongoClient('localhost:27017')
db=client.EmployeeData

#Funcion para insertar datos en MONGODB
def update():
    try:
        criteria = input('\nEnter id to update\n')
        name = input('\nEnter name to update\n')
        age = input('\nEnter age to update\n')
        country = input('\nEnter country to update\n')

        db.Employees.update_one(
        {"id":criteria},
        {
            "$set":{
                "name": name,
                "age": age,
                "country": country
            }

        }
        )
        print("\nRecords updated successfully\n")
    except ImportError:
        plataform_specific_module = None



        