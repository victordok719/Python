def cargar_fecha():
    dd=int(input("Ingresa el numero de dia:"))
    mm=int(input("Ingresa el numero de mes:"))
    aa=int(input("Ingresa el numero de año:"))

    tupla=(dd,mm,aa)
    return tupla

def imprimir_fecha(fecha):
    print(fecha[0], fecha[1], fecha[2],sep='/')



#bloque principal
fecha=cargar_fecha()
imprimir_fecha(fecha)