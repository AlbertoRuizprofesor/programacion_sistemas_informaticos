# Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. 
def crear_lista():
    lista = []
    
    for x in range(5):
        numero = int(input(f"Introduce el {x+1}º número: "))
        lista.append(numero)
    
    return lista

# Una segunda función debe recibir una lista y mostrar todos los valores mayores a 10. 
def mayor_10(lista):
    may_10 = []
    
    for list in lista:
        if list > 10:
            may_10.append(list)
            
    print (f"Lista: {lista}\nMayores de 10: {may_10}")

# Desde el bloque principal del programa llamar a ambas funciones.
mayor_10(crear_lista())