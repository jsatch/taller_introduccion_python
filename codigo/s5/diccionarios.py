""" 
{
    'pepito': {
        'twitter': '@pepito', 
        'numero': '123432523'
    }, 
    'juanito': {
        'twitter': '@juanito', 
        'numero': '2134324'
    },
}
 """

# [ [ "Pepito", "@pepito", "234234"  ] , [ "Juanito", "@juanito", "2342342"] ]
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

    
print(lista_amigos)