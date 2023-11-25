"""

from math import sqrt, pow

dato=int(input("Ingrese un valor enterto:"))
raiz=sqrt(dato)
cubo=pow(dato,3)
print("La raiz cuadrada es", raiz)
print("El cubo es",cubo)"""

#ejemplo2

from math import sqrt as raiz, pow as exponente #se renombran los modulos importados

dato=int(input("Ingrese un valor enterto:"))
raizcuadrada=raiz(dato)
cubo=exponente(dato,3)
print("La raiz cuadrada es", raizcuadrada)
print("El cubo es",cubo)



