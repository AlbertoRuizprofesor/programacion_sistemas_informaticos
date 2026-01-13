# ---------FUNCIONES---------

# Opción 1. Solo mira como juega sin apostar.
def opcion1(jugador,maquina,puntos_jugador,puntos_maquina,empates):
    if jugador > maquina:
        puntos_jugador += 1
        print(f"Jugador: {jugador}\nMáquina: {maquina}\nGana jugador")
    elif jugador < maquina:
        puntos_maquina += 1
        print(f"Jugador: {jugador}\nMáquina: {maquina}\nGana máquina")
    else: 
        empates += 1
        print(f"Jugador: {jugador}\nMáquina: {maquina}\nEmpate")

    return puntos_jugador,puntos_maquina,empates

# Opción 2. Juega apostando
def opcion2(jugador, maquina, puntos_jugador, puntos_maquina, empates, dinero, apuesta):
    # Si 'dinero' es mayor a 0 juega
    if dinero > 0:
        if jugador > maquina:
            puntos_jugador += 1
            dinero += apuesta
            print(f"Jugador: {jugador}\nMáquina: {maquina}\nHas ganado {apuesta}")
        elif jugador < maquina:
            puntos_maquina += 1
            dinero -= apuesta
            print(f"Jugador: {jugador}\nMáquina: {maquina}\nHas perdido {apuesta}")
        else:
            empates += 1
            print("Empate")
    # Muestra el saldo actual.
    print(f"Saldo actual: {dinero}\n")
    return puntos_jugador, puntos_maquina, empates, dinero

# Juego
def juego(opcion,partidas):
    import random
    x = 1
    puntos_maquina = 0
    puntos_jugador = 0
    empates = 0
    
    # Preguntar lo que quiere añadir de saldo para apostar
    if opcion == 2:
        dinero_inicial = int(input("¿Cuánto dinero quieres añadir? "))
        dinero = dinero_inicial

    # Jugar el número de partidas que ha decidido el usuario
    while x <= partidas:
        # Dar un valor aleatorio entre 1 y 6
        jugador=random.randint(1, 6)
        maquina=random.randint(1, 6)
        
        # Elegir la opción 1 y llamar a su función
        if opcion == 1:
            print(f"\nPartida numero {x}")
            puntos_jugador, puntos_maquina, empates = opcion1(jugador, maquina, puntos_jugador, puntos_maquina, empates)
        # Elegir la opción 2 y llamar a su función
        elif opcion == 2:
            print(f"\nPartida numero {x}(Puedes apostar hasta {dinero}€):")
            # Indicar cuanto quieres apostar en cada jugada
            apuesta = int(input("¿Cuánto quieres apostar en esta jugada? "))
            
            # Si apuestas 0 o un número negativo
            if apuesta <= 0:
                print("La apuesta debe ser mayor que 0")
                continue
            
            # Decir que no puedes apostar más de lo que tienes
            if apuesta > dinero:
                print("¿Que haces payaso? Tienes menos de lo que puedes dar, por eso te dejó ella.")
                continue       
            # Poder jugar si apuestas menos o todo lo que tienes
            elif apuesta <= dinero:
                puntos_jugador, puntos_maquina, empates, dinero = opcion2(jugador, maquina, puntos_jugador, puntos_maquina, empates, dinero, apuesta)
                
        # Si te quedas sin dinero y quieres seguir jugando
        if opcion == 2 and dinero <= 0:
            volver = input("No tienes dinero. ¿Quieres añadir más? (S/N): ")
            # Jugar otra vez
            if volver.upper() == "S":
                print("ERES UN PUTO LUDOPATA!!!")
                juego(opcion,partidas)
            # No jugar más
            elif  volver.upper() == "N":
                print("La banca siempre gana. Largate tieso de mierda")
                break
            # No poner la opción
            else:
                print("Imbécil, 'S' o 'N'")

        x += 1
        
        #Para que no vaya todo seguido
        input("Pulsa 'Enter' para la siguiente tirada.")
    
    print(f"\nPartidas ganadas por la máquina: {puntos_maquina}")
    print(f"Partidas ganadas por el jugador: {puntos_jugador}")
    print(f"Partidas empatadas: {empates}\n")

# Menú
def menu():
    while True:
        print("Bienvenido a este casino. ¿Que desea hacer?")
        print("1. Jugar dados.\n2. Jugar dados con apuesta.\n3. Salir.")
        opcion = int(input("Elija una opción: "))

        # Seleccionar la opción y llamar a la función juego
        match opcion:
            case 1:
                partidas = int(input("\n¿Cuántas partidas quieres jugar? "))
                juego(opcion, partidas)
            case 2:
                partidas = int(input("\n¿Cuántas partidas quieres jugar? "))
                juego(opcion, partidas)        
            case 3:
                print("Adiós")
                break
            case _:
                print("No es una opción")

# ---------PROGRAMA PRINCIPAL---------
menu()