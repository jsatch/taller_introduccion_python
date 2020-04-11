archivo = open("archivo1.txt", "r")

terminado = False
while not terminado:
    linea = archivo.readline()
    if not linea:
        terminado = True
    else:
        print(linea, end="")

archivo.close()
