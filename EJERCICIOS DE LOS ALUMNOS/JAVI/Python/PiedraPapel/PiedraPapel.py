import random
#random e input

numero=random.randint(1, 3)

jugador = int(input("Piedra: 1 , Papel: 2 , Tijeras: 3 : "))
com = numero


if jugador == com:
    print ("Empate. COM sacó: " , com)

else:
    if (jugador == 1 and com == 3) or (jugador == 2 and com == 1) or (jugador == 3 and com ==2):
        print ("Has ganado. COM sacó: " , com)
    else:
        print ("Has perdido. COM sacó: " , com)






