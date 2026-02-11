# En una empresa se almacenaron los sueldos de 10 personas. Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
# 1) Carga de los sueldos en una lista.
def cargar_sueldos():
    sueldos = []
    for x in range(10):
        sueldo = float(input(f"Dame el sueldo del trabajador número {x+1}: "))
        sueldos.append(sueldo)
    return sueldos

# 2) Impresión de todos los sueldos.
def imprimir(lista):
    print(f"Sueldos: {lista}")

# 3) Cuántos tienen un sueldo superior a $4000.
def superiores(lista):
    superior = 0
    for list in lista:
        if list > 4000:
            superior += 1
    print(f"Cantidad superior a 4.000€: {superior}")

# 4) Retornar el promedio de los sueldos
def promedio(lista):
    suma = 0
    for x in range(len(lista)):
        suma += lista[x]
    prom = suma / 10
    return prom

# 5) Mostrar todos los sueldos que están por debajo del promedio.
def inferior_promedio(lista,promedio):
    inferior = []
    for list in lista:
        if list < promedio:
            inferior.append(list)
    print(f"Sueldos sinferiores a 4.000€: {inferior}")

# -----PROGRAMA PRINCIPAL-----
datos = cargar_sueldos()
imprimir(datos)
superiores(datos)
prom = promedio(datos)
inferior_promedio(datos,prom)