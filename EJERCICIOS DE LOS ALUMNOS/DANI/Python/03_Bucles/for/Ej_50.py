# Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la tabla de multiplicar del mismo (los primeros 12 términos)
# Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36.

num = int(input("Dame un num: "))

if num >= 1 and num <= 10:
    for x in range(13):
        print(f"{num} x {x} = {num*x}")
else:
    print("Tiene que ser un número entre 1 y 10")