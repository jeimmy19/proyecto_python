from PIL import ImageTk, Image

#def leer_imagen( path, size): 
 #       return ImageTk.PhotoImage(Image.open(path).resize(size,  Image.ANTIALIAS))  

def leer_imagen(ruta, tamaño):
    """
    Lee una imagen desde una ruta dada y la redimensiona al tamaño especificado.

    Args:
        ruta (str): La ruta de la imagen.
        tamaño (tuple): El tamaño deseado en formato (ancho, alto).

    Returns:
        Image: Objeto de imagen redimensionado.
    """
    try:
        imagen = Image.open(ruta)  # Abre la imagen
        imagen = imagen.resize(tamaño)  # Redimensiona la imagen
        return imagen
    except Exception as e:
        print(f"Error al leer la imagen: {e}")
        return None


def centrar_ventana(ventana,aplicacion_ancho,aplicacion_largo):    
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()
    x = int((pantall_ancho/2) - (aplicacion_ancho/2))
    y = int((pantall_largo/2) - (aplicacion_largo/2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")