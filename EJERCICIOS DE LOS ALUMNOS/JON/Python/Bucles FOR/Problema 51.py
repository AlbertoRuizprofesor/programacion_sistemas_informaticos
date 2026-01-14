print("Problema 51")
print("")
print("")

n=int(input("Introduce el número de triángulos: "))
equilatero=0
isosceles=0
escaleno=0
for i in range(n):
    lado1=int(input("Introduce el lado 1 del triángulo: "))
    lado2=int(input("Introduce el lado 2 del triángulo: "))
    lado3=int(input("Introduce el lado 3 del triángulo: "))
    if lado1==lado2 and lado2==lado3:
        print("El triángulo es equilátero")
    elif lado1==lado2 or lado2==lado3 or lado1==lado3:
        print("El triángulo es isósceles")
    else:
        print("El triángulo es escaleno")
print("El número de triángulos equilateros es: ", equilatero)
print("El número de triángulos isósceles es: ", isosceles)
print("El número de triángulos escalenos es: ", escaleno)




              