"""
Crear un diccionario en Python que defina como clave el número de documento de una persona y como valor un string con su nombre. Desarrollar las siguientes funciones:
1) Cargar por teclado los datos de 4 personas.
2) Listado completo del diccionario.
3) Consulta del nombre de una persona ingresando su número de documento.
"""

def cargar_personas():
    """
    Solicita al usuario el número de documento y el nombre
    de 4 personas, y los almacena en un diccionario donde:
        - clave: número de documento (int)
        - valor: nombre de la persona (str)
    Devuelve el diccionario completo.
    """
    registro_personas = {}
    for i in range(4):
        dni = int(input("Ingrese el número de documento: "))
        nombre = input("Ingrese el nombre: ")
        registro_personas[dni] = nombre
    return registro_personas


def mostrar_personas(registro_personas):
    """
    Muestra todas las personas almacenadas en el diccionario
    junto con su número de documento.
    """
    print("Listado completo del diccionario:")
    for dni, nombre in registro_personas.items():
        print(dni, nombre)


def consultar_por_dni(registro_personas):
    """
    Permite consultar el nombre asociado a un número de documento.
    Si el DNI no existe en el diccionario, informa al usuario.
    """
    dni_consulta = int(input("Ingrese el número de documento a consultar: "))
    if dni_consulta in registro_personas:
        print("Nombre de la persona:", registro_personas[dni_consulta])
    else:
        print("No existe una persona con ese número de documento.")


# Bloque principal

personas_registradas = cargar_personas()
mostrar_personas(personas_registradas)
consultar_por_dni(personas_registradas)
