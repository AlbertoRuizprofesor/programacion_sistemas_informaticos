#En una empresa se almacenaron los sueldos de 10 personas. Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
#1) Carga de los sueldos en una lista.
#2) Impresión de todos los sueldos.
#3) Cuántos tienen un sueldo superior a $4000.
#4) Retornar el promedio de los sueldos
#5) Mostrar todos los sueldos que están por debajo del promedio.


# ---------------------------------------------------------
# FUNCIÓN: cargar_sueldos
# Solicita 10 sueldos al usuario, los guarda en una lista
# y devuelve esa lista.
# ---------------------------------------------------------
def cargar_sueldos():
    sueldos = []
    for x in range(10):
        su = int(input("Ingrese sueldo:"))
        sueldos.append(su)   # Agregamos cada sueldo a la lista
    return sueldos


# ---------------------------------------------------------
# FUNCIÓN: imprimir_sueldos
# Muestra todos los sueldos almacenados en la lista.
# ---------------------------------------------------------
def imprimir_sueldos(sueldos):
    print("Listado de sueldos")
    for x in range(len(sueldos)):
        print(sueldos[x])


# ---------------------------------------------------------
# FUNCIÓN: sueldos_mayor4000
# Cuenta cuántos empleados ganan más de 4000
# y muestra el resultado.
# ---------------------------------------------------------
def sueldos_mayor4000(sueldos):
    cant = 0
    for x in range(len(sueldos)):
        if sueldos[x] > 4000:   # Si el sueldo supera 4000, lo contamos
            cant = cant + 1
    print("Cantidad de empleados con un sueldo superior a 4000:", cant)


# ---------------------------------------------------------
# FUNCIÓN: promedio
# Calcula el promedio de los 10 sueldos ingresados.
# Usa división entera (//) para no mostrar decimales.
# ---------------------------------------------------------
def promedio(sueldos):
    suma = 0
    for x in range(len(sueldos)):
        suma = suma + sueldos[x]   # Sumamos todos los sueldos
    promedio = suma // 10          # Promedio entero
    return promedio


# ---------------------------------------------------------
# FUNCIÓN: sueldos_bajos
# Muestra el promedio y luego imprime los sueldos
# que están por debajo de ese promedio.
# ---------------------------------------------------------
def sueldos_bajos(sueldos):
    pro = promedio(sueldos)
    print("Sueldo promedio de la empresa:", pro)
    print("Sueldos inferiores al promedio")
    for x in range(len(sueldos)):
        if sueldos[x] < pro:       # Si el sueldo es menor al promedio, lo mostramos
            print(sueldos[x])


# ---------------------------------------------------------
# BLOQUE PRINCIPAL DEL PROGRAMA
# ---------------------------------------------------------

sueldos = cargar_sueldos()      # Cargamos los 10 sueldos
imprimir_sueldos(sueldos)       # Mostramos la lista completa
sueldos_mayor4000(sueldos)      # Contamos cuántos superan 4000
sueldos_bajos(sueldos)          # Mostramos promedio y sueldos bajos



