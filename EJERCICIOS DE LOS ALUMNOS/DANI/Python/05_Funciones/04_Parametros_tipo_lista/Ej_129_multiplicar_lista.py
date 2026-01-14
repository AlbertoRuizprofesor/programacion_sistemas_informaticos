# Definir una función que reciba una lista de enteros y un segundo parámetro de tipo entero. Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado.
def multiplicar(lista,num):
    lista_multiplicada = []
    for list in lista:
        list *= num
        lista_multiplicada.append(list)
    return lista_multiplicada

# Crear una lista de enteros por asignación. 
lista=[3, 7, 8, 10, 2]
print(f"Lista: {lista}\nLista multiplicada: {multiplicar(lista,3)}")