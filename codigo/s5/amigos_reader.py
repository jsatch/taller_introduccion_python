import json

print("Programa obtencion de datos de amigos")
nombre = input("Ingrese nombre de amigo:")

#Abrir el archivo para obtener informacion
archivo = open("amigos.txt", "r")
lista_amigos_json = archivo.readline()
lista_amigos = json.loads(lista_amigos_json)
archivo.close()

#Buscar el amigo
if nombre in lista_amigos:
    amigo = lista_amigos[nombre]
    twitter = amigo["twitter"]
    numero = amigo["numero"]

    # Imprimir datos del amigo
    print("--Datos del amigo--")
    print("Nombre: " + nombre)
    print("Twitter: " + twitter)
    print("Numero: " + numero)
else:
    print("No existe el amigo")