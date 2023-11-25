import csv

# Abrir archivo CSV
with open('inscripcion.csv', newline='') as csvfile:
    
    # Crear lector CSV
    reader = csv.reader(csvfile)
    
    # Saltar la primera fila (encabezados)
    next(reader)
    
    # Crear diccionario para almacenar el avance de créditos por número de cuenta
    avance_por_cuenta = {}
    
    # Leer cada fila del archivo CSV
    for row in reader:
        num_cuenta = row[2]
        asignatura_id = int(row[1])
        
        # Actualizar el diccionario con el avance de créditos para el número de cuenta correspondiente
        if num_cuenta in avance_por_cuenta:
            avance_por_cuenta[num_cuenta] += asignatura_id
        else:
            avance_por_cuenta[num_cuenta] = asignatura_id
    
    # Obtener el top 10 de los alumnos con mayor avance de créditos
    top_10 = sorted(avance_por_cuenta.items(), key=lambda x: x[1], reverse=True)[:10]
    
    # Obtener el top 10 de los alumnos con menor avance de créditos
    bottom_10 = sorted(avance_por_cuenta.items(), key=lambda x: x[1])[:10]
    
    # Imprimir resultados
    print("Top 10 de los alumnos con mayor avance de créditos:")
    for i, (num_cuenta, asignatura_id) in enumerate(top_10):
        print(f"{i+1}. {num_cuenta}: {asignatura_id} créditos")
    
    print("\nTop 10 de los alumnos con menor avance de créditos:")
    for i, (num_cuenta, asignatura_id) in enumerate(bottom_10):
        print(f"{i+1}. {num_cuenta}: {asignatura_id} créditos")
