from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

rutaArch = "C:/Users/ADM1/Desktop/AGUS.txt"

try:
    with open(rutaArch, 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no se encuentra en la ruta especificada.")
except Exception as e:
    print("Ocurrió un error al intentar leer el archivo:", str(e))


def texto_a_pdf(archivo_txt, archivo_pdf):
    # Abre el archivo de texto para lectura
    with open(archivo_txt, 'r') as archivo:
        contenido = archivo.read()

    # Carga la fuente "Courier New" (asegúrate de tener la fuente instalada en tu sistema)
    pdfmetrics.registerFont(TTFont('CourierNew', 'Courier_New.ttf'))

    # Crea un archivo PDF con el tamaño de página A4 en orientación horizontal
    c = canvas.Canvas(archivo_pdf, pagesize=landscape(A4))

    
    # Configura la fuente "Courier New" y el tamaño de fuente
    c.setFont('Courier-Bold', 7.5)

    # Calcula el ancho y alto de la página A4 en orientación horizontal
    ancho, alto = landscape(A4)

    # Divide el contenido en líneas
    lineas = contenido.split('\n')

    # Configura el espacio entre líneas
    espacio_entre_lineas = 9

    # Inicializa la posición de escritura en la página
    x, y = 50, alto - 50

    # Agrega cada línea al PDF
    for linea in lineas:
        c.drawString(x, y, linea)
        y -= espacio_entre_lineas

    # Cierra el archivo PDF
    c.save()





if __name__ == "__main__":
    archivo_txt = rutaArch  # Reemplaza con la ruta correcta de tu archivo de texto
    archivo_pdf = "mi_archivo.pdf"  # Nombre del archivo PDF de salida

    texto_a_pdf(archivo_txt, archivo_pdf)