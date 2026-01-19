#Ejercicio 129: Crear una lista de enteros por asignación. Definir una función que reciba una lista de enteros y un segundo parámetro de tipo entero. Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado.

def multiplicar(lista,entero):
    for i in range(len(lista)):
        multi=lista[i]*entero
        print(multi)
        


lista=[4,6,2,7,8,9]
print("Lista original: ", lista)
print("Lista multiplicando cada elemento por 3: ", multiplicar(lista,3))



#OTRA FORMA DE HACERLO:

def multiplicar(lista):
    return [i*3 for i in lista]

lista=[3,5,7,8]
resultado=multiplicar(lista)

print("La lista de los valores es", lista)
print("El resultado de la multiplicación es: ", resultado)
    