mes=input("introduce un mes de año: ").lower()

match mes:
    case "enero" | "febrero" | "marzo":
        print("invierno")
    case "abril" |"mayo" | "junio":
        print("primavera")
    case "julio" | "agosto" | "septiembre":
        print("verano")
    case "octubre" |"noviembre" | "diciembre":
        print("otoño")
    case _:
        print("no es un mes valido")