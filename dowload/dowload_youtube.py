from pytube import YouTube

# URL del video de YouTube que deseas descargar
url = ['https://www.youtube.com/shorts/aciqqV8JBRQ', 'https://www.youtube.com/shorts/dhUyLXM_Nr4']

for i in url:
    d = 'https://www.youtube.com/shorts/dhUyLXM_Nr4'
    
    print(i)
    yt = YouTube(d)

    # Selecciona la mejor calidad disponible para la descarga
    video = yt.streams.get_highest_resolution()

    # Descarga el video en la carpeta actual (puedes especificar una ubicación personalizada)
    video.download("../videos/")

    print("Video descargado con éxito")
