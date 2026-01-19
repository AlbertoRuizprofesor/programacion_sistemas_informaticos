from menu import menu

persona = menu()

if persona:
    print("\nDatos de la persona creada:")
    persona.mostrar_datos()
