cantidad = 0
valor = 0
total = 0

for f in range(10):
    valor = int(input(f"Ingrese el valor del numero {f}: "))
    if f >= 5:
        total = total + valor

print(f"La suma de los 5 últimos valores es: {total}")
