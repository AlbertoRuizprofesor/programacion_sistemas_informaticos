# Crear una lista de enteros por asignación. Definir una función que reciba una lista de enteros y 
# un segundo parámetro de tipo entero.
# Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado.

lista_enteros = [1, 2, 3, 4, 5]
entero = int(input("Ingrese un número entero: "))

def enteros_mult():
    for x in lista_enteros: #tras el for puedo llamar a la variable x, num (como quiera)
        print(x * entero)
    return enteros_mult

enteros_mult()
