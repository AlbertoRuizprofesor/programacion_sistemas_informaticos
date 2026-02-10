option = 1
elegir = 1

while option:

    if elegir == 1:
        num1 = float(input("Introduce un numero 1: "))
        num2 = float(input("introduce un numero 2: "))
        elegir = 0

    print("1-Sumar  2-Restar  3-Multiplicar  4-Dividir   5-Nuevas Cifras   0-Salir")
    n = int(input("Elige, Bro: "))

    if n == 1:
        print("Has elegido Sumar, Bro")
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    elif n == 2:
        print("Has elegido Restar, Bro")
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
    elif n == 3:
        print("Has elegido Multiplicarr, Bro")
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")
    elif n == 4:
        print("Has elegido Dividir, Bro")
        resultado = num1 / num2
        print(f"El resultado de la División es: {resultado}")
    elif n == 5:
        print("Has elegido elegir nuevas cifras, Bro")
        elegir = 1
    elif n == 0:
        print("Has elegido Salir, Bro")
        option = 0
