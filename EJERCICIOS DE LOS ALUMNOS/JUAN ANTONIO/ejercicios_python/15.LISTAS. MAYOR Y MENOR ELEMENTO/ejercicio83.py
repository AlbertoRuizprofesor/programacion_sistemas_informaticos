"""
Cargar una lista con 5 elementos enteros.
Imprimir el mayor y un mensaje si se repite dentro de la lista 
(es decir si dicho valor se encuentra en 2 o más posiciones en la lista)
"""
listaNumeros = []                     # Creamos una lista vacía para guardar los números

for x in range(5):                    # Repetimos 5 veces (índices 0 a 4)
    numero = int(input("Ingrese un número entero: "))  # Pedimos un número entero
    listaNumeros.append(numero)       # Lo añadimos a la lista

numeroMayor = listaNumeros[0]         # Suponemos que el primer número es el mayor (punto de partida)

for x in range(1, 5):                 # Recorremos la lista desde el segundo elemento
    if listaNumeros[x] > numeroMayor: # Si encontramos un número mayor que el actual...
        numeroMayor = listaNumeros[x]       # ...actualizamos numeroMayor

print(f"La lista completa es: {listaNumeros}")         # Mostramos la lista completa
print(f"El número mayor de la lista es: {numeroMayor}") # Mostramos el mayor encontrado

repeticion = 0                        # Contador para saber cuántas veces aparece el mayor
for x in range(5):                    # Recorremos toda la lista
    if listaNumeros[x] == numeroMayor: # Si el elemento es igual al mayor...
        repeticion += 1               # ...sumamos 1 al contador

if repeticion > 1:                    # Si aparece más de una vez...
    print(f"El mayor se repite en la lista {repeticion} veces")  # Lo informamos
