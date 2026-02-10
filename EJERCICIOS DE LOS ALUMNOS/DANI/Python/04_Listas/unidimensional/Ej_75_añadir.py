# Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista. Imprimir la lista generada.

# El algoritmo propuesto crea primero una lista vacía (debemos asignar los corchetes de apertura y cerrado sin contenido):
lista=[]

#Luego mediante un for (podemos utilizar un while si queremos) solicitamos en forma sucesiva la carga de un entero por teclado y procedemos a agregarlo al final de la 
# lista llamando al método append:
for x in range(5):
    valor=int(input("Ingrese un valor entero:"))
    lista.append(valor)

# Finalmente mostramos los elementos de la lista creada:
print(lista)
