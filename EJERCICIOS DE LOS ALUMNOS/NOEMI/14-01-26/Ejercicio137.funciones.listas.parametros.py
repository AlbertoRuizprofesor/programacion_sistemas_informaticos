#Ejercicio 137: Confeccionar un programa que permita:
#1) Cargar una lista de 10 elementos enteros.
#2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
#3) Imprimir las dos listas generadas.

def cargar_lista():
    lista=[]
    for i in range(10):
        elementos=int(input("Introduce un valor: "))
        lista.append(elementos)
    return lista

def valores_positivos_negativos(lista):
    listanega=[]
    listaposi=[]
    for i in range(len(lista)):
        if lista[i]<0:
            listanega.append(lista[i])
        else:
            if lista[i]>0:
                listaposi.append(lista[i])
    return [listanega,listaposi]

def imprimir_listas(lista):
    for i in range(len(lista)):
        print(lista[i])
        

lista=cargar_lista()
listanega,listaposi=valores_positivos_negativos(lista)
print("Lista con valores negativos:")
imprimir_listas(listanega)
print("Lista con valores positivos:")
imprimir_listas(listaposi)

