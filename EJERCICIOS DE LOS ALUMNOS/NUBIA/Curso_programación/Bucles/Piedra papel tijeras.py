print("Juego de Piedra, Papel o Tijera")
import random
opcion = True

while opcion:
    print("1. Jugar, 2. Salir")
    eleccion = int(input("Elige una opción: "))
    
    if eleccion == 1:
        eleccion_usuario = int(input("Elige 1 para piedra, 2 para papel, 3 para tijera: "))
        eleccion_pc = random.randint(1, 3)
        print(f"El PC ha elegido {eleccion_pc}")
        if eleccion_usuario == eleccion_pc:
            print("¡Es un empate!")
        elif (eleccion_usuario == 1 and eleccion_pc == 3) or (eleccion_usuario == 2 and eleccion_pc == 1) or (eleccion_usuario == 3 and eleccion_pc == 2):
            print("¡Ganaste!")
        else:
            print("¡Perdiste!")
    elif eleccion == 2:
        opcion = False
        print("Gracias por jugar")

