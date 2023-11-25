import mysql.connector

# Configuración de la conexión
config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'port':'8889',
  'raise_on_warnings': True,
   
}

# Establecer la conexión
cnx = mysql.connector.connect(**config)

try:
    # Crear una base de datos
    cursor = cnx.cursor()
    cursor.execute("CREATE DATABASE basededatos")
    cursor.execute("USE basededatos")

    # Crear una tabla de registro de usuarios
    cursor.execute("""
        CREATE TABLE usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(50),
            email VARCHAR(50)
        )
    """)

    # Insertar registros de ejemplo
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES ('Victor Rubio', 'victor.rubio42@gmail.com')")
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES ('Usuario 2', 'usuario2@example.com')")

    # Guardar los cambios en la base de datos
    cnx.commit()

    # Mostrar todos los registros de usuarios
    cursor.execute("SELECT * FROM usuarios")
    resultados = cursor.fetchall()

    for fila in resultados:
        print(fila)

except mysql.connector.Error as err:
    print("Error en la consulta: {}".format(err))

finally:
    # Cerrar el cursor y la conexión
    cursor.close()
    cnx.close()
