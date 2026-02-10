# Realizar un programa que lea los lados de n triángulos, e informar:

cant = int(input("¿Cuántos triángulos? "))
equilatero = 0
isosceles = 0
escaleno = 0

for x in range(cant):
    x = x + 1
    print(f"\nTriángulo num {x}:")
    a = int(input("Lado a: "))
    b = int(input("Lado b: "))
    c = int(input("Lado c: "))
    
    # a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
    if a == b and a == c:
        print("El triángulo es equilatero.")
        equilatero = equilatero + 1
    elif a == b or a == c or b == c:
        print("El triángulo es isósceles.")
        isosceles = isosceles + 1
    else:
        print("El triángulo es escaleno.")
        escaleno = escaleno + 1

# b) Cantidad de triángulos de cada tipo.
print(f"\nTriángulo equilatero: {equilatero}")
print(f"Triángulo isósceles: {isosceles}")
print(f"Triángulo escaleno: {escaleno}")