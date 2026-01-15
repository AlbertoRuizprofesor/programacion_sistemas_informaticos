"""
Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
3) Imprimir las dos listas generadas.
"""

def cargar_lista():
    lista = []
    for x in range(10):
        valor = int(input(f"Ingrese valor {x+1}: "))
        lista.append(valor)
    return lista

def generar_listas(lista):
    listanegativos = []
    listapositivos = []
    for x in range(len(lista)):
        if lista[x] < 0:
            listanegativos.append(lista[x])
        else:
            if lista[x] > 0:
                listapositivos.append(lista[x])
    return [listanegativos,listapositivos]

def imprimir_lista(lista):
    for x in range(len(lista)):
        print(lista[x])


# Programa principal
lista = cargar_lista()
listanegativos,listapositivos = generar_listas(lista)
print("--------------------------------------")
print("Lista de valores negativos: ")
imprimir_lista(listanegativos)
print("--------------------------------------")
print("Lista con los valores positivos: ")
imprimir_lista(listapositivos)

