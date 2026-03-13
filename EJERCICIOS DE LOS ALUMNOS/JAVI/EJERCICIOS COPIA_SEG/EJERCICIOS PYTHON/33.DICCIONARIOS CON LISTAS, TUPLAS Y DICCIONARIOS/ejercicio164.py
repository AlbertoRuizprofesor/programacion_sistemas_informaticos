"""
Confeccionar una agenda. Utilizar un diccionario cuya clave sea la fecha. Permitir almacenar distintas actividades para la misma fecha (se ingresa la hora y la actividad)

Implementar las siguientes funciones:

1) Carga de datos en la agenda.

2) Listado completo de la agenda.

3) Consulta de una fecha.
"""

def cargar_agenda():
    """
    Permite ingresar fechas y, para cada fecha, una lista de actividades.
    Cada actividad contiene:
        - hora (str)
        - descripción (str)
    Devuelve un diccionario donde:
        clave   = fecha (str)
        valor   = lista de tuplas (hora, descripción)
    """
    agenda_completa = {}
    continuar_fechas = "s"

    while continuar_fechas == "s":
        fecha = input("Ingrese la fecha (dd/mm/aa): ")

        actividades_del_dia = []
        continuar_actividades = "s"

        # Cargar actividades para esa fecha
        while continuar_actividades == "s":
            hora = input("Ingrese la hora (hh:mm): ")
            descripcion = input("Ingrese la descripción de la actividad: ")
            actividades_del_dia.append((hora, descripcion))

            continuar_actividades = input("¿Agregar otra actividad para esta fecha? [s/n]: ")

        # Guardar la lista de actividades en la agenda
        agenda_completa[fecha] = actividades_del_dia

        continuar_fechas = input("¿Desea ingresar otra fecha? [s/n]: ")

    return agenda_completa


def mostrar_agenda(agenda_completa):
    """
    Muestra todas las fechas registradas y sus actividades asociadas.
    """
    print("Listado completo de la agenda:")
    for fecha, actividades in agenda_completa.items():
        print("Fecha:", fecha)
        for hora, descripcion in actividades:
            print("  ", hora, "-", descripcion)


def consultar_por_fecha(agenda_completa):
    """
    Permite consultar las actividades de una fecha específica.
    Si la fecha no existe, informa al usuario.
    """
    fecha = input("Ingrese la fecha que desea consultar: ")
    if fecha in agenda_completa:
        for hora, descripcion in agenda_completa[fecha]:
            print(hora, "-", descripcion)
    else:
        print("No hay actividades registradas para esa fecha.")


# Bloque principal

agenda_registrada = cargar_agenda()
mostrar_agenda(agenda_registrada)
consultar_por_fecha(agenda_registrada)
