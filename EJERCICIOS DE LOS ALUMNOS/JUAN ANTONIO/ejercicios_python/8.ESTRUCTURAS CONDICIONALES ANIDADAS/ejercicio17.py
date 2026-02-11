#Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y 
# muestre un mensaje indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si el número de cifras es mayor.


# Pedimos al usuario que introduzca un número positivo de 1 a 3 dígitos
numero = int(input("Introduzca un número de 1 a 3 digitos positivo: "))

# Primera condición: si el número es menor que 10, tiene un solo dígito
if numero < 10:
    print(f"El número tiene un dígito y es {numero}")
else:       # Si no es de un dígito, comprobamos si es menor que 100
    if numero < 100:
        print(f"El número tiene dos dígitos y es {numero}")
    else:   # Si tampoco es menor que 100, comprobamos si es menor que 1000
        if numero < 1000:
            print(f"El número tiene tres dígitos y es {numero}")
        else:      # Si no cumple ninguna condición anterior, el número no es válido
            print(f"'ERROR' el número es de cifras es incorrecto, usted introdujo {numero}")