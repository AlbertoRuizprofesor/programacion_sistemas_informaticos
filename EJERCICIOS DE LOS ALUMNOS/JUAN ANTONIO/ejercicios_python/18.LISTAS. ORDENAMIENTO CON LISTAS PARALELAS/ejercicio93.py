#Confeccionar un programa que permita cargar los nombres de 5 alumnos y sus notas respectivas. 
# Luego ordenar las notas de mayor a menor. Imprimir las notas y los nombres de los alumnos.

alumnos = []
notas = []

# Cargamos los nombres y las notas de 5 alumnos
for x in range(5):
    nom = input("Ingrese el nombre del alumno:")   # Pedimos el nombre
    alumnos.append(nom)                            # Lo guardamos en la lista 'alumnos'

    no = int(input("Ingrese la nota de dicho alumno:"))  # Pedimos la nota
    notas.append(no)                                     # La guardamos en la lista 'notas'

# Ordenamos ambas listas de mayor a menor según la nota
for k in range(4):                     # Controla cuántas pasadas hacemos
    for x in range(4 - k):             # Compara pares consecutivos
        if notas[x] < notas[x + 1]:    # Si la nota actual es menor que la siguiente...
            # Intercambiamos las notas
            aux1 = notas[x]
            notas[x] = notas[x + 1]
            notas[x + 1] = aux1

            # Intercambiamos también los nombres en la misma posición
            aux2 = alumnos[x]
            alumnos[x] = alumnos[x + 1]
            alumnos[x + 1] = aux2

# Mostramos el resultado final
print("Lista de alumnos y sus notas ordenadas de mayor a menor")
for x in range(5):
    print(alumnos[x], notas[x])
