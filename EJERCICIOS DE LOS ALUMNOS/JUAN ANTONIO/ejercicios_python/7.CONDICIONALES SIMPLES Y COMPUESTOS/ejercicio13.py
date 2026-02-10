#Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) 
# mostrar un mensaje indicando si el número tiene uno o dos dígitos.
# (Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)


#Introducción de datos
numero = int(input("Introduzca un número positivo de uno o dos digitos entre 1 y 99: "))


#Comparación para comprobar el número de digitos del número
if numero < 10:
    print(f"El número introducido tiene un dígito y es: {numero}")
else:
    print(f"El número introducido tiene dos dígitos y es: {numero}")
