from math import sqrt, pow
from random import randint

# Bloque Principal

valor = int(input("Ingrese un valor entero positivo: "))
if valor < 0:
    print("El valor debe ser positivo")
else:
    raiz = sqrt(valor)
    print("La raiz cuadrada de", valor, "es:", raiz)

    aleatorio = randint(1, 10)
    print("Un numero aleatorio entre 1 y 10 es:", aleatorio)

    potencia = pow(valor, aleatorio)
    print(f"El valor de {valor} elevado a el aleatorio {aleatorio} es: {potencia}")
