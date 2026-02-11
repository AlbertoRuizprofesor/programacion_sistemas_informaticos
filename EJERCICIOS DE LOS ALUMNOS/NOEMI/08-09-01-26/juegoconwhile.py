#Bucle papel y tijera.

import random

gana_maquina=0
gana_jugador=0
empate=0

jugar=True


while jugar:
    continuar=input("Quieres jugar? (si/no): ").lower()
    
    if continuar == "no":
        jugar=False
        break
    
    numero=random.randint(1,3)  #pc=
    jugador=int(input("Elige una opcion 1(piedra), 2(tijera), 3(papel): "))

    opciones={1:"piedra", 2:"tijera", 3:"papel"}
    print(f"Usted ha elegido  {opciones[jugador]}")
    print(f"La máquina ha elegido {opciones[numero]}")

    if jugador == numero:
        print("Empate")
        empate +=1
    
    elif (jugador == 1 and numero == 2) or \
         (jugador == 2 and numero == 3) or \
         (jugador ==3 and numero == 1):
        print(f"{opciones[jugador]} gana a {opciones[numero]} Usted ha ganado!") #print("ha ganado", jugador)
        gana_jugador +=1        
                 
    else:

         print(f"{opciones[numero]} gana a {opciones[jugador]} ha ganado la maquina!") #print("ha ganado", pc)
         gana_maquina+=1

print("Partidas ganadas por el jugador: ", gana_jugador)
print("Partidas ganadas por la máquina: ", gana_maquina)
print("Empate entre máquina y jugador: ", empate)