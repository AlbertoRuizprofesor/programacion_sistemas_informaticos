#JUEGO PAPEL PIEDRA Y TIJERAS CON FUNCION DEF:
import random

def jugada_maquina():
    return random.randint(1,3)

def obtener_jugada_jugador():
    return int(input("Elige una opción 1(piedra), 2(tijera), 3(papel): "))

def mostrar_opciones(jugador, maquina):
    opciones={1:"piedra", 2:"tijera", 3:"papel"}
    print(f"Usted ha elegido {opciones[jugador]}")
    print(f"La máquina ha elegido {opciones[maquina]}")
    
def determinar_ganador(jugador, maquina):
    if jugador == maquina:
        return "empate"
    elif (jugador==1 and maquina==2) or \
         (jugador==2 and maquina==3) or \
         (jugador==3 and maquina==1):
             return "jugador"
    else:
        return "maquina"
    
def jugar_partida():
    maquina=jugada_maquina()
    jugador=obtener_jugada_jugador()
    mostrar_opciones(jugador, maquina)
    return determinar_ganador(jugador, maquina)

def main():
    gana_jugador=0
    gana_maquina=0
    empates=0
    
    while True:
        continuar=input("¿Quieres jugar? (si/no): ").lower()
        
        if continuar=="no":
            break
        
        resultado=jugar_partida()
        
        if resultado=="empate":
            print("Empate.")
            empates +=1
            
        elif resultado=="jugador":
            print("¡Usted ha ganado!")
            gana_jugador+=1
            
        else:
            print("Ha ganado maquina.")
            gana_maquina+=1
            
    print("\nResultados Finales")
    print("Partidas ganadas por el jugador", gana_jugador)       #Tienen que estar dentro del MAIN()
    print("Partidas ganadas por la máquina:", gana_maquina)     
    print("Empates:", empates)     
        
main()