#Declaración de una lista vacía
lista = []

#Introducimos por teclado 5 valores utilizando un bucle for
for x in range(5):
    valor = int(input("Ingrese un valor entero: "))
    lista.append(valor)

#Imprime la lista
print(lista)