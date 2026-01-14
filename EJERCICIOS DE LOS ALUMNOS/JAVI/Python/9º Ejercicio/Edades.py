"""Ejercicio
Me pide tres numeros y me tiene que decir el programa cual de los tres numeros, es el mayor

Resultado
numero1: 10
numero2: 4
numero3: 7

el numero mayor es 10"""

num1 = int(input("Introduce el número 1: "))
num2 = int(input("Introduce el número 2: "))
num3 = int(input("Introduce el número 3: "))

if num1 > num2 and num1 > num3:
    print ("El mayor es: " , num1)

if num2 > num1 and num2 > num3:
    print ("El mayor es: " , num2)

if num3 > num2 and num3 > num1:
    print ("El mayor es: " , num3)

    
    


