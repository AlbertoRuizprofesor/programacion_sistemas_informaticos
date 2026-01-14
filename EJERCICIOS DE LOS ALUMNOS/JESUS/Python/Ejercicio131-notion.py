# Definir una lista de enteros por asignación en el bloque principal. 
# Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos. 
# Mostrar dicho producto en el bloque principal de nuestro programa.

def producto(lista_num):
    produc=1
    for x in range(len(lista_num)):
        produc=produc*lista_num[x]
    return produc


#bloque principal 

lista_num=[5,4,3,2,1]
print("Lista original",lista_num)
print("multiplicacion por elementos:", producto(lista_num))