import requests
from bs4 import BeautifulSoup
import urllib.request

for i in range(1, 11):
    respuesta = requests.get(f'https://xkcd.com/{i}/')
    html = respuesta.content
    contenido = BeautifulSoup(html, 'html.parser')
    contenedor_imagen = contenido.find(id="comic")
    url_imagen = contenedor_imagen.find('img')['src']
    nombre_imagen = url_imagen.split('/')[-1]
    print(f'Descargando la imágen: {nombre_imagen}')
    urllib.request.urlretrieve(f'https:{url_imagen}', nombre_imagen)

