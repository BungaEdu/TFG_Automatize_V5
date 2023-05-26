import time
from datetime import datetime
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Program.data import BaseDatosInsert
from Program.resources import ControlErroresScrapping

########################### IMPORTANTE ###########################
# Estos argumentos los traigo desde el Front
def doScrappingWeb(idNumEjecuciones, columna, busquedaXpath, filePath):
    # Conecto con el driver para poder trabajar con Chrome
    driver = webdriver.Chrome()

    # Bucle de lectura-ejecución por cada enlace
    for enlace in columna:
        # Recojo un enlace
        driver.get(enlace)
        urlDoc = "URL_doc: " + enlace
        print(urlDoc)

        # Para un mejor funcionamiento maximizo la pestaña
        driver.maximize_window()

        # Para control, reviso si se ha abierto en browser el mismo enlace del documento
        urlActual = driver.current_url
        print("URL_init: " + urlActual)

        # Realizo una espera hasta que detecto que mi botón está cargado, si hay overtime
        # el programa se parará
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.presence_of_element_located((By.XPATH, busquedaXpath)))

        # Realizo otra espera para que el programa no se pare, para darle tiempo después de
        # encontrar el botón
        time.sleep(2)
        button.click()

        #Realizo una comprobación para ver si la URL después de pulsar el botón es igual o no
        urlPost = driver.current_url
        print("URL_post: " + urlPost)
        time.sleep(2)
        controlErrores = ControlErroresScrapping.controlErrores(urlActual, urlPost)

        # Grabo toda la información de los pasos que realiza la aplicación
        BaseDatosInsert.insertarRegistro(idNumEjecuciones, datetime.now(), filePath, busquedaXpath,
                                         urlDoc, urlActual, urlPost, controlErrores)

    driver.quit()
