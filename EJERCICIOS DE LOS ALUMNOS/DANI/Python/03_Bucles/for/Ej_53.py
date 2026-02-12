# Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:

neg = 0
pos = 0
mult15 = 0
par = 0

for x in range(10):
    x = x + 1
    num = int(input(f"Dame el {x}º num: "))
    
    # a) La cantidad de valores ingresados negativos.
    if num < 0:
        neg = neg + 1
    
    # b) La cantidad de valores ingresados positivos.
    if num > 0:
        pos = pos + 1
    
    # c) La cantidad de múltiplos de 15.
    if num % 15 == 0:
        mult15 = mult15 + 1
    
    # d) El valor acumulado de los números ingresados que son pares.
    if num % 2 == 0:
        par = par + num

print(f"Negativos: {neg}")
print(f"Positivos: {pos}")
print(f"Múltiplos de 15: {mult15}")
print(f"Pares: {par}")
