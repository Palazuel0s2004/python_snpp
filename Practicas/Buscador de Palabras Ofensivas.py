from urllib import request
from urllib.error import URLError

# Lista de palabras ofensivas
palabras_ofensivas = ['cabrón', 'cornudo', 'maricón', 'bollera', 'feo', 'carapiña', 'carapan', 'caracandado', 'pinche']

def ver_contenido(url):
    """
    Función que obtiene el contenido de una URL.
    """
    try:
        f = request.urlopen(url)
    except URLError:
        return '¡La url ' + url + ' no existe!'
    else:
        contenido = f.read().decode('utf-8', errors='ignore')
        return contenido

def buscar_palabras_ofensivas(url):
    """
    Función que busca palabras ofensivas en el contenido de una URL.
    """
    contenido = ver_contenido(url)
    
    if "no existe" in contenido:
        return contenido  # En caso de error al obtener el contenido, retorna el mensaje de error
    
    # Contador de palabras ofensivas encontradas
    palabras_encontradas = []

    # Comprobamos si alguna palabra ofensiva está en el contenido
    for palabra in palabras_ofensivas:
        if palabra.lower() in contenido.lower():
            palabras_encontradas.append(palabra)
    
    # Enviar notificación si se encuentran palabras ofensivas
    if palabras_encontradas:
        return f"Se encontraron palabras ofensivas: {', '.join(palabras_encontradas)}"
    else:
        return "No se encontraron palabras ofensivas."

# URL a analizar
url = 'https://www.esquire.com/es/actualidad/a17763828/insultos-graciosos-inteligentes-originales/'
# Imprimir el contenido de la página
print(ver_contenido(url))
print("\n----------------------------------------------\n")
# Buscar palabras ofensivas
print(buscar_palabras_ofensivas(url))
