#Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne.
#Una segunda función debe recibir una lista y retornar el mayor y el menor valor de la lista. 
#Desde el bloque principal del programa llamar a ambas funciones e imprimir el mayor y el menor de la lista.

def cargar_lista():
    b=[]
    for i in range(5):
        var = int(input(f"ingrese el numero {i+1}: "))
        b.append(var)
    return b

def mayor_menor(lista):
    mayor = lista[0]
    menor = lista[0]

    for n in lista:
        if n > mayor:
            mayor = n
        if n < menor:
            menor = n
    
    return mayor, menor 

n = cargar_lista()
mayor, menor = mayor_menor(n)

print ("la lista es: " , n)
print ("el mayor de la lista es: " , mayor)
print ("el menor valor de la lista es: ", menor)

       
       


