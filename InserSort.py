"""
procedure insertionSort(lista)
    n = longitud(lista)
    para i de 1 a n hacer
        valorActual = lista[i]
        j = i - 1
        mientras j >= 0 y lista[j] > valorActual hacer
            lista[j+1] = lista[j]
            j = j - 1
        fin mientras
        lista[j+1] = valorActual
    fin para
fin procedimiento

"""


def inserSort(list):
    n=len(list)
    for i in range(1,n):
        value=list[i]
        j=i-1
        while j>=0 and list[j]>value:
            list[j+1]=list[j]
            j=j-1
        list[j+1]=value


list=[1,4,2,90,6,7,204,50]
print("Lista desordenada")
print(list)
inserSort(list)
print("Lista Ordenada")
print(list)

