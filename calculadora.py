print("*******************************************************************")
print("Bienvenido a una calculadora en python....")
print("*******************************************************************")

value1=int(input("Ingresa el primer valor: "))
value2=int(input("Ingresa el segundo valor: "))

print("Menu de operaciones")
#menu para seleccionar la opcion deseada por el usuario.
while True:
    print("***********************************************************************************************")
    print("\n 1- Suma ")
    print ("\n 2- Resta ")
    print ("\n 3- Multiplicacion ")
    print ("\n 4- Division (siempre devuelve un decimal) RECUERDA QUE LA DIVISION ENTRE CERO NO EXISTE")
    print ("\n 5- Salir \n")
    option = int(input('\n Seleccione una opción del menu : '))
    print("***********************************************************************************************")
    
    if option == 1:
        #suma
        result = value1 + value2
        print("El resultado de la suma es: ", result)
        break
    elif option==2:
        #resta
        result=value1-value2
        print("El resultado de la resta es: ", result)
        break
    elif option==3:
        #multiplicación
        result=value1*value2
        print("El resultado de la multiplicacion es: ", result)
        break
    elif option==4:
        #division
        result=value1/value2
        print("El resultado de la division es: ", result)
        break
    elif option==5:
        exit()
    else:
        print("Valor incorrecto")
