print("Reto juego de dados")
print("")
print("")

from random import randint

# Función MENÚ para iniciar el juego

def menu():
    menu=True
    while menu:
        print("1- Juego de dados.")
        print("2- Juego de dados con apuesta.")
        print("3- Salir.")
        opc=int(input("Elige una opción: "))
        if opc==1:
            juego1()
        elif opc==2:
            juego2()
        elif opc==3:
            menu=False    
    


# Función para iniciar el juego sin apuestas.
    
def juego1():
    npartidas=int(input("Cuántas partidas quieres jugar??? "))
    gana1=0
    gana2=0
    empate=0
    partida=[]
    for i in range (npartidas):
        jugador1=randint(1,6)
        print(f"Jugador 1 ha salido: {jugador1}")
        jugador2=randint(1,6)
        print(f"Jugador 2 ha salido: {jugador2}")
        partida.append((jugador1,jugador2))
        if jugador1>jugador2:
            print("Jugador 1 gana!!!")
            gana1+=1
        elif jugador2>jugador1:
            print("Jugador 2 gana!!!")
            gana2+=1
        else:
            empate+=1
    print(f"El resultado de la partida es: {gana1} - {gana2}, empates: {empate}")
    for x in range (len(partida)):
        print(f"Jugada {x+1}: Jugador 1: {partida[x][0]} - Jugador 2: {partida[x][1]} ")
    print("")
    print("")


# Función para iniciar el juego con apuestas.

def juego2():
    credito=int(input("¿ Cuánto dinero quieres jugar en total? "))
    npartidas=int(input("Cuántas partidas quieres jugar??? "))
    gana1,gana2,empate,apuesta=0,0,0,0
    partida=[]
    
    while credito>0 and npartidas>0:
        apuesta=int(input(f"¿ Cuánto quieres apostar esta partida? Saldo disponible: {credito}€: "))
        if apuesta<=credito: 
            jugador1=randint(1,6)
            print(f"Jugador 1 ha salido: {jugador1}")
            jugador2=randint(1,6)
            print(f"Jugador 2 ha salido: {jugador2}")
            if jugador1>jugador2:
                print("Jugador 1 gana!!!")
                gana1+=1
                credito=credito+apuesta
            elif jugador2>jugador1:
                print("Jugador 2 gana!!!")
                gana2+=1
                credito=credito-apuesta
            else:
                print("Empate!!!")
                empate+=1
            partida.append((jugador1,jugador2))
            npartidas-=1
            print(f"Partidas restantes: {npartidas}")
        elif apuesta>credito:
            print("No tienes saldo suficiente para jugar ese importe, prueba otra cantidad.")    
    if credito==0:
        print("La partida ha terminado por falta de crédito. Vuelve cuando quieras!!!")
    elif npartidas==0:
        ("Fin de la partida!!!")    
    print(f"El resultado de la partida es: {gana1} - {gana2}, empates: {empate}")
    for x in range (len(partida)):
        print(f"Jugada {x+1}: Jugador 1: {partida[x][0]} - Jugador 2: {partida[x][1]} ")
    print("")
    print("")
    
# Cuerpo de programa.

menu()


# Fin de programa.