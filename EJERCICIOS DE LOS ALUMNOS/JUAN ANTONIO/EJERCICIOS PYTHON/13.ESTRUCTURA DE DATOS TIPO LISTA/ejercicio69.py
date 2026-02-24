# Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.

lista = [10, 7, 3, 7, 2]   # Lista de números cuyos valores queremos sumar
suma = 0                   # Acumulador donde iremos sumando los elementos
x = 0                      # Índice para recorrer la lista con el while

while x < len(lista):      # Mientras x sea menor que la longitud de la lista...
    suma = suma + lista[x] # Sumamos el elemento actual de la lista al acumulador
    x = x + 1              # Avanzamos al siguiente índice para continuar el recorrido

print("Los elementos de la lista son: ")        # Mostramos la lista completa  
print(lista)               

print(f"La suma de todos sus elementos es: {suma}")     # Mostramos el resultado final de la suma
               
