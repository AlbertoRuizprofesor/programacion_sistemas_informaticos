#Ejercicio Juego papel, tijeras y piedra.


import random

#random e input

numero=random.randint(1,3)  #pc=
jugador=int(input("Elige una opcion 1(piedra), 2(tijera), 3(papel): "))


opciones={1:"piedra", 2:"tijera", 3:"papel"}
print(f"Usted ha elegido  {opciones[jugador]}")
print(f"La máquina ha elegido {opciones[numero]}")

if jugador == numero:
    print("Empate")
    
elif (jugador == 1 and numero == 2) or \
     (jugador == 2 and numero == 3) or \
     (jugador ==3 and numero == 1):
        print(f"{opciones[jugador]} gana a {opciones[numero]} Usted ha ganado!") #print("ha ganado", jugador)
                 
                 
else:

    print(f"{opciones[numero]} gana a {opciones[jugador]} ha ganado la maquina!") #print("ha ganado", pc)

