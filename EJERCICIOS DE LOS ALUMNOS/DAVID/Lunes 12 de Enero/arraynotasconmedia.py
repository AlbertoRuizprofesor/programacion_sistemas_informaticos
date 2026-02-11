# Definimos la lista de listas (matriz)
notas_escolares = [
    ["Matemáticas", 10],
    ["Historia", 9],
    ["Lengua", 5]
]

# Variable para acumular la suma de las notas
suma_notas = 0

# Recorremos la lista usando un bucle
for i in range(len(notas_escolares)):
    # Sumamos la nota (que está en la posición 1 de cada sublista)
    suma_notas = suma_notas + notas_escolares[i][1]
    
    # Mostramos los datos de cada asignatura
    print(f"Posición {i}: Asignatura: {notas_escolares[i][0]}, Nota: {notas_escolares[i][1]}")


# Calculamos la media: Suma total dividida por la cantidad de elementos
media = suma_notas / len(notas_escolares)

print("-" * 30)
print(f"La nota media total es: {media}")