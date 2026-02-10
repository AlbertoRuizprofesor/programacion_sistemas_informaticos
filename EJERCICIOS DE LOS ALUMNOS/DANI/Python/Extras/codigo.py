intentos = 3
codigos = ["kali", "parrot", "ubuntu"]

while intentos >= 0:
    intento = input("\nIntroduce el código: ")

    if intento.lower() in codigos:
        match intento.lower():
            case "kali":
                print("Codigo correcto. Tienes acceso al area de hacking\n")
            case "parrot":
                print("Codigo correcto. Tienes acceso al area de los piratas\n")
            case "ubuntu":
                print("Codigo correcto. Tienes acceso al area de victimas\n")
        break
    else:
        intentos = intentos - 1
        if intentos >= 0:
            print("Error, prueba otra vez.")
            print(f"Quedan {intentos} intentos")
        else:
            print("🚨BLOQUEADO🚨")