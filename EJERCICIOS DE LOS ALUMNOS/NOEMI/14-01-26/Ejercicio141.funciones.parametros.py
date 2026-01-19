#Ejercicio 141: Cargar una lista de 10 enteros, luego mostrarlos por pantalla a cada elemento separados por una coma.

def cargar():
    lista=[]
    for i in range(10):
        valores=int(input("Introduce un valor: "))
        lista.append(valores)
    return lista

def imprimir(lista):
    for i in range(len(lista)):
        print(lista[i], end=",")
        
    
lista=cargar()
imprimir(lista)