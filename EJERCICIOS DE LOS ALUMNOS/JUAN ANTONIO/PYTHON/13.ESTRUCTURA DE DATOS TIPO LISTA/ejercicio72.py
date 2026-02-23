 #Definir por asignación una lista con 8 elementos enteros. 
 # Contar cuantos de dichos valores almacenan un valor superior a 100.

#Declaración de la lista
miLista = [10, 300, 1000, 50, 500, 25, 3000, 150]

#Declaración e iniciación de variables
cantidad = 0
x = 0

#Bucle while para determinar la cantidad de numeros que son superiores a 100
while x < len(miLista):
    if miLista[x] > 100:
        cantidad = cantidad + 1
    x = x + 1

#Imprime el resultado en consola: Elementos de la lista y cantidad de mayores a 100
print(f"La lista contiene los siguientes elementos: {miLista}")
print(f"La cantidad de valores mayores a 100 de la lista son: {cantidad}")


