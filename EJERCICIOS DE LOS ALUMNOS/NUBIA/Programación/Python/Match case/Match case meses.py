mes = input("Introduce un mes del año (enero, febrero, etc.): ").lower()

match mes.lower():
    case "diciembre" | "enero" | "febrero":
        print("El mes introducido pertenece a invierno")
    case "marzo" | "abril" | "mayo":    
        print("El mes introducido pertenece a primavera")
    case "junio" | "julio" | "agosto":
        print("El mes introducido pertenece a verano")
    case "septiembre" | "octubre" | "noviembre":
        print("El mes introducido pertenece a otoño")
    case _:
        print("El mes introducido no es válido")