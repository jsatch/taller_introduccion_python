print("Ingrese edad:")
edad = input()
# edad <- "20"

edad = int(edad)
# edad <- 20

if edad < 18:
    print("Es menor de edad")
elif edad <= 30:
    print("Es un adulto joven")
elif edad <= 65:
    print("Es un adulto")
else:
    print("Es un adulto mayor")

print("Termino el programa")