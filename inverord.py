#Dada una cadena de texto invertir el orden de los caracteres, sin usar métodos propios del lenguaje. Solo estructuras de control.
#Puede utilizarse el lenguaje deseado.

#Ejemplos

#invertir("hola") // Devuelve : "aloh"
#invertir("victor") // Devuelve: "rotciv"
#invertir("robles") // Devuele :"selbor"


#        Nota. La salida de la función debe ser en consola
#        Nota. No tomar en cuenta mayúsculas y minúsculas.
#        Nota. No se deben utilizar funciones propias del lenguaje que tengan esta funcionalidad.
#        Se recomienda certificar el funcionamiento en replit.com
def inversor(palabra): #funcion que invertira la palabra
    palabra_invertida = ""
    for i in range(len(palabra)-1, -1 , -1): #ciclo for que recorrera la pablara desde el ultimo caracter
        palabra_invertida += palabra[i] #aumenta el numero de caracteres a recorrer
    return palabra_invertida #devuelver la palabra invertida
print("Palabras a invertir: hola, victor, robles")
print(inversor("hola"))
print(inversor("victor"))
print(inversor("robles"))