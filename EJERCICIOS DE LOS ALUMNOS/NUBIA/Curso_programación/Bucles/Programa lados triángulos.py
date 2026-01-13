# Realizar un programa que lea los lados de n triángulos, e informar:
# a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
# b) Cantidad de triángulos de cada tipo.

n_triangulos = int(input("¿Cuántos triángulos desea analizar?: "))
contador_equilatero = 0
contador_isosceles = 0 
contador_escaleno = 0

for i in range(n_triangulos):
    n_lados_iguales = int(input("¿Cuántos lados iguales tiene?: "))

    if n_lados_iguales == 3:
        contador_equilatero += 1

    elif n_lados_iguales == 2:
        contador_isosceles += 1
    else:
        contador_escaleno += 1

print(f"Cantidad de triángulos equiláteros: {contador_equilatero}")
print(f"Cantidad de triángulos isósceles: {contador_isosceles}")
print(f"Cantidad de triángulos escalenos: {contador_escaleno}")

