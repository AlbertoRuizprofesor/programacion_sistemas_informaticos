#  1º RETO CON FUNCIONES:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
 
#  Crear un juego que consiste en un juego de dados, usando funciones, aparecerá un juego con tres opciones, 
#  1: Juego de dados 2: juego de dados con apuesta  3: salir
 
#  Se pedirá al usuario, el número de partidas a jugar y en el caso de la opción 2, el dinero que vas a apostar en cada partida
 
#  Usaremos random tanto para el jugador como para la máquina, y tanto el la opción 1 como la 2, me tiene que decir el resultado del juego
#  ejemplo:
 
#  partidas ganadas por la máquina: 3
#  Partidas ganadas por el jugador: 4
#  En cada partida deberá aparecer tanto el dinero apostado, como el dinero ganado o perdido de la partida anterior.

# 1º Partida

# El jugador ha apostado 100
# el jugador ha ganado 100
# total ganado/perdido 100

# así con el resto de partidas

# 1️⃣ Importar librería

# Escribe: import random

# 2️⃣ Función mostrar_menu()

# Imprime menú con 3 opciones

# Pide al usuario que ingrese su opción usando input()

# Convierte la opción a número si quieres

# Devuelve la opción

# Tip: puedes usar return opcion

# 3️⃣ Función tirar_dado()

# Genera un número aleatorio entre 1 y 6

# Devuelve el número

# Tip: usa random.randint(1, 6)

# 4️⃣ Función jugar_partida(dinero_apuesta=0)

# Llama a tirar_dado() para jugador → guarda en jugador

# Llama a tirar_dado() para máquina → guarda en maquina

# Compara los resultados:

# Si jugador > máquina → ganador = “jugador”

# Si máquina > jugador → ganador = “máquina”

# Si iguales → empate

# Calcula dinero de la partida:

# Si apuesta > 0 y jugador gana → dinero = +apuesta

# Si apuesta > 0 y jugador pierde → dinero = -apuesta

# Si empate → dinero = 0

# Devuelve ganador y dinero

# 5️⃣ Función main()

# Inicializa bucle while True:

# Dentro del bucle:

# Llama a mostrar_menu() → guarda opción

# Si opción 1:

# Pide número de partidas

# Inicializa ganadas_jugador y ganadas_maquina

# Para cada partida:

# Llama a jugar_partida()

# Actualiza contadores

# Imprime resultado

# Al final, imprime resumen

# Si opción 2:

# Pide número de partidas y dinero a apostar

# Inicializa contadores y dinero_total = 0

# Para cada partida:

# Llama a jugar_partida(dinero_apuesta)

# Actualiza contadores y dinero_total

# Imprime resultado y total

# Al final, imprime resumen

# Si opción 3:

# break para salir

# 6️⃣ Ejecutar el juego

# Al final del archivo, llama a main()