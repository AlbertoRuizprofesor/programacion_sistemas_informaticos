#Se cargan por teclado tres números distintos. 
# Mostrar por pantalla el mayor de ellos.


#Pedimos al usuario que introduzca los numeros y los convertimos a enteros
num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))
num3 = int(input("Introduzca el tercer número: "))

#Primera comparación: ¿num1 es mayor que num2?
if num1 > num2:
    if num1 > num3:     #Si num1 también es mayor que num3, entonces num1 es el mayor de todos     
        print(f"El número {num1} es el número mayor")
    else:               #Si num3 es mayor que num1, entonces num3 es el mayor
        print(f"El número {num3} es el número mayor")
else:
    if num2 > num3:     #Si num1 NO es mayor que num2, comparemos num2 con num3. Si num2 es mayor que num3, num2 es el mayor
        print(f"El número {num2} es el número mayor")
    else:               #Si num3 es mayor que num2, num3 es el mayor
        print(f"El número {num3} es el número mayor")
           