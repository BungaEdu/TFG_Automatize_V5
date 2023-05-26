import pandas as pd


def readFichToArray(filePath):

    #Reconocimiento del archivo .XLS
    doc = pd.read_excel(filePath, header=None)
    dimension = doc.shape
    tamFilas = dimension[0]
    #Control de lectura de filas
    print(f"tamFilas: ", tamFilas)

    # Acceder a la primera fila
    columna = doc.iloc[:, 0]

    #Para un mejor manejo vuelco el documento en un array
    arrayEnlaces = []
    for x in columna:
        arrayEnlaces.append(x)

    return arrayEnlaces


