# Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
# a) La cantidad de valores ingresados negativos.
# b) La cantidad de valores ingresados positivos.
# c) La cantidad de múltiplos de 15.
# d) El valor acumulado de los números ingresados que son pares.

valor1 = int(input("Ingrese el valor 1: "))
valor2 = int(input("Ingrese el valor 2: "))
valor3 = int(input("Ingrese el valor 3: "))
valor4 = int(input("Ingrese el valor 4: "))
valor5 = int(input("Ingrese el valor 5: "))
valor6 = int(input("Ingrese el valor 6: "))
valor7 = int(input("Ingrese el valor 7: "))
valor8 = int(input("Ingrese el valor 8: "))
valor9 = int(input("Ingrese el valor 9: "))
valor10 = int(input("Ingrese el valor 10: "))

valores = [valor1, valor2, valor3, valor4, valor5, valor6, valor7, valor8, valor9, valor10]

cantidad_negativos = 0
cantidad_positivos = 0
cantidad_multiplos_15 = 0
acumulado_pares = 0

for valor in valores:
    if valor < 0:
        cantidad_negativos += 1
    elif valor > 0:
        cantidad_positivos += 1

    if valor % 15 == 0:
        cantidad_multiplos_15 += 1

    if valor % 2 == 0:
        acumulado_pares += valor

print("Cantidad de valores negativos:", cantidad_negativos)
print("Cantidad de valores positivos:", cantidad_positivos)
print("Cantidad de múltiplos de 15:", cantidad_multiplos_15)
print("Acumulado de números pares:", acumulado_pares)
