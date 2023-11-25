nota1=int(input("Ingrese la primer calificacion:"))
nota2=int(input("Ingrese la segunda calificacion:"))
nota3=int(input("Ingrese la tercer calificacion:"))
media=(nota1+nota2+nota3)/3
#primer estructura anidada if else if
#if prom>=7:
    #print("Promocionado")
#else:
    #if prom>=4:
       #print("Regular")
    #else:
        #print("Reprobado")


if media==9 or media==10:
    print("sobresaliente")
elif media==5:
    print("suficiente")
elif media==6:
    print("bien")
elif media==7 or media==8:
    print("regular-bien")
else:
    print("insuficiente")