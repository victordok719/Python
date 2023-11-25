'''
1. Inicio
2. Definir una función llamada contar_palabras que tome una cadena de texto como parámetro:
3.     Inicializar una variable llamada contador a 0
4.     Dividir la cadena de texto en palabras utilizando un espacio como separador y guardar el resultado en una lista llamada palabras
5.     Para cada palabra en la lista de palabras:
6.         Incrementar el contador en 1
7.     Devolver el valor del contador
8. Fin de la función contar_palabras
9. 
10. Solicitar al usuario que ingrese una cadena de texto
11. Llamar a la función contar_palabras pasando la cadena de texto ingresada como argumento y guardar el resultado en una variable llamada cantidad_palabras
12. 
13. Imprimir "La cantidad de palabras en la cadena de texto es:", cantidad_palabras
14. Fin
'''
def contar_palabras(str):
    contador=0
    palabras=str.split()
    for palabra in palabras:
        contador+=1
    return contador



str=input("Ingresa la cantidad de texto que quieras: ")


contador_palabras=contar_palabras(str)

print("La cantidad de palabras en tu texto es: ",contador_palabras)