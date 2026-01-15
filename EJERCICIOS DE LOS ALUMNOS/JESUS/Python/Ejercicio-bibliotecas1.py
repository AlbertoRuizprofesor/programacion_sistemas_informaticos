#Confeccionar una aplicación que permita cargar por teclado una lista de enteros, obtener y mostrar el mayor y calcular su suma. 
# Definir un módulo con las funciones de carga, identificar el mayor y sumar. 
# En el módulo principal del programa importar el otro módulo y llamar a sus funciones.


def cargar():
    lista=[]
    for x in range(5):
        valor=int(input("Ingrese valor:"))
        lista.append(valor)
    return lista


def imprimir_mayor(lista):
    may=lista[0]
    for x in range(1,5):
        if lista[x]>may:
            may=lista[x]
    print("Mayor de la lista",may)


def imprimir_suma(lista):
    suma=0
    for elemento in lista:
        suma=suma+elemento
    print("Suma de todos sus elementos",suma)
