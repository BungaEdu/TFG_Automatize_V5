def controlErrores(urlInit, urlPost):
    if urlInit != urlPost:
        resultado = "OK"
    else:
        resultado = "Algo ha ido mal"
    return resultado