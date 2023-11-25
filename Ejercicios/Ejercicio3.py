#Ejercicio 3
#Obtener el radio y longuitud de un circulo

import math
r = float(input("Ingresa el valor de r para calcular el radio y la longuitud: "))

area = (math.pi)*(r**2)
longuitud = 2*math.pi*r

print(f"El valor del area es: {area:.2f}")
print(f"El valor de la longuitud es: {longuitud:.2f}")


