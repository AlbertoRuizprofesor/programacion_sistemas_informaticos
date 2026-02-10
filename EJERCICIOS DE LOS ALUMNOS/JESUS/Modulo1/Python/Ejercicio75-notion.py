#Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista. 
#Imprimir la lista generada.



#definimos la lista vacia
lista=[]
#creamos el bucle de 5 vueltas
for x in range(5):
    valor=(input("Ingrese un valor entero: "))
    lista.append(valor)

#imprimimos la lista 
print(lista)

