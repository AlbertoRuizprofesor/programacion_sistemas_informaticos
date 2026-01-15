# Poner """ para no tener que estar poniendo # en cada comentario
""" 
En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos
5) Mostrar todos los sueldos que están por debajo del promedio.
"""

def cargar_sueldos():
    sueldos = []
    for x in range(10):
        sueldo = int(input(f"Ingrese sueldo {x+1}: "))
        sueldos.append(sueldo)
    return sueldos

def imprimir_sueldos(sueldos):
    print("Listado de sueldos: ")
    for x in range(len(sueldos)):
        print(sueldos[x])

def sueldos_mayor4000(sueldos):
    cantidad = 0
    for x in range(len(sueldos)):
        if sueldos[x] > 4000:
            cantidad = cantidad+1
    print(f"Cantidad de empleados con un sueldo superior a 4000: {cantidad}")

def promedio(sueldos):
    suma = 0
    for x in range(len(sueldos)):
        suma = suma + sueldos[x]
    promedio = suma/ len(sueldos)
    return promedio

def sueldos_bajos(sueldos):
    pro = promedio(sueldos)
    print(f"Sueldo promedio de la empresa: {pro}")
    print("Sueldos inferiores al promedio")
    for x in range(len(sueldos)):
        if sueldos[x]<pro:
            print(sueldos[x])


# bloque principal
sueldos = cargar_sueldos()
imprimir_sueldos(sueldos)
sueldos_mayor4000(sueldos)
sueldos_bajos(sueldos)