edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    if edad > 12 and edad < 18:
        print("Eres un adolescente insoportable.")
    else:
        print("Eres un niño feliz e insoportable.")