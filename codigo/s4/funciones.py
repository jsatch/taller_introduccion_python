
lista_numeros = [0 , 1 , 2]
lista_numeros.append(4)
print(lista_numeros)
lista_numeros.pop(0)
print(lista_numeros)
print(len(lista_numeros))

# Definicion de una funcion
def conversar(nombre, edad):
    print("Hola " + nombre)
    print("Edad: " + str(edad))

def sumar(num1, num2):
    res = num1 + num2
    return res

def despedir():
    print("Adios")

conversar("Pepito", 20) # Estoy ejecutando la funcion
despedir()
respuesta = sumar(5, 8)
print(respuesta)