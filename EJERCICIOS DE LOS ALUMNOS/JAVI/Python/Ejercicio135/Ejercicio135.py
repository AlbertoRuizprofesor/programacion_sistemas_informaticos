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
        sueldo = float(input("Introduce el sueldo: "))
        sueldos.append(sueldo)
    return sueldos

def imprimir_sueldos(sueldos):
    print("listado de sueldos")
    for x in range(len(sueldos)):
        print(sueldos[x])

def mayor_4k(sueldos):
    cant = 0
    for x in range (len(sueldos)):
        if sueldos[x] > 4000:
            cant = cant + 1

    print("Sueldos mayores a 4000: ") 

def media_sueldos(sueldos):
    suma = 0
    for x in range(len(sueldos)):
        suma = suma + sueldos[x]
    media = suma//10
    return media

def menores_media(sueldos):
    media=media(sueldos)
    for x in range(len(sueldos)):
        if sueldos[x] < media:
            print(sueldos[x])



