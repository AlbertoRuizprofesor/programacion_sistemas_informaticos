#Ejercicio CODESHARE LISTAS.

#añadir listas multidimensionales

n = int(input("¿Cuántas asignaturas quieres añadir? "))

for _ in range(n):     # el _ no declara ninguna variable
    asignatura = input("Nombre de la asignatura: ")
    nota = int(input("Nota: "))

    # Añadimos a la lista 2D
    nota.append([asignatura, nota])
    