"""
Realizar un programa que lea los lados de n triángulos, e informar:
a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
b) Cantidad de triángulos de cada tipo.

"""
#Contadores para cada tipo de triángulo
equilatero=0
isosceles=0
escaleno=0

#Pedimos cuántos triángulos se van a analizar
n=int(input("Ingrese la cantidad de triángulos:"))

#Repetimos el proceso "n" veces
for f in range(n):
    #Pedimos los tres lados del triángulo
    lado1 = int(input("Ingrese lado 1:"))
    lado2 = int(input("Ingrese lado 2:"))
    lado3 = int(input("Ingrese lado 3:"))

    #Si los tres lados son iguales es equilátero
    if lado1 == lado2 and lado1 == lado3:
        print("Es un triángulo equilatero.")
        equilatero = equilatero + 1
    else:   #Si solo dos son iguales es isósceles
        if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("Es un triángulo isósceles.")
            isosceles = isosceles + 1
        else:   #Si los tres son distintos es escaleno
            print("Es un triángulo escaleno.")
            escaleno = escaleno + 1

#Mostramos los resultados finales
print("Cantidad de triángulos equilateros:", equilatero)

print("Cantidad de triángulos isósceles:", isosceles)

print("Cantidad de triángulos escalenos:", escaleno)
