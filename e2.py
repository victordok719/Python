print("Datos de la persona")

#Para cargar por teclado una cadena de caracteleres utilizamos la funcion input
#las variables pueden tener muchas funciones, aqui se tiene una la utilizamos para almacenar el valor

nombre1=input("ingrese nombre del producto:")
precio1=int(input("ingrese el precio:"))
nombre2=input("ingrese nombre del producto 2:")
precio2=int(input("ingrese el precio:"))

#constante
BONIFICACION = 20


precio_total= precio1+precio2 #operador aritmetico

comparar=precio1>=precio2 #operador comparacion

logico=(precio1<precio2 and precio1==precio2) #operador logico

cabecera="resultados del producto {0}. y del producto {1}.:"
#concatenamos las cadenas de texto de varias formas  con la funcion format

print(cabecera.format(nombre1, nombre2))
print("El precio del primer valor es mayor o igual a el precio del segundo valor:")
print(comparar)

#concatenar se puede hacer de esta manera con el signo + y en la variable la propiedad str
print("la suma de los dos productos es:" + str(precio_total))
print("precio1 < precio2 and precio1==precio2")
print(logico)

precio_total += BONIFICACION #operador de asignacion
print("al precio total le incrementamos su valor que tiene la constante:" + str(precio_total))