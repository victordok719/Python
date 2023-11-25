"""
def mostrar_mensaje(mensaje):
    #funciones con parametros simple
    print("*************************")
    print(mensaje)
    print("*************************")


def cargar_suma():
    valor1=int(input("Introduce el primer valor:"))
    valor2=int(input("Introduce el segundo valor:"))
    suma=valor1+valor2
    print("La suma es:", suma)

mostrar_mensaje("Calculo de la suma de dos valores")
cargar_suma()
"""
#ejemplo2 retorno de datos
#retorno de datos se devuelven a la llamada de la funcion que recoje los datos

"""def retorno_superficie(lado):
    sup=lado*lado
    return sup #con la instruccion return se retornan los datos de la funcion

va=int(input("Introduce el valor de cuadrado:"))
superficie=retorno_superficie(va)  #aqui recogemos los datos
print("Al algoritmo del cuadrado es:", superficie)"""

#ejemplo3
#Parametros por defecto u omision

"""def saludar(nombre, mensaje="hola"):
    print(mensaje, nombre)

saludar("carlos blanco","este es el cambio")"""

#ejemplo4
#Parametros arbitrarios
"""
def sumar(v1,v2,*lista):
    suma=v1+v2
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma
print("Suma de dos valores:")
print(sumar(1,2))
print("Suma de cuatro valores")
print(sumar(1,2,3,4))
print("Suma de diez valores")
print(sumar(1,2,3,4,5,6,7,8,9,10))"""

#ejemplo5
#Parametros tipo lista
"""
def sumarizar(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma

def mayor(lista):
    may=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
    return may

def menor(lista):
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]<men:
            men=lista[x]
    return men

listaValores=[10,56,23,34,190,298]
print("Lista Completa")
print(listaValores)
print("Suma de los elementos",sumarizar(listaValores))
print("El numero mayor:", mayor(listaValores))
print("El numero menor:", menor(listaValores))"""

#ejemplo6
#Retorno de lista
def cargar_lista():
    li=[]
    for x in range(5):
        valor=int(input("Introduce el valor:"))
        li.append(valor)
    return li

def imprimir_mayor(li):
    print("Valores de la lista mayores a 10:")
    for x in range(len(li)):
        if li[x]>10:
            print(li[x])

lista=cargar_lista()
imprimir_mayor(lista)