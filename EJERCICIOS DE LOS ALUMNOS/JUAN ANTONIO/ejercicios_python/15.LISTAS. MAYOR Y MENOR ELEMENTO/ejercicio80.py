#Crear y cargar una lista con 5 enteros. 
# Implementar un algoritmo que identifique el mayor valor de la lista.

numeros = []                     # Creamos una lista vacía donde guardaremos los valores ingresados

for x in range(5):               # Repetimos 5 veces (índices 0 a 4)
    elemento = int(input("Ingrese un valor: "))  # Pedimos un número entero al usuario
    numeros.append(elemento)     # Lo añadimos a la lista

elementoMayor = numeros[0]       # Suponemos que el primer elemento es el mayor (punto de partida)

for x in range(1, 5):            # Recorremos la lista desde el segundo elemento hasta el último
    if numeros[x] > elementoMayor:   # Si encontramos un número mayor que el actual máximo...
        elementoMayor = numeros[x]   # ...actualizamos el valor del máximo

print(f"Lista completa: {numeros}")  # Mostramos la lista completa ingresada por el usuario
print(f"El elemento mayor de la lista es: {elementoMayor}")  # Mostramos el mayor encontrado
