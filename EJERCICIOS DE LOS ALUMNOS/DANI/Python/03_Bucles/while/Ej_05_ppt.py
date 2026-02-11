# Crearemos el juego de piedra, papel o tijera

# Importamos random
import random
boolean = True
persona = 0
maquina = 0
empates = 0

while boolean:
    print("----MENÚ----")
    print("1.jugar\n2.salir")
    eleccion = int(input("Elige una opcion: "))
    
    if eleccion == 1:
        print("\nElije una opción para jugar siendo:\n1.Papel.\n2.Tijera.\n3.Piedra.")
        # Pedimos que elija el usuario una opción:
        opcion=int(input("Elije una opción:"))
        num=random.randint(1, 3)

        if opcion <= 3 and opcion >= 1:
            if opcion == 1 and num == 2:
                print("-------\nMáquina: Tijera\nTú: Papel\nHas perdido.\n")
                maquina += 1
            elif opcion == 1 and num == 3:
                print("-------\nMáquina: Piedra\nTú: Papel\nHas ganado.\n")
                persona += 1
            elif opcion == 2 and num == 1:
                print("-------\nMáquina: Papel\nTú: Tijera\nHas ganado.\n")
                persona += 1
            elif opcion == 2 and num == 3:
                print("-------\nMáquina: Piedra\nTú: Tijera\nHas perdido.\n")
                maquina += 1
            elif opcion == 3 and num == 1:
                print("-------\nMáquina: Papel\nTú: Piedra\nHas perdido.\n")
                maquina += 1
            elif opcion == 3 and num == 2:
                print("-------\nMáquina: Tijera\nTú: Piedra\nHas ganado.\n")
                persona += 1
            else:
                print("Habéis seleccionado la misma opción.\n")
                empates += 1
        else:
            print("Esa opción no está disponible.\n")
    elif eleccion == 2:
        print("Cerrando programa")
        boolean = False
    else:
        print("Eso no es una opcion tontito.\n")

# Ver resultados
print(f"\nMáquina: {maquina}")
print(f"Persona: {persona}")
print(f"Empates: {empates}")

# Decir ganador
if maquina > persona:
    print("La máquina gana.")
elif maquina < persona:
    print("Has ganado")
else:
    print("Claro empate.")