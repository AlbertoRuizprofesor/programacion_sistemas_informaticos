import random

opcion = 0

while opcion != 2:
    print("\n1. Jugar")
    print("2. Salir")
    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        jugador = int(input("Elija: 1=Piedra, 2=Papel, 3=Tijeras: "))
        maquina = random.randint(1, 3)

        if maquina == 1:
            print("La máquina eligió Piedra")
        elif maquina == 2:
            print("La máquina eligió Papel")
        else:
            print("La máquina eligió Tijeras")

        if jugador == maquina:
            print("Empate")
        elif (jugador == 1 and maquina == 3) or \
             (jugador == 2 and maquina == 1) or \
             (jugador == 3 and maquina == 2):
            print("¡Usted gana!")
        else:
            print("La máquina gana")

    elif opcion == 2:
        print("Saliendo del juego...")
    else:
        print("Opción incorrecta")
