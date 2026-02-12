#Juego de dados: Crear un juego que consiste en un juego de dados, usando funciones, aparecerá un juego con tres opciones, 
#1: Juego de dados 2: juego de dados con apuesta  3: salir
#Se pedirá al usuario, el número de partidas a jugar y en el caso de la opción 2, el dinero que vas a apostar en cada partida
#Usaremos random tanto para el jugador como para la máquina, y tanto el la opción 1 como la 2, me tiene que decir el resultado del juego
#ejemplo:
#partidas ganadas por la máquina: 3
#Partidas ganadas por el jugador: 4
#En cada partida deberá aparecer tanto el dinero apostado, como el dinero ganado o perdido de la partida anterior.

import random

def tirar_dado():
    return random.randint(1,6)

def jugar_partida():
    jugador=tirar_dado()
    maquina=tirar_dado()
    
    print(f"Usted ha sacado {jugador}")
    print(f"La máquina ha sacado {maquina}")
    
    if jugador==maquina:
        return "Empate."
    elif jugador > maquina:
        return "jugador"
    else:
        return "maquina"

def juego_dados(partidas):
    gana_jugador=0
    gana_maquina=0
    empates=0
    
    for i in range(partidas):
        print(f"\nPartida {i+1}")
        resultado= jugar_partida()
        
        if resultado=="jugador":
            print("¡Gana el jugador!")
            gana_jugador+=1
            
        elif resultado=="maquina":
            print("Gana máquina!")
            gana_maquina+=1
            
        else:
            print("Empate.")    
            empates+=1
            
    print("\nResultados Finales.")
    print("Partidas ganadas por el jugador", gana_jugador)
    print("Partidas ganadas por la máquina", gana_maquina)
    print("Empates:",empates)
    
def juego_dados_apuestas(partidas, apuesta):
    dinero=0
    
    for i in range(partidas):
        print(f"\nPartida {i+1}")
        print("Apuesta actual: ", apuesta)
        
        resultado= jugar_partida()
        
        if resultado=="jugador":
            dinero +=apuesta
            print("Ganaste:", apuesta)
            
        elif resultado=="maquina":
            dinero-=apuesta
            print("Perdiste", apuesta)
        else:
            print("Empate, no ganas ni pierdes.")
            
        print("Dinero acumulado: ", dinero)
        
        
# MAIN() INDICA DONDE COMIENZA EL PROGRAMA:
        
def main():
    while True:
        print("\nMENÚ")
        print("1.Juego de dados.")
        print("2.Juego de apuestas.")
        print("3.Salir.")
        
        opcion=input("Elige una opción: ")
        
        if opcion=="1":
            partidas=int(input("Número de partidas: "))
            juego_dados(partidas)
            
        elif opcion=="2":
            partidas=int(input("Número de partidas: "))
            apuesta=int(input("Dinero a apostar por partida: "))
            juego_dados_apuestas(partidas,apuesta)
            
        elif opcion=="3":
            print("Saliendo del juego....")
            break
        
        else:
            print("Opción incorrecta.")
            
#HAY QUE DECLARAR MAIN() AL FINAL SIEMPRE PARA QUE SE EJECUTE.
            
main()



    

            
    
    
        
            
        