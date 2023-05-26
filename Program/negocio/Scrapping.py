import time
from datetime import datetime
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Program.data import BaseDatosInsert
from Program.resources import ControlErroresScrapping


def doScrappingWeb(idNumEjecuciones, columna, busquedaXpath, filePath):
    driver = webdriver.Chrome()

    for enlace in columna:
        driver.get(enlace)
        urlDoc = "URL_doc: " + enlace
        print(urlDoc)
        driver.maximize_window()
        urlActual = driver.current_url
        print("URL_init: " + urlActual)
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.presence_of_element_located((By.XPATH, busquedaXpath)))
        time.sleep(2)
        button.click()
        urlPost = driver.current_url
        print("URL_post: " + urlPost)
        time.sleep(2)
        controlErrores = ControlErroresScrapping.controlErrores(urlActual, urlPost)
        BaseDatosInsert.insertarRegistro(idNumEjecuciones, datetime.now(), filePath, busquedaXpath, urlDoc,
                                         urlActual, urlPost, controlErrores)

    driver.quit()
