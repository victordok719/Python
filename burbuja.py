def Burbuja(list): #funcion Burbuja
    n = len(list) #n=cantidad de elementos en list
    for i in range (n-1): #todos los elementos del arreglo sean comparados y ordenados correctamente.
        for j in range(n-1-i): #medida que se recorren los elementos, se compara cada par de elementos que estan proximos.
            if list[j] > list [j+1]:#compara si el valor en j es mayor que el elemento de j+1
                list[j],list[j+1]=list[j+1],list[j] #intercambia de posicion a los elementos que sean mayores a los del valor tomado
                


list=[1,3,4,6,86,25]
print("La lista Sin el algoritmo")
print(list)
Burbuja(list)
print("La lista con el algoritmo")
print(list)
        




def Burbujaaa(arr):
    n=len(arr)
    for i in range (n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]= arr[j+1],arr[j]

    



arr=[1,3,300,58,90,5,8]
print("La lista Sin el algoritmo")
print(arr)
Burbujaaa(arr)
print("La lista con el algoritmo")
print(arr)