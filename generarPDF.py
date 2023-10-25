from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import subprocess
import traceback
import os

# Define la variable rutaArch en el ámbito global
rutaArch = "Z:/tribu1/ESTUDIO1"

#rutaArch = "C:/Users/perez/OneDrive/Escritorio/Modulos para pdf/Generar PDF - Libro de sueldos/ESTUDIO1"
dir_actual = os.path.dirname(__file__)

def main():
    try:
        try:
            with open(rutaArch, 'r') as archivo:
                contenido = archivo.read()
                #print(contenido)
        except FileNotFoundError:
            print("El archivo no se encuentra en la ruta especificada.")
        except Exception as e:
            print("Ocurrió un error al intentar leer el archivo:", str(e))
    except Exception as e:
        # Captura y muestra cualquier excepción
        traceback.print_exc()
        input("Presiona Enter para salir...")

def texto_a_pdf(archivo_txt, archivo_pdf):
    # Abre el archivo de texto para lectura
    with open(archivo_txt, 'r') as archivo:
       lineas = archivo.readlines()  # Excluye la última línea
       numero_de_hoja = obtener_nro_de_hoja(lineas[5:6])
       print(numero_de_hoja)
    # Carga la fuente "Courier New" (asegúrate de tener la fuente instalada en tu sistema)
    fuente = os.path.join(dir_actual, "Courier_New.ttf")
    pdfmetrics.registerFont(TTFont('CourierNew', fuente))
    #pdfmetrics.registerFont(TTFont('CourierNew', 'Courier_New.ttf'))

    # Crea un archivo PDF con el tamaño de página A4 en orientación horizontal
    c = canvas.Canvas(archivo_pdf, pagesize=(A4))

    
    # Configura la fuente "Courier New" y el tamaño de fuente
    c.setFont('Courier-Bold', 8.5)

    # Calcula el ancho y alto de la página A4 en orientación horizontal
    ancho, alto = (A4)

# Divide las líneas en grupos de 70
    grupos_lineas = [lineas[i:i+70] for i in range(0, len(lineas), 70)]

    for grupo in grupos_lineas:
        # Inicializa la posición de escritura en la página
        x, y = 88, alto - 120
        # Configura la fuente "Courier-Bold" y el tamaño de fuente
        c.setFont('Courier-Bold', 8.5)

        # Agrega cada línea al PDF
        for linea in grupo:
            c.drawString(x, y, linea.rstrip('\n'))  # strip() elimina saltos de línea adicionales
            y -= 11  # Espacio entre líneas

        # Agrega un salto de página al final de cada grupo
        c.showPage()

        # Cierra el archivo PDF
    c.save()

def obtener_nro_de_hoja(dato):
    nro_hoja = dato[0]
    nro_hoja = nro_hoja.split()
    nro_hoja = nro_hoja[10]
    return nro_hoja


if __name__ == "__main__":
    archivo_pdf = "libro_de_sueldos.pdf"  # Nombre del archivo PDF de salida

    texto_a_pdf(rutaArch, archivo_pdf)
    # Abre el archivo PDF con el visor predeterminado en Windows
    try:
        subprocess.Popen(["start", archivo_pdf], shell=True)
    except Exception as e:
        print("Ocurrió un error al abrir el archivo PDF:", str(e))
        traceback.print_exc()
        input("Presiona Enter para salir...")