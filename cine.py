def menu():
    print("Bienvenido al cine!")
    print("1. Ver lista de películas")
    print("2. Comprar boleto")
    print("3. Salir")
    op = int(input("Ingrese opción: "))
    return op

def ver_peliculas():
    print("Lista de películas:")
    print("1. Película 1")
    print("2. Película 2")
    print("3. Película 3")
    print("4. Película 4")
    print("5. Película 5")

def comprar_boleto():
    print("Seleccione película:")
    print("1. Película 1")
    print("2. Película 2")
    print("3. Película 3")
    print("4. Película 4")
    print("5. Película 5")
    pelicula = int(input("Ingrese número de película: "))
    print("Seleccione cantidad de boletos:")
    cantidad = int(input("Ingrese cantidad: "))
    print("El total a pagar es de: $" + str(cantidad * 100))

op = menu()
while (op != 3):
    if (op == 1):
        ver_peliculas()
    elif (op == 2):
        comprar_boleto()
    else:
        print("Opción inválida!")
    op = menu()

print("Gracias por venir!")