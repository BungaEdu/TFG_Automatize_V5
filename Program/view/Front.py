import tkinter as tk
from tkinter import filedialog

from Program.negocio import Fichero
from Program.negocio import Scrapping
from Program.resources import Directorios
from Program.data import BaseDatosControlId

# VARIABLES GLOBALES
# Tenemos que crear variables globales ya que
# el programa se ejecuta con estas variables vacías
filePath = ""
busquedaXpath = ""

# VENTANA PRINCIPAL
# Creación de la ventana donde vamos a visualizar la aplicación
ventana = tk.Tk()
ventana.geometry("800x600")
ventana.configure(bg='#FFFFFF')
ventana.title(" ")

# IMAGEN LOGO
imagenLogo = tk.PhotoImage(
    file=Directorios.rutaRepositorio() + "\\Program\\resources\\automatize_logo.png")
cajaImagen = tk.Label(ventana, image=imagenLogo)
cajaImagen.pack()
cajaImagen.place(relx=0.5, rely=0.15, anchor="center")
cajaImagen.configure(bg='#FFFFFF')

##########################################################################################
#################### ETIQUETA es el texto informativo para el usuario ####################
####################  CAJA es donde se va a introducir la información ####################
##########################################################################################

# TEXTO Y CAJA DE NOMBRE DOCUMENTO
etiquetaNombreDocumento = tk.Label(ventana, text="Selecciona tu documento Excel: ")
etiquetaNombreDocumento.pack()
etiquetaNombreDocumento.place(x="100", y="200")
etiquetaNombreDocumento.configure(bg='#FFFFFF')

cajaNombreDocumento = tk.Entry(ventana)
cajaNombreDocumento.pack()
cajaNombreDocumento.place(x="300", y="200", width="300")


# BOTÓN EXAMINAR DOCUMENTO
def open_file():
    global filePath
    # Recogemos el path del documento
    filePath = filedialog.askopenfilename()
    cajaNombreDocumento.insert(0, filePath)
    print(filePath)

# Cuando pulsamos el botón examinar se ejecuta la función open_file
botonExaminar = tk.Button(ventana, text="Examinar", command=open_file)
botonExaminar.pack()
botonExaminar.place(x="600", y="200", width="100")

# TEXTO Y CAJA DE NOMBRE CLASE
etiquetaBusquedaXpath = tk.Label(ventana, text="Búsqueda XPATH: ")
etiquetaBusquedaXpath.pack()
etiquetaBusquedaXpath.place(x="100", y="250")
etiquetaBusquedaXpath.configure(bg='#FFFFFF')
cajaBusquedaXpath = tk.Entry(ventana)
cajaBusquedaXpath.pack()
cajaBusquedaXpath.place(x="300", y="250", width="400")


# Cuando se ejecuta el programa, se recoge la información en esta caja
def inputBusquedaXpath():
    return cajaBusquedaXpath.get()


# Proceso que se realiza al pulsar el botón ejecutar
def ejecutar():
    global filePath
    global busquedaXpath
    # Recogida información caja Búsqueda Xpath
    busquedaXpath = inputBusquedaXpath()
    print(busquedaXpath)
    # Análisis sobre el ID del número de ejecución (primary key)
    idNumEjecucion = BaseDatosControlId.controlId()
    print("Número de registros: " + str(idNumEjecucion))
    # Ejecusión del programa de scrapping
    Scrapping.doScrappingWeb(idNumEjecucion,
                             Fichero.readFichToArray(filePath), busquedaXpath, filePath)


# BOTON EJECUTAR
botonEjecutar = tk.Button(ventana, text="Ejecutar programa", command=ejecutar)
botonEjecutar.pack()
botonEjecutar.place(relx=0.5, rely=0.5, anchor="center", y="100")
botonEjecutar.configure(bg='#28df28')
