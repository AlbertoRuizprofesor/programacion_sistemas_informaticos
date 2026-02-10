opcion = True

while opcion:
    print("----MENÚ----")
    print("1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n5.Salir")
    eleccion = int(input("Elige una opcion: "))
    
    if eleccion >= 1 and eleccion <=4:
        print("\nAhora introduce los números.")
        num1 = int(input("Num1: "))
        num2 = int(input("Num2: "))

        if eleccion == 1:
            print(f"{num1} + {num2} = {num1+num2}\n")
        elif eleccion == 2:
            print(f"{num1} - {num2} = {num1-num2}\n")
        elif eleccion == 3:
            print(f"{num1} x {num2} = {num1*num2}\n")
        elif eleccion == 4:
            print(f"{num1} / {num2} = {num1/num2}\n")
    elif eleccion == 5:
        print("Cerrando programa")
        opcion = False
    else:
        print("Eso no es una opcion tontito.\n")