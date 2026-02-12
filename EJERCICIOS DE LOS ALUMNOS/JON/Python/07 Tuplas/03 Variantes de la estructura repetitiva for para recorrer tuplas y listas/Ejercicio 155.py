print("Ejercicio 155")
print("")
print("")

def cargar():
    lista=[]
    for i in range (5):
        num=int(input("Introduzca un valor: "))
        lista.append(num)
    return lista

def imprimir(lista):
    print("Lista completa: ")
    for elemento in lista:
        print(elemento)

def mayor(lista):
    mayor=lista[0]
    for elemento in lista:
        if elemento>mayor:
            mayor=elemento
    print(f"El elemento mayor es: {mayor}")

def sumar(lista):
    suma=0
    for elemento in lista:
        suma+=elemento
    print(f"La suma total de elementos es: {suma}")


lista=cargar()
imprimir(lista)
mayor(lista)
sumar(lista)

print("Fin de programa.")
