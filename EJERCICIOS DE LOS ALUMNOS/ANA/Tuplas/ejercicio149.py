# Confeccionar un programa con las siguientes funciones:
# 1) Cargar una lista de 5 enteros.
# 2) Retornar el mayor y menor valor de la lista mediante una tupla. Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.

def cargar_lista():

    lst = []
    print("Introduzca 5 numeros: ")

    for i in range(5):
        num = int(input(f"Introduzca el numero {i}: "))
        lst.append(num)

    return lst

def devuelve_maymen(lista):

    
    mayor = lista[0]
    menor = lista[0]

    for i in range(len(lista)): 
        if lista[i] > mayor:
            mayor = lista[i]
        
        elif lista[i] < menor:
            menor = lista[i]
        else: 
            continue 

    return (mayor,menor) 


lista = cargar_lista()

mayor, menor = devuelve_maymen(lista) 
print("Valor más grande encontrado en la lista: ", mayor)
print("Valor más pequeño encontrado en la lista: ", menor)