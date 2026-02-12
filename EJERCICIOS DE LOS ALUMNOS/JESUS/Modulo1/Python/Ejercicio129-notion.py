#Crear una lista de enteros por asignación. 
# Definir una función que reciba una lista de enteros y un segundo parámetro de tipo entero. 
# Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado.

def multi(lista,valor):
    for x in range(len(lista)):
        multi=lista[x]*valor
        print(multi)


# bloque del programa

lista=[1,2,3,4,5] 
print("lista sin multiplicar ",lista)
print("resultado de la multiplicacion x 4 ")
multi(lista,4)