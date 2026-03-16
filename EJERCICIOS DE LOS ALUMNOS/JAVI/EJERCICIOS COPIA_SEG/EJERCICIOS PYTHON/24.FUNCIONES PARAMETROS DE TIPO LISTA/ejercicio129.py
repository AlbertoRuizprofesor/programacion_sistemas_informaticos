#Crear una lista de enteros por asignación. Definir una función que reciba una lista de enteros y un segundo parámetro de tipo entero.
#Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado.


#Función que multiplica cada elemento de una lista por un valor dado
def multiplicar(lista,va):
    for x in range(len(lista)):     #Recorremos la lista usando sus índices
        multi = lista[x] * va       #Multiplicamos el elemento actual pro el valor 'va'
        print(multi)                #Mostramos el resultado de la multiplicación



#Bloque principal
#Lista de ejemplo con varios números
lista = [3, 7, 8, 10, 2]

#Mostramos la lista original
print("Lista original: ", lista)

#Indicamos lo que vamos a hacer
print("Lista multiplicando cada elemento por 3")

#Llamamos a la función para multiplicar cada elemento por 3
multiplicar(lista, 3)
