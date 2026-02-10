# Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. 
# Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)
# Imprimir la edad promedio de las personas.

def cargar_datos():
    nombres = []
    edades = []
    
    for x in range(5):
        nombre = input(f"Ingrese el nombre de la persona {x+1}: ")
        nombres.append(nombre)
        edad = int(input(f"Ingrese la edad de la persona {x+1}: "))
        edades.append(edad)
    return nombres, edades


def mayores_edad(nombres, edades):
    print("Personas mayores de edad: ")
    
    for x in range(len(nombres)):
        if edades[x] >= 18:
            print(nombres[x])


def promedio_edades(edades):
    suma=0
    
    for x in range(len(edades)):
        suma = suma + edades[x]
    promedio = suma/5
    print(f"Edad promedio de las personas: {promedio}")

# Bloque principal
nombres,edades=cargar_datos()
mayores_edad(nombres,edades)
promedio_edades(edades)

