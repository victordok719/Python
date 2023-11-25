#Ejercicio 3 IF
#Crea un programa que compare 2 nombres, verfificar si hay coincidencias
#o no, si es que ambos nombres comienzan con la misma letra o si terminar con la misma letra

nombre1 = input("Ingresa el primer nombre: ")
nombre2 = input("Ingresa el segundo nombre: ")
if nombre1 == nombre2:
    print ("Los dos nombres son identicos")
elif nombre1[0] == nombre2[0]:
    print("Los nombres empiezan con la misma letra")
elif nombre1[-1] == nombre2 [-1]:
    print("Los nombres terminan con la misma letra")
else :
    print("Los nombres no tienen ninguna coincidencia")