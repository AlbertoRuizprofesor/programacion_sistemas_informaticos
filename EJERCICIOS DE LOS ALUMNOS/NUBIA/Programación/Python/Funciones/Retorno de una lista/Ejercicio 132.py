def carga_lista():
    li = []
    for n in range(5):
        valor = int(input("Ingrese valor: "))
        li.append(valor)
    return li


def imprimir_mayor10(li):
    for x in range(len(li)):
        if li[x]>10:
            print("Elementos de la lista mayores a 10: ", li[x])



# Llamar funciones
lista = carga_lista() 
imprimir_mayor10(lista)