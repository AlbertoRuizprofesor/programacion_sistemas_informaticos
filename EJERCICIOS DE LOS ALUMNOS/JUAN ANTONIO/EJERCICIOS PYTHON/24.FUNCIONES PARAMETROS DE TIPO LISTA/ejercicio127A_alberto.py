#1. Pedir 5 notas al usuario
#2. Guardarlas en una lista
#3. Calcular la media
#4. Decir si has aprobado o suspendido


#Función que pide 5 notas al usuario y las guarda en una lista
def cargar_nota():
    notas = []  #Lista vacía done iremos guardando las notas
    for x in range(5):  #Repetimos 5 veces (x vale 0, 1, 2, 3, 4)
        nota = float(input(f"Introduce la nota {x + 1}: "))     # Pedimos una nota al usuario. Usamos x+1 para mostrar "nota 1", "nota 2", etc.
        notas.append(nota)  #Añadimos la nota a la lista
    return notas    #Devolvemos la lista completa de notas


#Función que calcula la media de las notas
def calcular_media(notas):
    return sum(notas) / len(notas)
    #sum(notas) suma todos los valores de la lista
    #len(notas) devuelve cuántos elementos hay en la lista

#Función que muestra si has aprobado o suspendido según la media
def mostrar_resultado(media):
    if media >= 5:  #Si la media es 5 o más, está aprobado
        print(f"Has aprobado con una media de {media:.2f}")
    else:   #Si es menor que 5, está suspendido
        print(f"Has suspendido con una media de {media:.2f}")

#Llamamos a las funciones:
#1. Pedimos las notas
#2. Calculamos la media
#3. Mostramos el resultado
media = calcular_media(cargar_nota())
mostrar_resultado(media)


