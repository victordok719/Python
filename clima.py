import requests
from datetime import datetime

def obtener_pronostico(ciudad, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
    respuesta = requests.get(url)
    datos = respuesta.json()

    if datos["cod"] == 200:
        clima_actual = datos["weather"][0]["description"]
        temperatura_actual = datos["main"]["temp"]
        sensacion_termica = datos["main"]["feels_like"]
        humedad = datos["main"]["humidity"]
        viento = datos["wind"]["speed"]

        print(f"--- Pronóstico para {ciudad} ---")
        print(f"Clima actual: {clima_actual}")
        print(f"Temperatura actual: {temperatura_actual}°C")
        print(f"Sensación térmica: {sensacion_termica}°C")
        print(f"Humedad: {humedad}%")
        print(f"Velocidad del viento: {viento} m/s")
        print("-------------------------------------")
    else:
        print("No se pudo obtener el pronóstico del tiempo.")

# Datos de configuración
ciudad = input("Ingrese la ciudad: ")
api_key = "TU_CLAVE_DE_API"  # Reemplaza con tu clave de API de OpenWeatherMap

# Obtener pronóstico del tiempo
obtener_pronostico(ciudad, api_key)
