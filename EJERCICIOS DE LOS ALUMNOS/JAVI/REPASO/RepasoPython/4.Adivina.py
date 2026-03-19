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
        print(f"¡Correcto! Intentos: {intentos}")
        break
