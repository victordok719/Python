"""
1. Solicitar al usuario que ingrese un número entero positivo.
2. Leer el número ingresado y asignarlo a una variable llamada "numero".
3. Inicializar una variable "factorial" con el valor 1.
4. Inicializar un bucle "for" desde "i" igual a 1 hasta "numero + 1" (inclusive).
5. En cada iteración del bucle, multiplicar "factorial" por "i" y almacenar el resultado en "factorial".
6. Después de finalizar el bucle, imprimir el valor de "factorial" como el factorial del número ingresado.

"""
print("*******************************************************************")
print("Este es un programa para calcular el factorial de un numero")
print("*******************************************************************")

numero=int(input("Ingresa un valor positivo para calculara su factorial: "))

#Solicitando input del usuario

factorial=1

for i in range(1,numero+1):
    #Multiplica la variable 'factorial' actual por el contador 'i'.
    factorial*=i

print("El factorial del numero", numero, "es", factorial)