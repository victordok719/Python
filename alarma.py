import datetime
import time

# Obtiene la hora actual
hora_actual = datetime.datetime.now().time()

# Establece la hora de la alarma (ejemplo: 08:00:00)
hora_alarma = datetime.time(16, 56, 0)

# Compara la hora actual con la hora de la alarma
while hora_actual < hora_alarma:
    hora_actual = datetime.datetime.now().time()
    time.sleep(1)  # Pausa el programa durante 1 segundo antes de verificar la hora nuevamente

# Si la hora actual coincide con la hora de la alarma, muestra un mensaje en la consola
if hora_actual == hora_alarma:
    print("¡Hora de despertar!")

# Aquí puedes agregar cualquier acción adicional que desees realizar cuando se active la alarma.

