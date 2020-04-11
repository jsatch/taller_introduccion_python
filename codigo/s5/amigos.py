import json

lista_amigos = {}

continuar = True
while continuar == True:
    persona = []
    print("---- Datos de amigo ----")
    nombre = input("Nombre: ")
    twitter = input("Twitter: ")
    numero = input("Telefono: ")
    opcion = input("Desea continuar? Si (s) No (n): ")
    if opcion == "n":
        continuar = False

    lista_amigos[nombre] = {
        "twitter" : twitter,
        "numero" : numero
    }

# Guardado de datos
archivo = open("amigos.txt", "a")
lista_amigos_json = json.dumps(lista_amigos)
archivo.write(lista_amigos_json)
archivo.close()