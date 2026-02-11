#Ejercicio 148: Tupplas.: Definir una tupla con tres valores enteros. Convertir el contenido de la tupla a tipo lista. Modificar la lista y luego convertir la lista en tupla.

tupla=(2,5,7)
print("La primera tupla")
print(tupla)
lista=list(tupla)
print("imprimir la lista")
print(lista)
lista[0]=3
print("imprimir lista modificada")
print(lista)
tupla2=tuple(lista)
print("imprimir segunda tupla copiada de la lista")
print(tupla2)