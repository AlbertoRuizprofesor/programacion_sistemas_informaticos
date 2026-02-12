"""

- Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista con el nombre del empleado junto a sus últimos tres sueldos (estos tres valores en una tupla) El programa debe tener las siguientes funciones:
1) Carga de los nombres de empleados y sus últimos tres sueldos.
2) Imprimir el monto total cobrado por cada empleado.
3) Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000 en los últimos tres meses.
Tener en cuenta que la estructura de datos si se carga por asignación debería ser similar a:
    

    empleados = [["juan",(2000,3000,4233)] , ["ana",(3444,1000,5333)] ,  etc.   ]
    
"""

# -----------------------------------------
# Función: cargar_datos_empleados
# Solicita el nombre y los tres sueldos de 5 empleados.
# Cada empleado se guarda como:
#   [nombre, (sueldo1, sueldo2, sueldo3)]
# Devuelve una lista con todos los empleados.
# -----------------------------------------

def cargar_datos_empleados():
    lista_empleados = []

    for i in range(5):
        nombre = input("Ingrese el nombre del empleado: ")
        sueldo1 = int(input("Primer sueldo: "))
        sueldo2 = int(input("Segundo sueldo: "))
        sueldo3 = int(input("Tercer sueldo: "))

        # Guardamos nombre + tupla de sueldos
        lista_empleados.append([nombre, (sueldo1, sueldo2, sueldo3)])

    return lista_empleados


# -----------------------------------------
# Función: mostrar_ganancias
# Recibe la lista de empleados y calcula
# el total ganado por cada uno en los últimos 3 meses.
# -----------------------------------------

def mostrar_ganancias(empleados):
    print("Monto total ganado por cada empleado en los últimos tres meses:")

    for i in range(5):
        # Sumamos los tres sueldos almacenados en la tupla
        total = empleados[i][1][0] + empleados[i][1][1] + empleados[i][1][2]
        print(empleados[i][0], total)


# -----------------------------------------
# Función: mostrar_superiores_10000
# Imprime solo los empleados cuyo total de ingresos
# supera los 10.000 en los últimos 3 meses.
# -----------------------------------------

def mostrar_superiores_10000(empleados):
    print("Empleados con ingresos superiores a 10000 en los últimos 3 meses:")

    for i in range(5):
        total = empleados[i][1][0] + empleados[i][1][1] + empleados[i][1][2]

        if total > 10000:
            print(empleados[i][0], total)


# -----------------------------------------
# Bloque principal del programa
# -----------------------------------------

empleados = cargar_datos_empleados()
mostrar_ganancias(empleados)
mostrar_superiores_10000(empleados)
