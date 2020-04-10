# 0 1 2
# 3 4 5
# 6 7 8

casillas = [0 ,0, 0, 0, 0, 0, 0, 0, 0]

def mostrar_tablero():
    cont = 0
    for casilla in casillas:
        if casilla == 0:
            print("_ ", end="")
        elif casilla == 1:
            print("X ", end="")
        else:
            print("O ", end="")

        if cont == 2 or cont == 5 or cont == 8:
            print("")

        cont = cont + 1

def verificarGanador():
    # TODO
    # Debe devolver:
    #   0 : Si no hay un ganador
    #   1 : Si gano el jugador 1 
    #   2 : Si gano el jugador 2
    #  -1 : Si hay empate
    return 0

def jugar():
    # Repetir hasta que haya un ganador o empate
    #    jugado1 realiza jugada
    #    verificarGanador
    # .  Si hay ganador -> termina el juego
    # .  Si no hay ganador ->
    #    jugador2 realiza jugada
    #    verificarGanador
    # .  Si hay ganador -> termina el juego

    hayGanador = False
    jugador = "1"
    ganador = ""
    while not hayGanador:
        print("Jugador " + jugador)
        pos = input("Ingrese una posicion:")

        casillas[int(pos)] = int(jugador)

        ganador = verificarGanador()
        if ganador == 0:
            if jugador == "1":
                jugador = "2"
            else:
                jugador = "1"
        else:
            # Falta Verificar si hubo empate
            ganador = jugador
            hayGanador = True

        mostrar_tablero()
    
    if ganador == "":
        print("Hubo empate")
    else:
        print("El ganador fue " + ganador)


jugar()