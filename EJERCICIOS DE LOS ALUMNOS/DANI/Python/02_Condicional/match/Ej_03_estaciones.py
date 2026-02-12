# Pedir al usuario que le de un valor a la variable
mes = input("Introduce un mes del año: ").lower() # .lower() --> Convierte lo escrito en minúscula

match mes:
    case "enero" | "febrero" | "marzo" :
        print(f"En {mes} es invierno.")
    case "abril" | "mayo" | "junio":
        print(f"En {mes} es primavera.")
    case "julio" | "agosto" | "septiembre":
        print(f"En {mes} es verano.")
    case "octubre" | "noviembre" | "diciembre":
        print(f"En {mes} es otoño.")
    case _:
        print(f"{mes} no es un mes válido.")
