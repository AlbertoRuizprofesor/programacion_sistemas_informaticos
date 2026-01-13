import random

# Variables de control y marcadores
continuar_programa = True
ganadas_usuario = 0
ganadas_maquina = 0

# Diccionario de reglas para que sea escalable (fácil de ampliar)
REGLAS = {
    "piedra": "tijeras",
    "papel": "piedra",
    "tijeras": "papel"
}

while continuar_programa:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Jugar a Piedra, Papel o Tijeras")
    print("2. Salir y ver resultados")
    
    eleccion = input("Elige una opción: ")

    if eleccion == "1":
        # Pedimos el nombre antes de empezar las rondas
        nombre = input("Introduce tu nombre de usuario: ")
        print(f"\n¡Bienvenido {nombre}! (Escribe 'salir' para volver al menú principal)")
        
        # BUCLE DE JUEGO CONTINUO
        jugando_rondas = True
        while jugando_rondas:
            usuario = input(f"\n{nombre}, elige (piedra, papel, tijeras) o 'salir': ").lower()

            if usuario == "salir":
                jugando_rondas = False
                print("Regresando al menú principal...")
            elif usuario in REGLAS:
                maquina = random.choice(list(REGLAS.keys()))
                print(f"La máquina eligió: {maquina}")

                if usuario == maquina:
                    print("¡Empate!")
                elif REGLAS[usuario] == maquina:
                    print(f"¡Punto para {nombre}!")
                    ganadas_usuario += 1
                else:
                    print("¡Punto para la máquina!")
                    ganadas_maquina += 1
            else:
                print("Opción no válida. Inténtalo de nuevo.")

    elif eleccion == "2":
        # Salida del programa y estadísticas finales
        print("\n" + "="*30)
        print("ESTADÍSTICAS FINALES")
        print(f"Partidas ganadas por el usuario: {ganadas_usuario}")
        print(f"Partidas ganadas por la máquina: {ganadas_maquina}")
        print("="*30)
        print("¡Gracias por jugar! Saliendo...")
        continuar_programa = False

    else:
        print("Opción no válida. Por favor, pulsa 1 o 2.")