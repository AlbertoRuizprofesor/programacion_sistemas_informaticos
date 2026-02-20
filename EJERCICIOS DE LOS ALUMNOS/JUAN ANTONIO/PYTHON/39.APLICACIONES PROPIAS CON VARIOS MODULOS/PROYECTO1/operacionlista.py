
#Función para cargar 5 valores en una lista
def cargar():
    lista=[]    #Creamos una lista vacía
    for x in range(5):  #Repetimos 5 veces
        valor=int(input("Ingrese valor:"))  #Pedimos un número entero
        lista.append(valor)     #Lo agregamos a la lista
    return lista        #Devolvemos la lista completa

#Función para encontrar el mayor valor en la lista
def imprimir_mayor(lista):
    may=lista[0]    #Tomamos el primer valor como el mayor inicial
    for x in range(1,5):    # Recorremos desde el segundo hasta el quinto elemento
        if lista[x]>may:    # Si encontramos uno mayor
            may=lista[x]    # Lo actualizamos
    print("Mayor de la lista",may)  # Mostramos el resultado

# Función para sumar todos los elementos de la lista
def imprimir_suma(lista):
    suma=0  # Inicializamos la suma
    for elemento in lista:  # Recorremos cada número en la lista
        suma=suma+elemento  # Lo sumamos
    print("Suma de todos sus elementos",suma)   # Mostramos el total