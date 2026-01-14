import random

# Definimos las opciones posibles
opciones = ["piedra", "papel", "tijera"]

print("--- ¡Bienvenido al juego de Piedra, Papel o Tijera! ---")

# 1. El usuario elige
usuario = input("Elige (piedra, papel o tijera): ").lower()

# 2. La computadora elige al azar
computadora = random.choice(opciones)

print(f"\nTú elegiste: {usuario}")
print(f"La computadora eligió: {computadora}")
print("-" * 20)

# 3. Lógica para determinar el ganador
if usuario == computadora:
    print("¡Es un empate!")
    
elif (usuario == "piedra" and computadora == "tijera") or \
     (usuario == "papel" and computadora == "piedra") or \
     (usuario == "tijera" and computadora == "papel"):
    print("¡Ganaste! 🎉")
    
else:
    print("Perdiste... Inténtalo de nuevo. 🤖")