import functions as fc

def print_hi(name):

    option = int(input("Introdueix què vols fer amb el fitxer: 1)Crear   2)Mostrar contingut 3)modificar contingut  4)sortir"))

    if option == 1:
        fc.create_file_content()
    elif option == 2:
        fc.read_file()
    elif option==3:
        fc.append_text()
    elif option == 4:
        print("Has sortit del programa")


if __name__ == '__main__':
    print_hi('PyCharm')


