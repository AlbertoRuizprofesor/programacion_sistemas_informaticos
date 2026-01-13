# Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.
sum = 0

for x in range(10):
    x = x + 1
    num = int(input(f"Dame el {x}º num: "))
    
    if x > 5:
        sum = sum + num

print(f"La suma de los últimos 5 números es {sum}")