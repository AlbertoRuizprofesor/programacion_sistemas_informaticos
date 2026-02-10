

# Confeccionar un programa que permita la carga de una lista de 5 enteros por teclado.
# Luego en otras funciones:
# 1) Imprimirla en forma completa.
# 2) Obtener y mostrar el mayor.
# 3) Mostrar la suma de todas sus componentes.

def cargar_datos():
    lista=[]
    
    for i in range(5): 
        num=int(input("Ingrese un valor:"))
        lista.append(num)
    
    return lista


def imprimir(lista):
    
    print("Lista completa")
    
    for elemento in lista: 
        print(elemento)


def mayor(lista):
    
    mayor=lista[0]

    for elemento in lista:
        if elemento>mayor:
            mayor=elemento
    
    print("El elemento mayor de la lista es",mayor)


def sumar_elementos(lista):
    
    suma=0

    for elemento in lista:
        suma=suma+elemento
    
    print("La suma de todos sus elementos es",suma)


# bloque principal

lista=cargar_datos()
imprimir(lista)
mayor(lista)
sumar_elementos(lista)