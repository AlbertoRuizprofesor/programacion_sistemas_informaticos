# Programa: ejercicio46.py

n = int(input("Indica cuántos números enteros quiere introducir: "))
cantidad = 0

for x in range(n):
    valor = int(input("Introduzca un número entero: "))
    
    if valor >= 1000:
        cantidad = cantidad + 1

print(f"Ha introducido {cantidad} números mayores o iguales a 1000.")