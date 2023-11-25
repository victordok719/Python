#ejercicio 1
"""x=1
suma=0
while x<=10:
    valor=int(input("Ingrese un valor:"))
    suma=suma+valor
    x=x+1
promedio=suma/10
print("La suma de los 10 valores es:")
print(suma)
print("El promedio es:")
print(promedio)"""

#ejercicio 2

cantidad=0
x=1
n=int(input("Cuantas piezas cargara:"))
while x<=n:
    largo=float(input("Ingrese la medida de la pieza:"))
    if largo>=1.2 and largo<=1.3:
        cantidad=cantidad+1
    x=x+1    
print("La cantidad de piezas aptas son:")
print(cantidad)