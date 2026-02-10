"""
Confeccionar un programa que almacene en un diccionario como clave el nombre de un contacto y como valor su número telefónico:

1) Carga de contactos y su número telefónico.

2) Pemitir modificar el número telefónico. Se ingresa el nombre del contacto para su búsqueda.

3) Imprimir la lista completa de contactos con sus números telefónicos.
"""

def cargar_contactos():
    # Creamos un diccionario vacío donde guardaremos los contactos
    agenda = {}
    seguir = "s"

    # Mientras el usuario quiera seguir añadiendo contactos
    while seguir == "s":
        nombre = input("Escribe el nombre del contacto: ")
        numero = input("Introduce su número telefónico: ")

        # Guardamos el contacto en el diccionario
        agenda[nombre] = numero

        seguir = input("¿Deseas agregar otro contacto? [s/n]: ")

    return agenda


def actualizar_numero(agenda):
    # Pedimos el nombre del contacto cuyo número queremos cambiar
    nombre = input("Nombre del contacto al que deseas cambiar el número: ")

    # Verificamos si existe en la agenda
    if nombre in agenda:
        nuevo_num = input("Introduce el nuevo número: ")
        agenda[nombre] = nuevo_num
    else:
        print("No se encontró ningún contacto con ese nombre.")


def mostrar_agenda(agenda):
    print("Listado completo de contactos:")
    for nombre in agenda:
        print(nombre, agenda[nombre])


# Programa principal

contactos = cargar_contactos()
actualizar_numero(contactos)
mostrar_agenda(contactos)
