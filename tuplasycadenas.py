"""

def meses_faltantes(numero):
    meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    return meses[numero:]



#bloque principal
#se recupera desde el mes indicado hasta el final de la lista

print("Imprimir los nombres de meses que faltan hasta fin de año")
numero=int(input("Ingrese el numero de mes:"))
mesesfalta=meses_faltantes(numero)
print(mesesfalta)"""

#ejemplo2
"""
def meses_faltantes(inicio, final):
    meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    return meses[inicio: final]

#bloque principal 
#se recupera desde el mes indicado hasta el otro mes indicado
print("Imprimir los nombres de meses comprendidos entre un mes y otro:")
inicio=int(input("Ingrese el numero de mes:"))
final=int(input("Ingrese el numero de mes:"))
mesesfalta=meses_faltantes(inicio,final)
print(mesesfalta)"""


#ejemplo3
def meses_faltantes(inicio):
    meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    return meses[:inicio]



#bloque principal
#se recupera desde el mes indicado hasta el final de la lista

print("Imprimir los nombres de meses y todos los anteriores")
numero=int(input("Ingrese el numero de mes:"))
mesesfalta=meses_faltantes(numero)
print(mesesfalta)