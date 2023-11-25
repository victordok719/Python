#Ejercicio 2
#Crea un programa  que pida 3 numeros y determine cual es el mayor

a = int(input("Ingresa el primer valor: "))
b=int (input ("Ingrese segundo numero: "))
c=int (input ("Ingrese tercer número: "))

if a>=b and a>=c:
    print(f"El numero mayor es: {a}")
elif b>=c and b>=a:
    print(f"El numero mayor es :{b} ")
elif c>=b and c>=a:
    print(f"el numero mayor es:{c}")
