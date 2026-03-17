# Ejercicio 6. Agenda simple
# Implementa una agenda usando un diccionario donde
# la clave sea el nombre y el valor el teléfono.
# Crea un menú para añadir, buscar, modificar y borrar contactos.
# Idea clave: Haz que no se distingan mayúsculas y minúsculas en las búsquedas.

agenda = {} # Recordatorio {}Dicionario, []Lista, ()Tupla

def agregar_contacto(nombre, telefono):
    agenda[nombre.title().strip()] = telefono
    print(f"Contacto '{nombre}' agregado con teléfono '{telefono}'.")

def borrar_contacto(nombre):
    nombre = nombre.title().strip()
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto '{nombre}' borrado.")
    else:
        print(f"Contacto '{nombre}' no encontrado.")

def buscar_contacto(nombre):
    nombre = nombre.title().strip()
    if nombre in agenda:
        print(f"Contacto '{nombre}': {agenda[nombre]}")
    else:
        print(f"Contacto '{nombre}' no encontrado.")

def modificar_contacto(nombre, nuevo_telefono):
    nombre = nombre.title().strip()
    if nombre in agenda:
        agenda[nombre] = nuevo_telefono
        print(f"Contacto '{nombre}' modificado con nuevo teléfono '{nuevo_telefono}'.")
    else:
        print(f"Contacto '{nombre}' no encontrado.")

def mostrar_menu():
    print("\nMenú de Agenda:")
    print("_" * 20)
    print("1. Agregar contacto")
    print("2. Borrar contacto")
    print("3. Buscar contacto")
    print("4. Modificar contacto")
    print("5. Mostrar agenda")
    print("0. Salir")

def mostrar_agenda():
    if not agenda:  # Usamoos not agenda en vez de len(agenda) == 0 o agenda == {}
                    # Es una forma más pythonica de verificar si el diccionario está vacío
        print("La agenda está vacía.")
    else:
        print("\nAgenda de Contactos:")
        print("-" * 20)
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")

# Main loop del programa
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")
    
    if opcion == '1':
        nombre = input("Nombre del contacto: ")
        telefono = input("Teléfono del contacto: ")
        agregar_contacto(nombre, telefono)
    elif opcion == '2':
        nombre = input("Nombre del contacto a borrar: ")
        borrar_contacto(nombre)
    elif opcion == '3':
        nombre = input("Nombre del contacto a buscar: ")
        buscar_contacto(nombre)
    elif opcion == '4':
        nombre = input("Nombre del contacto a modificar: ")
        nuevo_telefono = input("Nuevo teléfono del contacto: ")
        modificar_contacto(nombre, nuevo_telefono)
    elif opcion == '5':
        mostrar_agenda()
    elif opcion == '0':
        print("Saliendo de la agenda. ¡Hasta luego, Bro!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú. Tú puedes hacerlo, Bro!")