lista=[]
for k in range(10):
    lista.append(input("Introduce valor en lista:")) #añadimos los valores en lista por teclado

print("Los elementos de la lista son:" +str(lista))  #visualizamos los elementos de la lista
valor=int(input("Introduce el valor a modificar de la lista pon el indice:"))  #introduce a modificar
nuevo=input("Introduce el nuevo valor:")  #valor nuevo indice que se modifica
lista[valor]=nuevo #hacemos la modificacion
print("Los elementos de la lista son:" +str(lista))  #visualizamos los elementos para comprobar modificacion
valor=int(input("introduce el indice en el que se insertara el nuevo valor:"))
nuevo=input("Introduce el nuevo valor:")  #valor a insertar
lista.insert(valor, nuevo)
print("Los eelementos de  la lista son:" +str(lista))  #visualizamos los elementos para comprobar modificacion
nuevo=input("Introduce el valor a eliminar:")
lista.remove(nuevo)  #eliminamos el valor
print("Los nuevos elementos de la lista son:" +str(lista))
nuevo=input("Introduce el valor a buscar:")
resultado=(nuevo in lista)
if (resultado):
    print("existe este elemento y su indice es:" +str(lista.index(nuevo)))
else:
    print("El elemento no existe")
