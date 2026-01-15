#Ejercicio 131: Definir una lista de enteros por asignación en el bloque principal. Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos. Mostrar dicho producto en el bloque principal de nuestro programa.

def recibir_productos(lista):
    producto=1
    for i in range(len(lista)):
        producto=producto*lista[i]
    return producto


lista=[3,4,7,2,7,9]
print("Lista:",lista)
print("Multiplicación de todos sus elementos: ", recibir_productos(lista))

#EN ESTE CASO DE ABAJO SE MULTIPLICA POR UN NUMERO:

def multiplicar_por_numero(lista, n):
    nueva_lista = []
    for i in range(len(lista)):
        nueva_lista.append(lista[i] * n)
    return nueva_lista

lista = [3,4,7,2,7,9]
resultado = multiplicar_por_numero(lista, 3)

print("Lista original:", lista)
print("Lista multiplicada por 3:", resultado)