#Ejercicio 76: Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la carga de enteros al ingresar el cero. Mostrar finalmente el tamaño de la lista.

lista=[]

valor=int(input("Introduce un valor (finaliza con 0): "))

while 0!=valor:
    lista.append(valor)
    valor=int(input("Introduce un valor (finaliza con 0): "))
    

print("Los datos de la lista son: ", lista)
print("Tamaño de la lista es ", len(lista))