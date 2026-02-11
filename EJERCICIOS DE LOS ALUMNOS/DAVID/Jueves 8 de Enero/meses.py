print("Meses del año")
print("Escribe un número del 1 al 12:")

mes = input("Número: ")

match mes:
    case "1":
        print("Enero")
    case "2":
        print("Febrero")
    case "3":
        print("Marzo: Es primavera")
    case "4":
        print("Abril")
    case "5":
        print("Mayo")
    case "6":
        print("Junio: Es verano")
    case "7":
        print("Julio")
    case "8":
        print("Agosto")
    case "9":
        print("Septiembre")
    case "10":
        print("Octubre: Es otoño")
    case "11":
        print("Noviembre")
    case "12":
        print("Diciembre: Es Navidad")
    case _:
        print("Número no válido. Debe estar entre 1 y 12.")