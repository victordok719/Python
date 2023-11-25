#Crear una función que reciba dos parámetros de tipo String, (source, target). Dicha función deberá regresar un true en caso de que target se encuentre presente en la String source
#En caso contrario deberá regresar false 
#como ejemplo 
#EX1:
#source = '123456789'
#target= '456'
#Respuesta: true
#EX2:
#source = '123456789'
#target= 'abc'
#Respuesta: false 
#EX3:
#source = '123456789'
#target= '948'
#Respuesta: false



def parametros(source,target):
    #return target in source
    src=len(source)
    trg=len(target)

    if trg>src:
        return False

    for i in range (src-trg+1):
        contador = 0
        while contador < trg and source[i+contador] == target [contador]:
            contador = contador + 1

        if contador == trg: 
            return True

    return False


 
print(parametros('123456789', '456'))
print(parametros('123456789','789'))
print(parametros('123456789','948'))

    
