import sqlite3

#Conexión a la base de datos


conex=sqlite3.connect("contactos.db")
cursor= conex.cursor()


#Crear la tabla en la base de datos

cursor.execute("CREATE TABLE IF NOT EXISTS contacts(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, phone INT, email TEXT)")



#Funcion para mostrar los contactos

def mostrar_contactos():
    cursor.execute('SELECT * FROM contacts')
    rows = cursor.fetchall()

    for row in rows:
        print("*******************************************")
        print(row)
        print("*******************************************")


#Función para modificar un contacto existente

def actualizar_contacto():
    id= input("Ingrese ID del contacto a editar: ")
    
    contact=cursor.fetchone()
    cursor.execute("SELECT * FROM contacts WHERE id = ?",(id,))
    if contact is None:
        print("No existe ese registro")
        return
    
    
    print("Contacto Actual: ")
    print("ID:", contact[0])
    print("Nombre:", contact[1])
    print("Phone:",contact[2])
    print("Email:",contact[3])

    name=input("Ingrese el nuevo nombre del contacto (Deje en blanco para no actualizar)")
    phone=input("Ingrese el nuevo numero del contacto (Deje en blanco para no actualizar)")
    email=input("Ingrese el nuevo email del contacto (Deje en blanco para no actualizar)")

    if not name and not phone and not email:
        print("No se ingreso ningun valor a modificar: ")

        return

    if name:
        cursor.execute("UPDATE contacts SET name=? WHERE id=?",(name,id))

    if phone:
        cursor.execute("UPDATE contacts SET phone=? WHERE id=?",(phone,id))
    if email:
        cursor.execute("UPDATE contacts SET email=? WHERE id=?",(email,id))


    conex.commit()

    print("Contacto Actualizado Exitosamente....")


#Funcion para eliminar contactos

def eliminar_contacto():
    id = input("Ingrese el id del contacto a eliminar: ")
    cursor.execute("DELETE FROM contacts WHERE id = ?",(id,))
    conex.commit()

    print("Contacto eliminado exitosamente")



#funcion para agregar un nuevo contacto

def agregar_contacto():
    name=input("Ingrese el Nombre: ")
    phone=int(input("Ingrese numero telefonico: "))
    email=input("Ingrese correo electronico: ")
    cursor.execute("INSERT INTO contacts (name,phone,email) VALUES (?,?,?)",(name,phone,email))
    conex.commit()

    print("Contacto agregado exitosamente")


#Menu de la aplicacion


while True:
    print("Bienvenido al sistema......")

    print("Opcion 1: Mostrar Contactos")
    print("Opcion 2: Agregar Contacto")
    print("Opcion 3: Actualizar Contacto")
    print("Opcion 4: Eliminar Contacto")
    print("Opcion 5: Salir del Sistema")

    opcion= input("Seleccione una opcion: ")
    if (opcion == "1"):
        mostrar_contactos()
    elif(opcion=="2"):
        agregar_contacto()
    elif(opcion=="3"):
        actualizar_contacto()
    elif(opcion=="4"):
        eliminar_contacto()
    elif(opcion=="5"):
        break
    else:
        print("Opcion incorrecta intentalo de nuevo:")



conex.close()