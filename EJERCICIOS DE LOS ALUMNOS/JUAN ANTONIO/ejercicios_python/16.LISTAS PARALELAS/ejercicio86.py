"""
En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.
"""

# Creamos dos listas vacías: una para los nombres de los alumnos y otra para sus notas
nombres = []
notas = []

# Bucle que se repite 4 veces para pedir los datos de 4 alumnos
for x in range(4):
    nom = input("Ingrese nombre del alumno:")  # Pedimos el nombre del alumno
    nombres.append(nom)  # Guardamos el nombre en la lista 'nombres'

    no = int(input("Ingrese la nota de dicho alumno:"))  # Pedimos la nota del alumno
    notas.append(no)  # Guardamos la nota en la lista 'notas'

# Inicializamos un contador para saber cuántos alumnos tienen nota "Muy Bueno"
cantidad = 0

# Recorremos las 4 posiciones de las listas
for x in range(4):
    print(nombres[x])  # Mostramos el nombre del alumno
    print(notas[x])    # Mostramos su nota

    # Clasificamos la nota según el valor
    if notas[x] >= 8:
        print("Muy Bueno")  # Nota alta
        cantidad = cantidad + 1  # Sumamos al contador de "Muy Bueno"
    else:
        if notas[x] >= 4:
            print("Bueno")  # Nota media
        else:
            print("Insuficiente")  # Nota baja

# Mostramos cuántos alumnos obtuvieron la categoría "Muy Bueno"
print("La cantidad de alumnos muy buenos son")
print(cantidad)

