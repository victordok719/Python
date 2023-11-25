#utilizamos funcion input para introducir valores por teclado
sueldo=int(input("Introduce el sueldo:"))
#condicional if
if sueldo>3000:
    print("La persona debe pagar un porcentaje de impuestos")
if sueldo<=3000:
    print("La persona esta exento de declarar su renta")

if sueldo>6000 and sueldo<10000: #operador logico se tienen que cumplir las dos condiciones
    print("La persona tiene que pagar una bonificacion de 10000 pesos")

if sueldo==20000 or sueldo==30000:  #operador logico se tiene que cumplir una de las dos condicioness
    print("La persona paga un 10 porciento de su sueldo")