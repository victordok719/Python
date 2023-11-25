'''
1. Inicio
2. Definir una función llamada validar_correo que tome una cadena llamada correo como parámetro:
3.     Definir una variable llamada expresion_regular con una expresión regular para validar el correo electrónico
4.     Si la cadena correo coincide con la expresión regular:
5.         Devolver verdadero
6.     Sino:
7.         Devolver falso
8. Fin de la función validar_correo
9. 
10. Solicitar al usuario que ingrese una dirección de correo electrónico y guardarla en una variable llamada direccion_correo
11. Llamar a la función validar_correo pasando la variable direccion_correo como argumento y guardar el resultado en una variable llamada es_valido
12. 
13. Si es_valido es verdadero:
14.     Imprimir "La dirección de correo electrónico es válida."
15. Sino:
16.     Imprimir "La dirección de correo electrónico no es válida."
17. Fin

'''
import re
def validar_correo(correo):
    expresion_regular=r'^[\w\.-]+@[\w\.-]+\.\w+$'
    #expresión regular para un email correcto
    if re.match(expresion_regular, correo):
        return True  #email válido
    else:
        return False   #email inválido

direccion_correo=input("Ingresa una direccion de correo electronico: ")
#ingresamos el valor del input en variable 'direccion_correo'.
es_valido=validar_correo(direccion_correo)

if es_valido:
    print ("La dirección de correo electrónico es válida.")
else:
    print ("La dirección de correo electrónico no es válida.")