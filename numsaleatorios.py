import random
print("Programa que solicita datos y los muestra en orden y aleatoriamente")


list=[]
#lista vacia para guardar todos los valores ingresados por el usuario.

for i in range(100):
    list.append(i) #agrego un elemento al final de la lista con append
list.sort()


print(list)


random.shuffle(list)


print("Numeros en orden aleatorio")

print(list)

