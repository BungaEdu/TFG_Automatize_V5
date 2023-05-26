from Program.view import Front
from Program.data import BaseDatosConector


def main():
    Front.ventana.mainloop()


if __name__ == '__main__':
    main()
    print(BaseDatosConector.mydb)
