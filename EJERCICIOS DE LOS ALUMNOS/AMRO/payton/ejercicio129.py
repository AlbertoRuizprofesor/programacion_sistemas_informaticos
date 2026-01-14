def multiplicar(lista,valor):
    for x in range(len(lista)):
        multi=lista[x]*valor
        print(multi)


# bloque main

lista=[3, 7, 8, 10, 2]
print("Lista original:",lista)
print("Lista multiplicando cada elemento por 3")
multiplicar(lista,3)