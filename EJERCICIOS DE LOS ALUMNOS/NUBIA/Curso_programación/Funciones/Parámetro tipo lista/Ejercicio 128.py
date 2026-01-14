# Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros. 
# Implementar una función que imprima el mayor y el menor valor de la lista.

numeros = []

for n in range(5):
    num = int(input(f"Introduce el número {n+1}: "))
    numeros.append(num)
    
def mayor_menor(numeros):
    mayor = max(numeros)
    menor = min(numeros)
    print(f"El mayor de los elementos de la lista es: {mayor}")
    print(f"El menor de los elementos de la lista es: {menor}")
    
def main():
    mayor_menor(numeros)
    
main()

