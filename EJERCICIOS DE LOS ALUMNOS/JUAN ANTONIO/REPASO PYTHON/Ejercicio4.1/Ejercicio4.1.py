# Ejercicio 4.1. Ampliacion: Cuenta cuántos intentos ha necesitado el usuario

import random

numero_secreto = random.randint(1, 100)
intentos = 0

print("He pensado un número entre 1 y 100. ¡Intenta adivinarlo!")

while True:
    intento = int(input("Tu intento: "))
    intentos += 1

    if intento < numero_secreto:
        print("Demasiado bajo.")
    elif intento > numero_secreto:
        print("Demasiado alto.")
    else:
        print(f"🎉 ¡Correcto! El número era {numero_secreto}.")
        print(f"Lo has adivinado en {intentos} intentos.")
        break
