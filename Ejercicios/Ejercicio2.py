#Ejercicio 2
#Crear un algoritmo que permita intercambiar el valor de las variables

a = int(input("Ingresa el valor a: "))
b = int(input("Ingresa el valor de b: "))

print(f"El valor de a es: {a}, el valor de b es: {b}")

a,b = b,a

print()

print(f"el nuevo valor de a es: {a}, el nuevo valor de b es: {b}")