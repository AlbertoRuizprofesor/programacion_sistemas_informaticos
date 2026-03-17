edad = int(input("Cual es tu edad: "))
if edad < 0 or edad >130:
    print("Error de la edad")

elif edad <12:
    print(f"Eres un niño de {edad} años.")
    
elif edad < 16:
    print(f"Eres un adolescente de {edad} años.")
elif edad < 18:
    print(f"Eres un menor de {edad} años.")
elif edad < 65:
    print(f"Eres un trabajador de {edad} años.")
elif edad <= 130:
    print("Eres un jubilado si o si")
