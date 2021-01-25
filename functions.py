def save_text():
    text = input("Introdueix el text a insertar al arxiu")
    f = open("test.txt", "w")
    f.write(text)
    f.close()

def append_text():
    text = input("Introdueix el text a afegir al arxiu")
    file_name = input("Introdueix nom de fitxer")
    f = open(file_name, "a+")
    f.write(text)
    f.close()

def create_file_content():
    text = input("Introdueix el text a afegir al arxiu")
    f_name = input("introdueix el nom del fitxer a crear")
    f = open(f_name, "a+")
    f.write(text)
    f.close()

def read_file():
    f_name = input("introdueix el nom del fitxer a llegir")
    f = open(f_name, "r")
    for x in f:
        print(x)
    f.close()