''' 
Genera un número aleatorio entre 1 y 100. 
El usuario debe intentar adivinarlo y el programa indicará si el intento es mayor o menor. 
Idea clave: Cuenta cuántos intentos ha necesitado el usuario. 
'''
import random

numero = random.randint(1,10)
intentos = 0

while True:
    try:
        respuestaUsuario = int(input("Indica el número que crees que es: "))

        if respuestaUsuario == numero:
            print(f"Has adivinado el número {numero} después de {intentos} intentos")
            break

        elif respuestaUsuario > numero:
            print(f"El número es menor que {respuestaUsuario}")
            intentos += 1
            
        else:
            print(f"El número es mayor que {respuestaUsuario}")
            intentos += 1
            
    except ValueError:
                print("Indica un número válido (un número entero)")

