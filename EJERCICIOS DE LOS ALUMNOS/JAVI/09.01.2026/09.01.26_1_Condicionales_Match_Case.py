dia = input("¿Qué día de la semana es?: ").lower()

match dia:
    case "lunes" | "martes" | "miercoles" | "jueves" | "viernes":
        print("Día de diario y toca currar")
    case "sabado" | "domingo":
        print("Por_Fin Finde")
    case _:
        print("Opción no válida")
