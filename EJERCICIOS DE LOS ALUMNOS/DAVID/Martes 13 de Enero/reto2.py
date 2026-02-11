import random

def obtener_eleccion_maquina():
    opciones = ["piedra", "papel", "tijeras"]
    return random.choice(opciones)

def determinar_ganador(jugador, maquina):
    # Retorna: 0 si hay empate, 1 si gana jugador, 2 si gana máquina
    if jugador == maquina:
        return 0
    
    # Casos en los que gana el jugador
    if (jugador == "piedra" and maquina == "tijeras") or \
       (jugador == "papel" and maquina == "piedra") or \
       (jugador == "tijeras" and maquina == "papel"):
        return 1
    else:
        # En cualquier otro caso, gana la máquina
        return 2

def jugar():
    print("--- BIENVENIDO AL PIEDRA, PAPEL O TIJERAS ---")
    
    victorias_j = 0
    victorias_m = 0
    
    try:
        num_partidas = int(input("\n¿A cuántas partidas quieres jugar?: "))
    except ValueError:
        print("Error: Ingresa un número válido.")
        return

    for i in range(1, num_partidas + 1):
        print(f"\n--- {i}º RONDA ---")
        
        # Elección del jugador
        eleccion_j = input("Elige (piedra, papel, tijeras): ").lower()
        while eleccion_j not in ["piedra", "papel", "tijeras"]:
            eleccion_j = input("Opción no válida. Escribe piedra, papel o tijeras: ").lower()

        # Elección de la máquina
        eleccion_m = obtener_eleccion_maquina()
        print(f"La máquina eligió: {eleccion_m}")

        # Determinar resultado
        resultado = determinar_ganador(eleccion_j, eleccion_m)

        if resultado == 0:
            print("¡Es un empate!")
        elif resultado == 1:
            print(f"¡Ganaste la ronda {i}!")
            victorias_j += 1
        else:
            print(f"La máquina gana la ronda {i}")
            victorias_m += 1

        print(f"Marcador actual -> Jugador: {victorias_j} | Máquina: {victorias_m}")

    print("\n" + "="*30)
    print("RESUMEN FINAL")
    print(f"Puntuación del Jugador: {victorias_j}")
    print(f"Puntuación de la Máquina: {victorias_m}")
    
    if victorias_j > victorias_m:
        print("¡RESULTADO: ERES EL CAMPEÓN!")
    elif victorias_m > victorias_j:
        print("¡RESULTADO: LA MÁQUINA HA GANADO!")
    else:
        print("¡RESULTADO: EMPATE FINAL!")
    print("="*30)

# Iniciar el juego
if __name__ == "__main__":
    jugar()