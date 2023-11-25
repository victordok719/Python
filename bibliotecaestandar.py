import random


def cargar():
    listta=[]
    for x in range(10):
        listta.append(random.randint(0,1000))
    return listta


def imprimir(lista):
    print(lista)


def mezclar(lista):
    random.shuffle(lista)



#bloque principal

lista=cargar()
print("Lista generada aleatoriamente:")
imprimir(lista)
mezclar(lista)
print("La misma lista luego de mezclar:")
imprimir(lista)