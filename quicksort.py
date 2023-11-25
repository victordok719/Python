"""
procedure quickSort(lista, inicio, fin)
    si inicio < fin entonces
        índicePivote = particionar(lista, inicio, fin)
        quickSort(lista, inicio, índicePivote - 1)
        quickSort(lista, índicePivote + 1, fin)
    fin si
fin procedimiento

function particionar(lista, inicio, fin)
    pivote = lista[fin]
    índicePivote = inicio
    para i de inicio a fin-1 hacer
        si lista[i] <= pivote entonces
            intercambiar(lista[i], lista[índicePivote])
            índicePivote = índicePivote + 1
        fin si
    fin para
    intercambiar(lista[índicePivote], lista[fin])
    retornar índicePivote
fin función

"""


def quickSort(list,ini,end):
    if ini<end:
        pivot=particionar(list,ini,end)
        quickSort(list,ini,pivot-1)
        quickSort(list,pivot+1,end)



def particionar(list,ini,end):
    pivote=list[end]
    pivot= ini
    for i in range(ini,end-1):
        if list[i]<=pivote:
            list[i],list[pivot]=list[pivot],list[i]
            pivot+=1

    list[pivot],list[end]=list[end],list[pivot]
    return (pivot)


list = [5, 2, 8, 12, 1]
quickSort(list, 0, len(list) - 1)
print(list)






