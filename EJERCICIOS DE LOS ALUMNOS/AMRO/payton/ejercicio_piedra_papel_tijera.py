##1º Modificar el ejercicio de piedra, papel, tijeras, de manera que usemos un bucle con dos opciones
##1...jugar 2 salir, mientres le de a jugar, jugaremos una partida de piedra, papel, tijeras, deberá
##sumarme el número de partidas ganadas por la máquina y el número de partidas ganadas por el usuario.

import random

ganador_Maquina=0
ganador_jugador=0
empate=0
opcion=True

while opcion:
    print("elige una opcion 1: jugar 2: salir")
    elegir=int(input("dime la opcion: "))
    if elegir==1:  
        maquina=random.randint(1, 3)  # 

        jugador=int(input("Elige una opcion 1(piedra)2(papel)3(tijeras): "))
        if jugador==1 and maquina==1 or jugador==2 and maquina==2 or jugador==3 and maquina==3:
            print("Empate")
            empate=empate+1
        elif jugador==1 and maquina==3 or jugador==2 and maquina==1 or jugador==3 and maquina==2:
            print("Gana el jugador")
            ganador_jugador=ganador_jugador+1
        else:
            print("Gana la maquina")
            ganador_Maquina=ganador_Maquina+1
    elif elegir==2:
        opcion=False
        print("Saliendo del juego")
    else:
        print("Opcion no valida")
print(f"El jugador ha ganado: {ganador_jugador} veces")
print(f"La maquina ha ganado: {ganador_Maquina} veces")
print(f"Han empatado: {empate} veces")