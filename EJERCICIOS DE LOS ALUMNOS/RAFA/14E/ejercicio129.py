def multiplicar(lista,va):
    for x in range(len(lista)):
        multi=lista[x]*va
        print(multi)

lista=[3,7,8,10,2]
print("lista original: ", lista)
print("lista multiplicando cada elemento por 3")
multiplicar(lista,3)