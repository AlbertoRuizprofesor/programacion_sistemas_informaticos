mes=input("Introduce un mes del año: ")

match mes:
    
    case "enero" | "febrero" | "marzo":
        print("Es un mes de invierno")

    case "abril" | "mayo" | "junio":
        print("Es un mes de primavera")

    case "julio" | "agosto" | "septiembre":
        print("Es un mes de verano")

    case "octubre" | "noviembre" | "diciembre":
        print("Es un mes de otoño")

    case _:
        print("El mes no es válido")
        

    