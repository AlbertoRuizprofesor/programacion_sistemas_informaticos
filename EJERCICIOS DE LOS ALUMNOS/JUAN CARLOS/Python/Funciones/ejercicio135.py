"""
En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos
5) Mostrar todos los sueldos que están por debajo del promedio.
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

def entradaSueldos(numeroSueldos):
    listaSueldos = []
    for cnt in range(numeroSueldos):
        sueldo = float(input(f"Introduce el sueldo {cnt + 1}: "))
        listaSueldos.append(sueldo)
    return listaSueldos

def imprimirSueldos(lista):
    print("Todos los sueldos:")
    for cnt in lista:
        print(cnt)

def contarSuperiores4000(lista):
    contador = 0
    for cnt in lista:
        if cnt > 4000:
            contador += 1
    return contador

def calcularPromedio(lista):
    suma = 0
    for cnt in lista:
        suma += cnt
    return suma / len(lista)

def mostrarDebajoPromedio(lista, promedio):
    print("Sueldos por debajo del promedio:")
    for cnt in lista:
        if cnt < promedio:
            print(cnt)


#Main
listaSueldos = entradaSueldos(10)
mensaje("1. Carga completada")

mensaje("2. Todos los sueldos")
imprimirSueldos(listaSueldos)

superiores = contarSuperiores4000(listaSueldos)
mensaje("3. Superiores a $4000")
print(f"Cantidad: {superiores}")

promedio = calcularPromedio(listaSueldos)
mensaje("4. Promedio")
print(f"Promedio: {promedio:.2f}")

mensaje("5. Debajo del promedio")
mostrarDebajoPromedio(listaSueldos, promedio)

mensaje("Fin del programa")
