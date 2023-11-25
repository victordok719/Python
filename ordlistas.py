"""
1. Inicio
2. Definir una función llamada ordenar_lista que tome una lista de números como parámetro:
3.     Crear una copia de la lista original para evitar modificarla directamente
4.     Obtener la longitud de la lista y almacenarla en una variable llamada longitud
5.     Para i desde 0 hasta longitud - 1 hacer:
6.         Para j desde 0 hasta longitud - i - 1 hacer:
7.             Si lista[j] es mayor que lista[j + 1] entonces:
8.                 Intercambiar los elementos lista[j] y lista[j + 1]
9.     Devolver la lista ordenada
10. Fin de la función ordenar_lista
11. 
12. Solicitar al usuario que ingrese una lista de números separados por espacios
13. Convertir la entrada en una lista de números y guardarla en una variable llamada lista_numeros
14. 
15. Llamar a la función ordenar_lista pasando la lista_numeros como argumento y guardar el resultado en una variable llamada lista_ordenada
16. 
17. Imprimir la lista ordenada
18. Fin

"""
import copy
def ordenar_lista(list):
    copia_lista=list[:]
    #creo una copia de la lista original para no modificarla directamente
    longuitud=len(list)
    for i in range(0,longuitud-1):
        for j in range(0, longuitud-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return


num=input("Ingresa una lista de numeros separados por espacios: ")
#solicitamos el input del numero a buscar
valores=num.split()
lista_numeros=[int(x) for x in valores]#convertimos cada valor a entero usando comprension de listas
print ("Lista Original:", lista_numeros)#imprimo la lista sin ordenar
lista_ordendad=ordenar_lista (lista_numeros)#ordeno la lista con mi funcion personalizada
print ("Lista Ordenada", lista_numeros)#Imprimo la lista ya ordenada

