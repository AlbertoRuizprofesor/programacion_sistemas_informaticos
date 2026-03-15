import random

opciones = ["piedra", "papel", "tijera"]

print("🪨📄✂️ PIEDRA, PAPEL O TIJERA")
print("Escribe piedra, papel o tijera (0 para salir)\n")

while True:
    jugador = input("Tu elección: ").lower()

    if jugador == "0":
        print("Juego terminado 👋")
        break

    if jugador not in opciones:
        print("❌ Opción no válida")
        continue

    maquina = random.choice(opciones)

    print(f"La máquina eligió: {maquina}")

    if jugador == maquina:
        print("🤝 Empate\n")
    elif (
        (jugador == "piedra" and maquina == "tijera")
        or (jugador == "papel" and maquina == "piedra")
        or (jugador == "tijera" and maquina == "papel")
    ):
        print("🎉 ¡Ganaste!\n")
    else:
        print("💻 Perdiste\n")
