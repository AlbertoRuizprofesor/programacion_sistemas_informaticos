print("Días de la semana")
print("Escribe un número del 1 al 7:")

dia = input("Número: ")

match dia:
    case "1":
        print("Hoy es lunes.")
    case "2":
        print("Hoy es martes.")
    case "3":
        print("Hoy es miércoles.")
    case "4":
        print("Hoy es jueves.")
    case "5":
        print("Hoy es viernes.")
    case "6":
        print("Hoy es sábado.")
    case "7":
        print("Hoy es domingo.")
    case _:
        print("Número no válido. Debe estar entre 1 y 7.")
