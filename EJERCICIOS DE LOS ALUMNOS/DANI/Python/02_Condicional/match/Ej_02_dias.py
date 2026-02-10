# Pedir al usuario que le de un valor a la variable
dia = input("Introduce un día de la semana: ").lower() # .lower() --> Convierte lo escrito en minúscula

match dia:
    case "lunes" | "martes" | "miercoles" | "jueves" | "viernes":
        print(f"{dia} es laborable.")
    case "sabado" | "domingo":
        print(f"{dia} es fin de semana")
    case _:
        print(f"{dia} no es válido")