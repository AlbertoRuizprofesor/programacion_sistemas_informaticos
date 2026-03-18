# Ejercicio 6. Agenda simple
contactos = {}

while True:
    print("1. Añadir  2. Buscar  3. Modificar  4. Borrar  5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        persona = input("Introduce el nombre: ").strip().lower()
        numero = input("Introduce el número: ")
        contactos[persona] = numero

    elif opcion == "2":
        persona = input("Nombre a buscar: ").strip().lower()
        print(contactos.get(persona, "Contacto no encontrado"))

    elif opcion == "3":
        persona = input("Nombre a modificar: ").strip().lower()
        if persona in contactos:
            contactos[persona] = input("Nuevo número: ")
        else:
            print("Contacto no encontrado")

    elif opcion == "4":
        persona = input("Nombre a borrar: ").strip().lower()
        if persona in contactos:
            del contactos[persona]
        else:
            print("Contacto no encontrado")

    elif opcion == "5":
        print("Saliendo de la agenda...")
        break

    else:
        print("Opción inválida")
