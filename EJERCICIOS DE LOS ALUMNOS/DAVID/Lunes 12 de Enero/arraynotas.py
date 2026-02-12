# Definimos la lista de listas (matriz)
# Cada elemento interno es [Nombre de materia, Nota]
notas_escolares = [
    ["Matemáticas", 10],
    ["Historia", 9],
    ["Lengua", 5]
]

# Recorremos la lista usando un bucle
# len(notas_escolares) nos da el total de pares (3 en este caso)
for i in range(len(notas_escolares)):
    # notas_escolares[i] accede a la sublista, por ejemplo ["Matemáticas", 10]
    # notas_escolares[i][0] accede al nombre
    # notas_escolares[i][1] accede al número
    print(f"Posición {i}: Asignatura: {notas_escolares[i][0]}, Nota: {notas_escolares[i][1]}")