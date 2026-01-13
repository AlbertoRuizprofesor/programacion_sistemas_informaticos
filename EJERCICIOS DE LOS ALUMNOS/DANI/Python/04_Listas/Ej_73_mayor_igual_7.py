# Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos con valor iguales o superiores a 7.

# Creación de una lista vacía y variables
lista = []
x = 1

while x < 6 :
    num = int(input(f"Ingresa el {x}º número: "))
    if num >= 7:
        lista.append(num) # Esto indica que los numeros que meta el usuario se introducirán en la lista.
    x = x + 1

print(lista)