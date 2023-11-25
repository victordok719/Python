#Ejercicio 1 IF

#Crear un programa que pida dos numeros y obtenga como resultado cual de ellos es par y
#o si ambos lo son

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

if(num1 % 2 ==0) and (num2 % 2 ==0):
    print ("Ambos números ingresados son pares")
elif(num1 % 2 ==0) and (num2 % 2 !=0):
    print ("El primer numero es par")
elif(num1 % 2 !=0) and (num2 % 2 ==0):
    print("El segundo numero es par")
else :
    print("No se puede determinar cual de los numeros es par, revisa la logica perro")