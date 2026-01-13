#Match case

opción = 2

match opción:
    case 1:
        print("Has seleccionado la opción 1")
    case 2:
        print("Has seleccionado la opción 2")
    case 3:
        print("Has seleccionado la opción 3")
    #Para indicar respuesta vacía/por defecto:
    case _:
        print("Opción no válida")