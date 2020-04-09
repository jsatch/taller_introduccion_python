def tam(lista):
    cont = 0
    for i in lista:
        cont = cont + 1
    return cont


lista_nombres = ["Pepe", "Juan"]

tamano_lista = tam(lista_nombres)

for indice in range(tamano_lista):
    print(lista_nombres[indice])

#indice = 0
#while indice < 3:
#    print(lista_nombres[indice])
#    indice = indice + 1

print("Acabo el programa")