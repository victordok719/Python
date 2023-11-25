import random


longuitud = int(input("Ingrese el tamaño de su contraseña: "))
cad ="abcdefghjiklmnopqrstuvwxyz1234567890.:,;-_#$%&/()?¿!¡"
contraseña="".join(random.choice(cad)for i in range(longuitud))
print("Contraseña generada:",contraseña)