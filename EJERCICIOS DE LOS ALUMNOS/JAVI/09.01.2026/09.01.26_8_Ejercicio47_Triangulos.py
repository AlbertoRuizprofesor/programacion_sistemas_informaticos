cantidad = 0
base = 0
h = 0
superficie = 0

n = int(input("Cuantos valores ingresará: "))

for f in range(n):
    base = int(input(f"Ingrese el valor base para el triangulo {f}: "))
    h = int(input(f"Ingrese el valor altura para el triangulo {f}: "))
    superficie = base + h / 2
    print(
        f"El triangulo {f} de base {base} y altura {h} tiene una superficie de {superficie}"
    )

    if superficie >= 12:
        cantidad = cantidad + 1

print(f"La cantidad de triangulos con superficie mayor de 12 son: {cantidad}")
