"""
Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas.
Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años).
Imprimir la edad promedio de las personas.
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

def entradaDatosPersonas(numeroPersonas):
    listaNombres = []
    listaEdades = []
    for cnt in range(numeroPersonas):
        nombre = input(f"Introduce el nombre {cnt + 1}: ")
        edad = int(input(f"Introduce la edad de {nombre}: "))
        listaNombres.append(nombre)
        listaEdades.append(edad)
    return [listaNombres, listaEdades]

def procesarPersonas(nombres, edades):
    print("Personas mayores de edad:")
    sumaEdades = 0
    for cnt in range(len(nombres)):
        sumaEdades += edades[cnt]
        if edades[cnt] >= 18:
            print(nombres[cnt])
    promedio = sumaEdades / len(edades)
    return promedio


#Main
listaNombres, listaEdades = entradaDatosPersonas(5)
mensaje("Resultado")
promedio = procesarPersonas(listaNombres, listaEdades)
print(f"Edad promedio: {promedio:.2f}")
mensaje("Fin del programa")
