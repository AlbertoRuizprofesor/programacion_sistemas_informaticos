#Definir una lista por asignación con 5 enteros. 
# Mostrar por pantalla solo los elementos con valor iguales o superiores a 7.

#Declaración de la lista numeros
numeros = [5,10,25,5,100]

#Declaración e iniciación de la variable x
x = 0

#Imprime en pantalla mensaje
print("Elementos de la lista con valores iguales o superiores a 7:")

#Calcula los números iguales o mayores a 7 y los imprime en consola
while x < len(numeros):
    if numeros[x] >= 7:
        print(numeros[x], end = " ")
    x = x + 1