# ---------FUNCIONES---------
# Jugador gana a la máquina
def jugador_gana(jugada,num):
    return (
        (jugada == 1 and num == 3) or  # papel gana a piedra
        (jugada == 2 and num == 1) or  # tijera gana a papel
        (jugada == 3 and num == 2)     # piedra gana a tijera
    )

# Juego
def jugar():
    import random
    nombres = {1: "Papel", 2: "Tijera", 3: "Piedra"} # Diccionario para las jugadas
    
    print("\nElije una opción para jugar siendo:\n1.Papel.\n2.Tijera.\n3.Piedra.")
    jugada=int(input("Elije una opción:")) # Jugador elige movimiento
    
    num=random.randint(1, 3) # Máquina elige movimiento de forma aleatoria
    
    # Comprobar que el jugador ha elegido una opción válida
    if jugada <= 3 and jugada >= 1:
        print(f"\nTú: {nombres[jugada]} | Máquina: {nombres[num]}") # Saber los movimientos
        
        # Resultados
        if jugada == num:
            print("Empate")
            return "Empate"
        elif jugador_gana(jugada,num):
            print("Ganaste")
            return "Jugador"
        else: 
            print("Maquina gana")
            return "Maquina"
    else:
        print("Opcion no valida")

# Menú
def menu():
    # Contadores para saber las victorias
    jugador = 0
    maquina = 0
    
    # Bucle para jugar
    while True:
        # Menú para decidir que hacer
        print("\n----MENÚ----")
        print("1.jugar\n2.salir")
        opcion = int(input("Elige una opcion: "))
        
        # Resultado de las opciones
        match opcion:
            # Se elige jugar
            case 1:
                # El resultado será lo que nos devuelva los 'returns' de la función 'jugar'
                resultado = jugar()

                # Ver resultado y sumar puntos al ganador
                if resultado == "Jugador":
                    jugador += 1
                elif resultado == "Maquina":
                    maquina += 1
            # Se elige salir
            case 2:
                # Mostrar puntuaciones finales
                print(f"\nPuntuación jugador: {jugador}")
                print(f"Puntuación máquina: {maquina}")  
                break # Salir del bucle
            # En caso de que la opción introducida no sea valida
            case _:
                print("No es una opción")
                continue

# ---------PROGRAMA---------
# Llamada a la función 'menu'
menu()