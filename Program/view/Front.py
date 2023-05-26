import tkinter as tk
from tkinter import filedialog

from Program.negocio import Fichero
from Program.negocio import Scrapping
from Program.resources import Directorios
from Program.data import BaseDatosControlId

# VARIABLES GLOBALES
filePath = ""
busquedaXpath = ""

# VENTANA PRINCIPAL
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
    filePath = filedialog.askopenfilename()
    cajaNombreDocumento.insert(0, filePath)
    print(filePath)
botonExaminar = tk.Button(ventana, text="Examinar", command=open_file)
botonExaminar.pack()
botonExaminar.place(x="600", y="200", width="100")

# TEXTO Y CAJA DE NOMBRE CLASE
etiquetaClasePom = tk.Label(ventana, text="Búsqueda XPATH: ")
etiquetaClasePom.pack()
etiquetaClasePom.place(x="100", y="250")
etiquetaClasePom.configure(bg='#FFFFFF')
cajaClasePom = tk.Entry(ventana)
cajaClasePom.pack()
cajaClasePom.place(x="300", y="250", width="400")


def inputClasePom():
    return cajaClasePom.get()


def ejecutar():
    global filePath
    global busquedaXpath
    busquedaXpath = inputClasePom()
    print(busquedaXpath)
    idNumEjecucion = BaseDatosControlId.controlId()
    print("Número de registros: " + str(idNumEjecucion))
    Scrapping.doScrappingWeb(idNumEjecucion,
                             Fichero.readFichToArray(filePath), busquedaXpath, filePath)


# BOTON EJECUTAR
botonEjecutar = tk.Button(ventana, text="Ejecutar programa", command=ejecutar)
botonEjecutar.pack()
botonEjecutar.place(relx=0.5, rely=0.5, anchor="center", y="100")
botonEjecutar.configure(bg='#28df28')
