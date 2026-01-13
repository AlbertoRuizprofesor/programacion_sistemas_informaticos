
notas=[]
n = int(input("¿Cuántas asignaturas quieres añadir? "))

for _ in range(n):
    asignatura = input("Nombre de la asignatura: ")
    nota = int(input("Nota: "))

    # Añadimos a la lista 2D
    notas.append([asignatura, nota])
    
    
