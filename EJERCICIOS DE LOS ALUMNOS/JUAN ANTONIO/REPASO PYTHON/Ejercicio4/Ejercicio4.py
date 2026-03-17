# Ejercicio 4. Adivina el número
import random

numero_secreto = random.randint(1, 100)

print("He pensado un número entre 1 y 100. ¡Intenta adivinarlo!")

intento = int(input("Tu intento: "))

while intento != numero_secreto:
    if intento < numero_secreto:
        print("Demasiado bajo.")
    else:
        print("Demasiado alto.")
    
    intento = int(input("Intenta de nuevo: "))

print("¡Correcto! El número era", numero_secreto)
