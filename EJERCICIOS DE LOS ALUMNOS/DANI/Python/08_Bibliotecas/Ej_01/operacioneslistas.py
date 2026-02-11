def cargar():
    lista = []
    for x in range(5):
        valor = int(input(f"Dame el {x+1}º número: "))
        lista.append(valor)
    return lista

def imprmir_mayor(lista):
    mayor = lista[0]
    for x in range(len(lista)):
        if lista[x] > mayor:
            mayor = lista[x]
    print(f"El mayor es: {mayor}")

def imprimir_suma(lista):
    suma = 0
    for num in lista:
        suma += num
    print(f"La suma es: {suma}")