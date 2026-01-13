print("Ejercicio 118")
print("")
print("")

#definición de funciones

def perimetro(lado):
    peri=lado*4
    print("El perimetro del cuadrado es: ", peri)

def area(lado):
    ar=lado*lado
    print("El area del cuadrado es: ", ar)

def operacion():
    lado=int(input("Ingrese la medida del lado del cuadrado: "))
    opcion=input("Ingrese 'P' para calcular el perimetro o 'A' para calcular el area: ").upper()
    if opcion == 'P':
        perimetro(lado)
    elif opcion == 'A':
        area(lado)

#programa principal

operacion()
