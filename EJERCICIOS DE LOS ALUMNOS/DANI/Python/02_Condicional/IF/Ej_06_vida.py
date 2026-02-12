edad = int(input("Dime la edad: "))

if edad > -1 and edad <= 120:
    if edad >= 0 and edad < 3:
        print("bebe")
    elif edad >= 3 and edad < 13:
        print("preadolescente")
    elif edad >= 13 and edad < 18:
        print("adolecente")
    elif edad >= 18 and edad < 67:
        print("trabajador")
    elif edad >= 67:
        print("Feliz jubilacion")
else:
    print("Dame una edad en la que este vivo")