#Genera un número aleatorio entre 1 y 100. 
#El usuario debe intentar adivinarlo y el programa indicará si el intento es mayor o menor.

import random

objetivo = random.randint(1, 100)
intentos = 0

while True:
    numero = int(input("Tu intento: "))
    intentos += 1
    
    if numero < objetivo:
        print("Demasiado pequeño")
    elif numero > objetivo:
        print("Demasiado grande")
    else:
        print(f"¡Correcto! Número de intentos: {intentos}")
        break