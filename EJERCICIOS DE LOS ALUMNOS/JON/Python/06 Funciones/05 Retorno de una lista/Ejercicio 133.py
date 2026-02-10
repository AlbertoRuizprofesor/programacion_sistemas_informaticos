print("Ejercicio 133")
print("")
print("")

# Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne.
# Una segunda función debe recibir una lista y retornar el mayor y 
# el menor valor de la lista. 
# Desde el bloque principal del programa llamar a ambas funciones e 
# imprimir el mayor y el menor de la lista.

def cargar_lista():
    lista=[]
    for n in range(5):
        valor=int(input(f"Ingrese el valor entero {n+1}: "))
        lista.append(valor)
    return lista

def mayor_menor(lista):
    mayor = max(lista)
    menor = min(lista)
    return mayor, menor

lista = cargar_lista()
mayor, menor = mayor_menor(lista)
print("El mayor valor de la lista es:", mayor)
print("El menor valor de la lista es:", menor)

print("Fin del programa")
