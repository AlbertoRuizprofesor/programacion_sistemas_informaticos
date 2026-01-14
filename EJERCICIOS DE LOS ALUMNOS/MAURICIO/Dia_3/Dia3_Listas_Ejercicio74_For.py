nombres = ["juan", "ana", "marcos", "carlos", "luis"]
cantidad = 0

# Forma 1

for n in range(len(nombres)):
    if len(nombres[n]) >= 5:
        cantidad += 1

print(f"Todos los nombres son: {nombres}")
print(f"Cantidad de nombres con 5 o mas caracteres: {cantidad}")

# Forma 2
cantidad = 0
for n in nombres:
    if len(n) >= 5:
        cantidad += 1

print(f"Todos los nombres son: {nombres}")
print(f"Cantidad de nombres con 5 o mas caracteres: {cantidad}")
