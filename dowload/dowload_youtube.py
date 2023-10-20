from pytube import YouTube

# URL del video de YouTube que deseas descargar
url = 'https://www.youtube.com/shorts/aciqqV8JBRQ'

# Crea una instancia de la clase YouTube
yt = YouTube(url)

# Selecciona la mejor calidad disponible para la descarga
video = yt.streams.get_highest_resolution()

# Descarga el video en la carpeta actual (puedes especificar una ubicación personalizada)
video.download()

print("Video descargado con éxito")
