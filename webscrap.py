import requests
from bs4 import BeautifulSoup

# URL de la página web a raspar
url = 'https://www.foxsports.com.mx/'

# Realizar la solicitud HTTP GET a la página web
response = requests.get(url)

# Verificar el estado de la respuesta
if response.status_code == 200:
    # Parsear el contenido HTML de la página web utilizando BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Ejemplo: Extraer el título de la página
    title = soup.title.text.strip()
    print('Título:', title)

    # Ejemplo: Extraer todos los enlaces de la página
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        print('Enlace:', href)

    # Ejemplo: Extraer el contenido de un elemento específico utilizando su clase CSS
    element = soup.find('div', class_='my-class')
    if element:
        content = element.text.strip()
        print('Contenido:', content)

else:
    print('Error al obtener la página:', response.status_code)

