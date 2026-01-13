print("Menú:")
print("1. Saludar")
print("2. Decir la hora")
print("3. Salir")

opcion = input("Elige una opción: ")

match opcion:
    case "1":
        print("¡Hola! ¿Cómo estás?")
    case "2":
        print("Son las 10 en punto... según mi imaginación.")
    case "3":
        print("Hasta luego :)")
    case _:
        print("No te he entendido.")