# RETO CON FUNCIONES
#Crear un juego que consiste en un juego de dados, usando funciones, aparecerá un juego con tres opciones, 
#1: Juego de dados 2: juego de dados con apuesta  3: salir 
#Se pedirá al usuario, el número de partidas a jugar y en el caso de la opción 2, el dinero que vas a apostar en cada partida
 #Usaremos random tanto para el jugador como para la máquina, y tanto el la opción 1 como la 2, me tiene que decir el resultado del juego
 #ejemplo:
 #partidas ganadas por la máquina: 3
 #Partidas ganadas por el jugador: 4
 #En cada partida deberá aparecer tanto el dinero apostado, como el dinero ganado o perdido de la partida anterior.
#1º Partida
#El jugador ha apostado 100
#el jugador ha ganado 100
#total ganado/perdido 100
#así con el resto de partidas

import random 

#Funcion de lanzar un dado
def lanzar_dado():
    return random (2,6)

# 1:Juego basico de dados
def juego_dados():
    print("juego de dados")
    jugador = lanzar_dado()
    ordenador = lanzar_dado()

    print=int(f"tu dado:{jugador}")
    print=int(f"dado de la computadora: {ordenador}")
 
    if jugador > ordenador:
        print("ganas")
    elif jugador < ordenador:
        print("pierdes")
    else:
        print("empate")

# 2:Juego de dados con apuesta
def juego_de_dados_con_apuestas(dinero):
    print("juego de dados con apuestas")
    print("dinero actual: {dinero}")
    
    apuesta= int(input("ingreso de la apuesta: "))
    if apuesta > saldo:
        print("no tiene suficiente dinero")
        return dinero
    jugador=lanzar_dado()
    ordenador=lanzar_dado()
    print("el dado:{jugador}")
    print("dado del ordenador:{ordenador}")

    if jugador > ordenador:
        print("ganas la apuesta")
        dinero += apuesta
    elif jugador < ordenador:
        print("pierdes la apuesta")
        dinero -= apuesta

# 3:Salir
def salir():
    dinero = 1000
    while True:
     print("salir")
print("Juego de dados")
print("Juego de dados con apuesta")
print("Salir")


opcion = input("Selecciona una opción: ")

if opcion == "1":
    juego_dados()
elif opcion == "2":
    dinero = juego_de_dados_con_apuestas(dinero)
elif opcion == "3":
    print("gracias, ¡suerte a la proxima!")
else:
    print("error, intentelo de nuevo")

#Ejecutar el juego
menu()

