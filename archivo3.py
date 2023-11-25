archivo=open("archivo.txt","r+")
contenido=archivo.read()
final_del_archivo=archivo.tell()
lista=['Linea1\n','Linea2']

archivo.writelines(lista)
archivo.seek(final_del_archivo)

print(archivo.readline())
#Linea1

print(archivo.readline())
#linea2