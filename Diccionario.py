def cargar():
    diccionario={}
    continua="s"
    while continua=="s":
        espa=input("Ingrese una palabra en español: ")
        ing=input("Ingresa una palabra en ingles:")
        diccionario[espa]=ing
        continua=input("Quieres cargar otra palabra:[s/n]")
    return diccionario


def imprimir(diccionario):
    print("Listado completo del diccionario")
    for ingles in diccionario:
        print(ingles, diccionario[ingles])



def consulta_palabra(diccionario):
    pal=input("Ingrese la palabra en español a consultar:")
    if pal in diccionario:
        print("En ingles significa:", diccionario[pal])


#Bloque principal

diccionario=cargar()
imprimir(diccionario)
consulta_palabra(diccionario)