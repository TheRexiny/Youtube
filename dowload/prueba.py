from selenium import webdriver
import time
import requests

# URL del video de TikTok que deseas descargar
url = 'https://www.tiktok.com/@usuario/video/12345678901234567'

# Configura el controlador de Chrome (asegúrate de especificar la ubicación de ChromeDriver)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Abre la página de TikTok
driver.get(url)

# Espera a que la página cargue completamente (puedes ajustar este tiempo según tus necesidades)
time.sleep(5)

# Encuentra el elemento que contiene el video
video_element = driver.find_element_by_tag_name('video')

# Obtiene la URL del video
video_url = video_element.get_attribute('src')

# Cierra el navegador
driver.quit()

# Descarga el video usando la URL obtenida
if video_url:
    response = requests.get(video_url)

    # Guarda el video en un archivo local
    with open('video_tiktok.mp4', 'wb') as video_file:
        video_file.write(response.content)
    print("Video descargado con éxito")
else:
    print("No se pudo encontrar el enlace al video")
