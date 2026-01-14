"""
Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. 
Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad
(mayores o iguales a 18 años) Imprimir la edad promedio de las personas.
"""

def cargar_datos():
    nombre = []
    edad = []
    for x in range(5):
        nom = input("Introduce el nombre: ")
        nombre.append(nom)
        ed = int(input("Introduce su edad: "))
        edad.append(ed)

    return [nombre, edad]

def mayor_edad(nombre, edad):
    print("Mayores de edad: ")
    for x in range(len(nombre)):
        if edad[x] > 18:
            print(nombre[x])

def media_edad(edad):
    suma = 0
    for x in range(len(edad)):
        suma = suma + edad[x]
    
    media = suma//5
    print("Media de las edades: ")

nombre,edad = cargar_datos()
mayor_edad(nombre, edad)
media_edad(edad)


