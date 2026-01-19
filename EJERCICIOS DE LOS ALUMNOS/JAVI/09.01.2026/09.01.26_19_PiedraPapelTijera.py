import random

option = 1
jugar = True
while option:
    print("1-Jugar / 0-Salir")
    n = int(input("Elige, Bro: "))

    if n == 1:
        maquina=random.randint(1,3)
        while jugar==True
        print("Has elegido Jugar, Bro")
        jugador =int(input("Elige Bro, 1-Piedra, 2-Papel, 3-Tiejera, 0-Salir "))
        if jugador==0:
            jugar=False
        elif jugador>3:
            print("Vuelve a Intentarlo")
        else:
            if maquina==jugador:
                empate +=1
                print("Empate")
            elif maquina==1 and jugador==2:
    



    elif n == 0:
        print("Has elegido Salir, Bro")
        option = 0