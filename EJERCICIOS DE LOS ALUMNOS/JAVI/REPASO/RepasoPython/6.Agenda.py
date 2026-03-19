agenda = {}

while True:
    print("1. Añadir  2. Buscar  3. Modificar  4. Borrar  5. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        nombre = input("Nombre: ").strip().lower()
        telefono = input("Teléfono: ")
        agenda[nombre] = telefono
    elif opcion == "2":
        nombre = input("Nombre a buscar: ").strip().lower()
        print(agenda.get(nombre, "No encontrado"))
    elif opcion == "3":
        nombre = input("Nombre a modificar: ").strip().lower()
        if nombre in agenda:
            agenda[nombre] = input("Nuevo teléfono: ")
        else:
            print("No encontrado")
    elif opcion == "4":
        nombre = input("Nombre a borrar: ").strip().lower()
        if nombre in agenda:
            del agenda[nombre]
        else:
            print("No encontrado")
    elif opcion == "5":
        break
    else:
        print("Opción no válida")
