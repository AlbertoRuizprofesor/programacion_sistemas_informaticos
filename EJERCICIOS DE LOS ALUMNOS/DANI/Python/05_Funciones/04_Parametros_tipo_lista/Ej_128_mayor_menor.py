# Implementar una función que imprima el mayor y el menor valor de la lista.
def menor(lista):
    men=lista[0]
    may=lista[0]
    for x in range(1,len(lista)):
        if lista[x]<men:
            men=lista[x]
        elif lista[x]>may:
            may=lista[x]
    
    print(f"\nLista: {lista}\nMayor: {may}\nMenor: {men}")

# Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros. 
numeros = []

for x in range(5):
    num = int(input(f"Dame el {x+1}º número: "))
    numeros.append(num)

menor(numeros)