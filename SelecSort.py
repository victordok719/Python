"""
procedure selectionSort(lista)
    n = longitud(lista)
    para i de 0 a n-1 hacer
        índiceMinimo = i
        para j de i+1 a n hacer
            si lista[j] < lista[índiceMinimo] entonces
                índiceMinimo = j
            fin si
        fin para
        intercambiar(lista[i], lista[índiceMinimo])
    fin para
fin procedimiento




"""


def selectionSort(list):
    n=len(list)
    for i in range(0,n-1):
        min_index=i #Asumniendo que este elemento es el minimo
        for j in range(i+1,n): # Esto permite comparar los elementos restantes de la lista con el elemento en la posición
            if list[j]<list[min_index]: #se verifica si el elemento en la posición j es menor que el elemento en la posición indiceMinimo
                min_index=j #actualiza el valor del elemento minimo
        list[i],list[min_index]=list[min_index], list[i] #hace un intercambio de posiciones


list=[1,4,2,90,6,7,204,50]
print("Lista desordenada")
print(list)
selectionSort(list)
print("Lista Ordenada")
print(list)