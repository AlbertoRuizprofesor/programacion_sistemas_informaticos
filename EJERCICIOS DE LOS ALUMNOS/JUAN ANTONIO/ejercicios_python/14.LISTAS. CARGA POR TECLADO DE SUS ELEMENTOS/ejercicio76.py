#Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la carga de enteros al ingresar el cero. 
# Mostrar finalmente el tamaño de la lista.

#Declara una lista vacía
numeros = []

#Entrada de datos y pulsar 0 si se quiere terminar
numero_introducido = int(input("Ingrese un número (teclee 0 para terminar)"))

#Mientras no introduzcamos un 0 seguimos añadiendo números a la lista
while numero_introducido !=  0:
    numeros.append(numero_introducido)  #Introducción de elementos en la lista
    numero_introducido = int(input("Ingrese un número (teclee 0 para terminar)")) #Al teclear 0 se termina de ingresar datos
    
#Imprime la cantidad de numeros de la lista = numeros introducidos
print(f"Has introducido {len(numeros)} números")
