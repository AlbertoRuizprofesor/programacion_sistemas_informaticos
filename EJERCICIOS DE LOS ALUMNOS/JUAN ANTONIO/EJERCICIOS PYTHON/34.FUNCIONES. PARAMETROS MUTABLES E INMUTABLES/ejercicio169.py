"""
Crear un diccionario en Python para almacenar los datos de empleados de una empresa. La clave será su número de legajo y en su valor almacenar una lista con el nombre, profesión y sueldo. Desarrollar las siguientes funciones:
1) Carga de datos de empleados.
2) Permitir modificar el sueldo de un empleado. Ingresamos su número de legajo para buscarlo.
3) Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas"

"""

# Función para cargar los datos de varios trabajadores
def registrar_trabajadores():
    plantilla = {}   # Diccionario donde guardaremos los datos
    seguir = "s"

    # Bucle para ingresar tantos trabajadores como se desee
    while seguir == "s":
        codigo = int(input("Introduce el código del trabajador: "))
        nombre = input("Nombre del trabajador: ")
        oficio = input("Profesión del trabajador: ")
        salario = float(input("Salario actual: "))

        # Guardamos la información en el diccionario
        plantilla[codigo] = [nombre, oficio, salario]

        seguir = input("¿Deseas añadir otro trabajador? [s/n]: ")

    return plantilla


# Función para mostrar todos los trabajadores registrados
def mostrar_todos(plantilla):
    print("Listado general de trabajadores:")
    for codigo in plantilla:
        print(codigo, plantilla[codigo][0], plantilla[codigo][1], plantilla[codigo][2])


# Función para actualizar el salario de un trabajador
def actualizar_salario(plantilla):
    codigo = int(input("Introduce el código del trabajador a modificar: "))

    # Verificamos si el código existe
    if codigo in plantilla:
        nuevo_salario = float(input("Nuevo salario: "))
        plantilla[codigo][2] = nuevo_salario
    else:
        print("No se encontró ningún trabajador con ese código.")


# Función para mostrar solo los trabajadores cuyo oficio sea 'analista de sistemas'
def mostrar_analistas(plantilla):
    print("Trabajadores con profesión 'analista de sistemas':")
    for codigo in plantilla:
        if plantilla[codigo][1] == "analista de sistemas":
            print(codigo, plantilla[codigo][0], plantilla[codigo][2])


# Programa principal
empleados = registrar_trabajadores()
mostrar_todos(empleados)
actualizar_salario(empleados)
mostrar_todos(empleados)
mostrar_analistas(empleados)
