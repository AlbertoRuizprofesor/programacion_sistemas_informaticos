print("Ejercicio 135")
print("")
print("")

# En una empresa se almacenaron los sueldos de 10 personas.
# Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
# 1) Carga de los sueldos en una lista.
# 2) Impresión de todos los sueldos.
# 3) Cuántos tienen un sueldo superior a $4000.
# 4) Retornar el promedio de los sueldos
# 5) Mostrar todos los sueldos que están por debajo del promedio.

def cargar_sueldos():
    sueldos = []
    for n in range(10):
        sueldo = float(input(f"Ingrese el sueldo de la persona {n+1}: "))
        sueldos.append(sueldo)
    return sueldos

def imprimir_sueldos(sueldos):
    print("Lista de sueldos:")
    for sueldo in sueldos:
        print(f"${sueldo:.2f}")

def contar_sueldos_superiores(sueldos, limite=4000):
    contador = 0
    for sueldo in sueldos:
        if sueldo > limite:
            contador += 1
    return contador

def calcular_promedio(sueldos):
    return sum(sueldos) / len(sueldos)

def mostrar_sueldos_por_debajo_promedio(sueldos, promedio):
    print(f"Sueldos por debajo del promedio (${promedio:.2f}):")
    for sueldo in sueldos:
        if sueldo < promedio:
            print(f"${sueldo:.2f}")

# Bloque principal

sueldos = cargar_sueldos()
imprimir_sueldos(sueldos)
cantidad_superiores = contar_sueldos_superiores(sueldos)
print(f"Cantidad de sueldos superiores a $4000: {cantidad_superiores}")
promedio_sueldos = calcular_promedio(sueldos)
print(f"Promedio de sueldos: ${promedio_sueldos:.2f}")
mostrar_sueldos_por_debajo_promedio(sueldos, promedio_sueldos)


print("Fin del programa")

