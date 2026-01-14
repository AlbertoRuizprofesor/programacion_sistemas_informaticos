import random

def saludo():
    return print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    
def juego_ppt():
    opciones = ["piedra", "papel", "tijeras"]
    usuario_eleccion = input("Elige piedra, papel o tijeras: ").lower()
    computadora_eleccion = random.choice(opciones)

    print(f"Tú elegiste: {usuario_eleccion}")
    print(f"La computadora eligió: {computadora_eleccion}")

    if usuario_eleccion == computadora_eleccion:
        print("¡Es un empate!")
    elif (usuario_eleccion == "piedra" and computadora_eleccion == "tijeras") or \
         (usuario_eleccion == "papel" and computadora_eleccion == "piedra") or \
         (usuario_eleccion == "tijeras" and computadora_eleccion == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

# Ejecutar el juego
saludo()
juego_ppt()

# Para jugar de nuevo,  usar un bucle while (como se muestra en tutoriales):
while True:
    juego_ppt()
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (sí/no): ").lower()
    if jugar_de_nuevo == "No" or "no":
        print("¡Gracias por jugar!")
        break
    
    