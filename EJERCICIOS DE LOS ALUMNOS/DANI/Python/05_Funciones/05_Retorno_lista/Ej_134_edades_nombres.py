# Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. 
def personas():
    lista = [[],[]] # Creación de lista bidimensional
    for x in range(5):
        nombre = input(f"\nDime el nombre de la persona número {x+1}: ")
        edad = int(input("Ahora dame du edad: "))
        lista[0].append(nombre) # Añadir el nombre a la primera lista de la lista
        lista[1].append(edad)  # Añadir la edad a la segunda lista de la lista
    return lista

# Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)
def mayor_edad(lista):
    print("\nPersonas mayores de edad:")
    # Recorrer la sublista de edades
    for i in range(len(lista[1])):
        # Comprobar si el valor de la posicion 'i' dentro de la lista de edades es mayor de edad
        # e imprimir el nombre de la sublista de 'nombres' que tenga la misma posición
        if lista[1][i] >= 18: 
            print(lista[0][i]) 

# Imprimir la edad promedio de las personas.
def promedio_edad(lista):
    suma = sum(lista[1])
    promedio = suma / len(lista[1])
    return promedio

# -----PROGRAMA PRINCIPAL-----
datos = personas()
mayor_edad(datos)
print(f"Edad promedia: {promedio_edad(datos)}")