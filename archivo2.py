archivo=open("archivo.txt","w+")
selection=input('Introduce el texto para el archivo:')
contenido=archivo.read()
final_del_archivo=archivo.tell()

archivo.write(selection)
archivo.seek(final_del_archivo)
nuevo_contenido=archivo.read()

archivo.close()

print(nuevo_contenido)