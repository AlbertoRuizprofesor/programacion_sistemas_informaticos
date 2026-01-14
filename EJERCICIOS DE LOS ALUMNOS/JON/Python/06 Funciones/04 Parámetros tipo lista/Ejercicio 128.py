print("ejercicio 128")
print("")
print("")

# Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros. 
# Implementar una función que imprima el mayor y el menor valor de la lista.

def mayor_menor(lista):
    mayor = lista[0]
    menor = lista[0]
    for n in range(len(lista)):
        if lista[n] > mayor:
            mayor = lista[n]
        if lista[n] < menor:
            menor = lista[n]
    print("El mayor valor de la lista es:", mayor)
    print("El menor valor de la lista es:", menor)

lista = []
for i in range(5):
    valor = int(input(f"Ingrese el valor entero {i + 1}: "))
    lista.append(valor)
mayor_menor(lista)


print("Fin del programa")