cantidad = 0
n = int(input("Cuantos Triangulos ingresará: "))
equilatero = 0
isosceles = 0
escaleno = 0

for f in range(n):
    lado1 = int(input(f"Ingrese el lado 1 del triangulo {f}: "))
    lado2 = int(input(f"Ingrese el lado 2 del triangulo {f}: "))
    lado3 = int(input(f"Ingrese el lado 3 del triangulo {f}: "))
    if lado1 == lado2 and lado2 == lado3:
        equilatero = equilatero + 1
        print("Es un triangulo EQUILATERO my friend")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        isosceles = isosceles + 1
        print("Es un triangulo ISOSCELES my friend")
    else:
        escaleno = escaleno + 1
        print("Es un triangulo ESCALENO my friend")

print(f"Equilateros hay : {equilatero}")
print(f"Isosceles hay : {isosceles}")
print(f"escaleno hay : {escaleno}")
