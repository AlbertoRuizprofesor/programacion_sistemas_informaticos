#Ejercicio 14:Realizar un programa que lea los lados de n triángulos, e informar:
#a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
#b) Cantidad de triángulos de cada tipo.

n=int(input("Ingrese la cantidad de triangulos: "))

cant1=0
cant2=0
cant3=0

for i in range(n):
    lado1=int(input("Ingrese lado 1: "))
    lado2=int(input("Ingrese lado 2: "))
    lado3=int(input("ingrese lado 3: "))
    if lado1==lado2 and lado2==lado3 and lado3==lado1:
        print("Es un triángulo equilatero.")
        cant1=cant1+1
    elif lado1==lado2 or lado1==lado3 or lado2==lado3:
        print("Es un triángulo isosceles.")
        cant2=cant2+1
    else:
        print("es un triángulo escaleno.")
        cant3=cant3+1
        
print(f"Cantidad de triángulos equilateros {cant1}")
print(f"Cantidad de triángulos isosceles {cant2}")
print(f"Cantidad de triángulos escalenos {cant3}")

  