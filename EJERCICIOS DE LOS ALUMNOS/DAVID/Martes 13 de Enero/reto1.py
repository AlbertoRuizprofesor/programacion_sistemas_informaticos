import random

def lanzar_dados():
    """Genera los valores aleatorios para ambos jugadores."""
    return random.randint(1, 6), random.randint(1, 6)

def jugar(con_apuesta):
    try:
        num_partidas = int(input("\n¿Número de partidas a jugar?: "))
    except ValueError:
        print("Error: Debes ingresar un número entero.")
        return

    victorias_j = 0
    victorias_m = 0
    saldo_acumulado = 0
    apuesta_fija = 0

    if con_apuesta:
        try:
            apuesta_fija = float(input("Dinero a apostar en cada partida: "))
        except ValueError:
            print("Error: Debes ingresar un valor numérico para la apuesta.")
            return

    for i in range(1, num_partidas + 1):
        print(f"\n{i}º Partida")
        
        # 1. Obtener valores de los dados
        dado_jugador, dado_maquina = lanzar_dados()
        print(f"El jugador ha sacado: {dado_jugador}")
        print(f"La máquina ha sacada: {dado_maquina}")

        if con_apuesta:
            print(f"El jugador ha apostado {apuesta_fija}")

        # 2. Determinar ganador y calcular dinero
        if dado_jugador > dado_maquina:
            victorias_j += 1
            print("Resultado: ¡Ganaste!")
            if con_apuesta:
                saldo_acumulado += apuesta_fija
                print(f"El jugador ha ganado {apuesta_fija}")
        
        elif dado_maquina > dado_jugador:
            victorias_m += 1
            print("Resultado: Perdiste")
            if con_apuesta:
                saldo_acumulado -= apuesta_fija
                print(f"El jugador ha perdido {apuesta_fija}")
        
        else:
            print("Resultado: Empate (no se gana ni se pierde dinero)")

        # 3. Mostrar balance actual si hay apuesta
        if con_apuesta:
            print(f"Total ganado/perdido: {saldo_acumulado}")

    # Resumen final del bloque de partidas
    print("\n" + "="*30)
    print("RESUMEN DE RESULTADOS")
    print(f"Partidas ganadas por la máquina: {victorias_m}")
    print(f"Partidas ganadas por el jugador: {victorias_j}")
    print("="*30)

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1: Juego de dados")
        print("2: Juego de dados con apuesta")
        print("3: Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            jugar(con_apuesta=False)
        elif opcion == "2":
            jugar(con_apuesta=True)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, marca 1, 2 o 3.")

if __name__ == "__main__":
    menu()