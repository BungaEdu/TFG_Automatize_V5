from Program.view import Front
from Program.data import BaseDatosConector


def main():
    # El front tiene que eestarse ejecutando siempre que
    # se abra el programa
    Front.ventana.mainloop()


if __name__ == '__main__':
    main()
    # Control para saber si la bd está bien conectada
    print(BaseDatosConector.mydb)
