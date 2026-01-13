import random

ganadas = 0
perdidas = 0
empates = 0

opcion = int(input("¿Quieres jugar una partida? Sí(1) No(2): "))

if opcion == 1:
    jugador = int(input("Elige: 1.Piedra | 2.Papel | 3.Tijera: "))
    com = random.randint(1, 3)

    if jugador == com:
        empates += 1
        print("Empate. COM sacó:", com)

    elif (jugador == 1 and com == 3) or (jugador == 2 and com == 1) or (jugador == 3 and com == 2):
        ganadas += 1
        print("Has ganado. COM sacó:", com)

    else:
        perdidas += 1
        print("Has perdido. COM sacó:", com)

else:
    print("Juego cancelado.")

    

        

