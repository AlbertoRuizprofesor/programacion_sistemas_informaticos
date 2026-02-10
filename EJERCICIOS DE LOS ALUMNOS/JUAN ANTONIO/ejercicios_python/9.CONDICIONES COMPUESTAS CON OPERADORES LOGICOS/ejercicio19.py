#Confeccionar un programa que lea por teclado tres números enteros distintos y nos muestre el mayor.


# Pedimos al usuario que ingrese los valores
num1=int(input("Ingrese primer valor:"))
num2=int(input("Ingrese segundo valor:"))
num3=int(input("Ingrese tercer valor:"))

#Indicamos que vamos a mostrar el mayor de los tres números
print("El mayor de los tres valores es")

#Primera comparación: 
#Si num1 es mayor que num2 Y mayor que num3, entonces num1 es el mayor
if num1>num2 and num1>num3:
    print(num1)
else:   #Si num1 no es el mayor, comprobamos si num2 es mayor que num3
    if num2>num3:
        print(num2)
    else:   #Si ninguna de las anteriores se cumple, el mayor es num3
        print(num3)