edad = int(input("Dime tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    if edad > 12 and edad < 18:
        print("Eres un adolescente")
    else:
        print("Eres un pipiolo")
        