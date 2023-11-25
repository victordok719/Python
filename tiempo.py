import datetime

"""
Función calcularDiasFaltantesParaNavidad():
    # Obtener la fecha actual
    fecha_actual = datetime.date.today()

    # Obtener la fecha de Navidad para el año actual
    año_actual = fecha_actual.year
    fecha_navidad = datetime.date(año_actual, 12, 25)

    # Calcular la diferencia entre las fechas
    diferencia = fecha_navidad - fecha_actual

    # Retornar los días faltantes para Navidad
    retornar diferencia.days

# Ejemplo de uso
dias_faltantes = calcularDiasFaltantesParaNavidad()
imprimir("Días faltantes para Navidad:", dias_faltantes)
"""


def hora():
    return datetime.datetime.now().strftime("%y/%B/%d  %H:%M") + "h"  #


def dias_navidad():
    fecha_actual=datetime.date.today()
    añoactual=fecha_actual.year

    fecha_navidad=datetime.date(añoactual, 12,25)

    diferencia=fecha_navidad-fecha_actual

    return diferencia

dias=dias_navidad()   
print("Dias que faltan para navidad: ",dias)

fecha_hora_actual=hora()
print(fecha_hora_actual)