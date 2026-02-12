dia=input("introduce un dia de la semana: ").lower()

match dia:
    case "lunes" | "martes" | "miercoles" | "jueves" | "viernes":
        print("es un dia laborable")
    case "sabado" |"domingo":
        print("es fin de semana")
    case _:
        print("no es un dia valido")