#Se ingresa por teclado un valor entero, 
# mostrar una leyenda que indique si el número es positivo, 
# negativo o nulo (es decir cero)

# Pedimos al usuario que introduzca un número y lo convertimos a entero
numero = int(input("Introduzca un número positivo, negativo o igua a cero: "))

# Primera condición: ¿el número es exactamente cero?
if numero == 0:
    print(f"El número es igual a {numero}")
else:       # Si no es cero, comprobamos si es mayor que cero
    if numero > 0:
        print(f"El número es positivo y es {numero}")
    else:       # Si no es mayor que cero, entonces es negativo
        print(f"El número es negativo y es {numero}")

