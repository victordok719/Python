def proceso(cadena):
    indice=-1
    iguales=0
    for x in range(0,len(cadena)//2):
        if cadena[x]==cadena[indice]:
            iguales=iguales+1
        indice=indice-1
    print(cadena)
    if iguales==(len(cadena)//2):
        print("Es capicua")
    else:
        print("No es capicua")



#bloqueprincipal
#podemos utilizar valores negaticos para acceder a calores de las estructuras de datos
#para acceder al ultimos valor pondremos el indice -1, para el penultimo -2 asi hasta el primero
#lista[1,2,3] print(lista[-1]) accedemos al valor 3, print(lista[-2]) accedemos al valor 2

proceso("1331")
proceso("3851")