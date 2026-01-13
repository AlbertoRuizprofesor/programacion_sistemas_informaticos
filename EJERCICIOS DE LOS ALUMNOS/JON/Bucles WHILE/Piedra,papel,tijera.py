print("Piedra, papel o tijera")
print("")
print("")
import random
opcion=True
while opcion:
    print("1 jugar 2 salir ")
    eleccion=int(input("Elige una opcion: "))
    if eleccion==1:
        jugador1=int(input("Jugador 1, elige piedra: 1 , papel: 2 ó tijera: 3 :"))
        jugador2=random.randint(1,3)
        print("El jugador 2 ha elegido: ", jugador2)
        if jugador1==jugador2:
            print("Empate!")
        elif (jugador1==1 and jugador2==3) or (jugador1==2 and jugador2==1) or (jugador1==3 and jugador2==2):
            print("¡Jugador 1 gana!")
        else:
            print("¡Jugador 2 gana!")
    elif eleccion==2:
        print("Has elegido salir")
        opcion=False

print("Fin del programa")