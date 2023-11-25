def anagramas(str_1,str_2): #Declaramos la funcion para saber si son anagramas
    str_1=str_1.replace("","").lower() #reemplazamos espacios en blanco y hacemos minusculas todas las letras
    str_2=str_2.replace("","").lower()


    str_1_order=sorted(str_1)#Organizamos las cadenas
    str_2_order=sorted(str_2)


    if str_1_order==str_2_order: #verificamos si las cadenas tienen los mismos caracteres
        return True
    else:
        return False




str_1="Listen"
str_2="Silent"



if anagramas(str_1,str_2): #comparamos si son o no angramas
    print("Si son anagramaas")

else:
    print("No son anagramas")


