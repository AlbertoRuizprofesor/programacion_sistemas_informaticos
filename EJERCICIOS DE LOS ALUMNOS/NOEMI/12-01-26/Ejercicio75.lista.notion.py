#Ejercicio 75: Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista. Imprimir la lista generada.


lista=[]

for i in range(5):
    numeros=int(input("Introduzca un valor: "))
    lista.append(numeros)

print(lista)
    
    
    
lista=[]

for i in range(2):
    nombres=input("Introduce nombre: ")
    lista.append(nombres)
print(lista)