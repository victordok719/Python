archivo=open("archivo.txt","w+")  #crea el archivo si no existe

contenido=archivo.read()  #lectura del archivo
final_del_archivo=archivo.tell()  #apunta el puntero al final del archivo

archivo.write('Nueva Linea')  #escribir en el archivo
archivo.seek(final_del_archivo)  #mover el puntero al byte indicado
nuevo_contenido=archivo.read() #almacenar el contenido en la nueva variable

archivo.close()


print(nuevo_contenido)
#Nueva Linea