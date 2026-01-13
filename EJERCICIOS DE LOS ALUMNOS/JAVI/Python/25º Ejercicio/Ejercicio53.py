"""
Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números ingresados que son pares.
"""

negativos = 0
positivos = 0
mult15 = 0
pares = 0


for i in range(10):
    valor = int(input("Introduce el valor: "))

    if valor < 0:
        negativos = negativos + 1
    else:
        if valor > 0:
            positivos = positivos + 1

    if valor%15 == 0:
        mul15 = mult15 + 1

    if valor%2 == 0:
        pares = pares + valor

print("Cantidad de valores negativos:")
print(negativos)
print("Cantidad de valores positivos:")
print(positivos)
print("Cantidad de valores múltiplos de 15:")
print(mult15)
print("Suma de los valores pares:")
print(pares)


