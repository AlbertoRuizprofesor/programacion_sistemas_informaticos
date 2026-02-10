"""Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros.
Implementar una función que imprima el mayor y el menor valor de la lista."""
#Funciones
def mensaje(mensaje):
    print(f"\n=== === === {mensaje} === === ===")
def entradaDatos(numeroValores):
    for cntValores in range (numeroValores):
        listaValores.append(int(input(f"Introduce el valor {cntValores + 1}: ")))
def mayormenor(lista):
    mayor = lista[0]
    menor = lista[0]
    for cnt in lista:
        if mayor < cnt:
            mayor = cnt
        else:
            if menor > cnt:
                menor = cnt
    print(f"El número mayor es: {mayor}.\nEl número menor es: {menor}.")

#Main
listaValores = []
entradaDatos(5)
mensaje("Resultado")
mayormenor(listaValores)
mensaje("")
