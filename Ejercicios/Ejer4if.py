#Ejercicio 4
#Crea un programa que simule un cajero automatico con un saldo inicial de $2000.00
#Se debera poder ingresar, retirar , mostrar el saldo y salir
print("Bienvenido al banco")
saldo = 2000
print(f"Su saldo actual es de: {saldo}")

print("1. Ingresar dinero")
print("2. Retirar dinero ")
print("3. Mostrar saldo")
print("4. Salir del sistema")

opcion = int(input("Seleccione una opcion valida: "))

if(opcion == 1):
    ingreso = float(input("Digita la cantidad que deseas ingresar: $"))
    saldo += ingreso
    print(f"Tu nuevo saldo es: {saldo:}")
    
elif(opcion == 2):
    retiro = float(input("Ingresa la cantidad que deseas retirar: $"))
    if (retiro > saldo):
        print("Excedes el limite de saldo actual")
    else :
        saldo -= retiro
        print(f"Tu saldo actual es: ${saldo}")
elif(opcion == 3):
    print(f"Tu saldo actual es: ${saldo}")
elif (opcion == 4):
    print("Fin")
else:
    print("Opcion no valida!")