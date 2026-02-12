#ejercicio

dia=input("Introduce un dia de la semana: ").lower()
match dia:
    case "lunes" | "martes" | "miercoles" | "jueves" | "viernes":
        print("Es un día laboral")
    case "sabado" | "domingo":
        print("Es un fin de semana.")
    case _:
        print("No es u día válido.")