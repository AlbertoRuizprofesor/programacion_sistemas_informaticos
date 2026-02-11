"""
Almacenar en una lista de 5 elementos las tuplas con el nombre de empleado y su sueldo.

Implementar las funciones:

1) Carga de empleados.

2) Impresión de los empleados y sus sueldos.

3) Nombre del empleado con sueldo mayor.

4) Cantidad de empleados con sueldo menor a 1000.
"""
def cargar_empleados():
    """
    Solicita los datos de 5 empleados (nombre y sueldo)
    y devuelve una lista de tuplas con esa información.
    """
    lista_empleados = []
    for i in range(5):
        nombre_empleado = input("Nombre del empleado: ")
        sueldo_empleado = int(input("Ingrese el sueldo: "))
        lista_empleados.append((nombre_empleado, sueldo_empleado))
    return lista_empleados


def mostrar_empleados(lista_empleados):
    """
    Muestra el nombre y sueldo de cada empleado.
    """
    print("Listado de empleados y sus sueldos:")
    for nombre, sueldo in lista_empleados:
        print(nombre, sueldo)


def empleado_con_mejor_sueldo(lista_empleados):
    """
    Determina qué empleado tiene el sueldo más alto
    y muestra su nombre y sueldo.
    """
    mejor_pagado = lista_empleados[0]
    for empleado in lista_empleados:
        if empleado[1] > mejor_pagado[1]:
            mejor_pagado = empleado
    print("Empleado con mayor sueldo:", mejor_pagado[0],
          "con un sueldo de", mejor_pagado[1])


def contar_sueldos_bajos(lista_empleados):
    """
    Cuenta cuántos empleados ganan menos de 1000.
    """
    cantidad = 0
    for empleado in lista_empleados:
        if empleado[1] < 1000:
            cantidad += 1
    print("Cantidad de empleados con sueldo menor a 1000:", cantidad)


# Bloque principal

empleados_registrados = cargar_empleados()
mostrar_empleados(empleados_registrados)
empleado_con_mejor_sueldo(empleados_registrados)
contar_sueldos_bajos(empleados_registrados)

