

# Confeccionar un programa que genere un número aleatorio entre 1 y 100 y no se muestre.

import random

intentos=0
aleatorio=random.randint(1,100) 
elegido=-1 

print("Intenta adivinar el numero que pense entre 1 y 100")
while (elegido!=aleatorio): 

    elegido=int(input("¿Qué número eliges?: "))

    if aleatorio>elegido:
        print("Mi número es mayor al introducido")
    else:
        if aleatorio<elegido:
            print("Mi número es menor al introducido")
    intentos=intentos+1

print("Ganaste en",intentos,"intentos")