"""

Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea el número de documento del alumno. Como valor almacenar una lista con componentes de tipo tupla donde almacenamos nombre de materia y su nota. Crear las siguientes funciones:
1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas)
2) Listado de todos los alumnos con sus notas
3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.
"""

def cargar_alumnos():
    """
    Carga los datos de 3 alumnos.
    Para cada alumno se pide:
        - DNI
        - Lista de materias cursadas con su nota
    Devuelve un diccionario donde:
        clave = DNI del alumno
        valor = lista de tuplas (materia, nota)
    """
    registro_alumnos = {}

    for i in range(3):
        dni = int(input("Ingrese el número de DNI: "))
        materias_cursadas = []
        continuar = "s"

        # Cargar materias y notas del alumno
        while continuar == "s":
            materia = input("Ingrese el nombre de la materia: ")
            nota = int(input("Ingrese la nota: "))
            materias_cursadas.append((materia, nota))

            continuar = input("¿Desea cargar otra materia para este alumno? [s/n]: ")

        registro_alumnos[dni] = materias_cursadas

    return registro_alumnos


def mostrar_alumnos(registro_alumnos):
    """
    Muestra todos los alumnos cargados con sus materias y notas.
    """
    for dni, materias in registro_alumnos.items():
        print("DNI del alumno:", dni)
        print("Materias que cursa y sus notas:")
        for materia, nota in materias:
            print("  ", materia, "-", nota)
        print()  # Separador visual


def consultar_notas_por_dni(registro_alumnos):
    """
    Permite consultar las materias y notas de un alumno
    ingresando su DNI.
    """
    dni = int(input("Ingrese el DNI a consultar: "))

    if dni in registro_alumnos:
        print("Materias y notas del alumno", dni)
        for materia, nota in registro_alumnos[dni]:
            print("  ", materia, "-", nota)
    else:
        print("No existe un alumno con ese DNI.")


# Bloque principal

alumnos_registrados = cargar_alumnos()
mostrar_alumnos(alumnos_registrados)
consultar_notas_por_dni(alumnos_registrados)
