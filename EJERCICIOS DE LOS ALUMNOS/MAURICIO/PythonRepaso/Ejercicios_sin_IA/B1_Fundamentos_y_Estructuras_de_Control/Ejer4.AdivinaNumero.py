# Ejercicio 4. Adivina el número
# Genera un número aleatorio entre 1 y 100.
# El usuario debe intentar adivinarlo y el programa
# indicará si el intento es mayor o menor.
# Ampliación: Cuenta cuántos intentos ha necesitado el usuario.
import random

numeroMaquina = random.randint(1, 100)
intentos = 0

while True:

    intentos += 1
    numeroUsuario = int(input(f"{intentos}º intento. Introcduce tu número, bro: "))

    if numeroUsuario == numeroMaquina:
        print("¡¡¡HAS ACERTADO, BRO!!!")
        print(f"Solo has necesitado {intentos} intentos")
        break
    elif numeroUsuario < numeroMaquina:
        print("Te quedaste corto el número es más alto")
    elif numeroUsuario > numeroMaquina:
        print("Te has pasado, bro. Buscamos un número más bajo")

print("Fin de Ejecución del Código")
