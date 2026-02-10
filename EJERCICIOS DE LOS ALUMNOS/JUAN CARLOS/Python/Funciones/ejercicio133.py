"""
Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne.
Una segunda función debe recibir una lista y retornar el mayor y el menor valor de la lista.
Desde el bloque principal del programa llamar a ambas funciones e imprimir el mayor y el menor de la lista.
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

def entradaDatos(numeroValores):
    listaValores = []
    for cntValores in range (numeroValores):
        listaValores.append(int(input(f"Introduce el valor {cntValores + 1}: ")))
    return listaValores

def mayorMenor(lista):
    mayor = lista[0]
    menor = lista[0]
    for cnt in lista:
        if cnt > mayor:
            mayor = cnt
        if cnt < menor:
            menor = cnt
    return [mayor, menor]


#Main
listaNumeros = entradaDatos(5)
mayormenor = mayorMenor(listaNumeros)
mensaje("Resultado")
print(f"Mayor: {mayormenor[0]}")
print(f"Menor: {mayormenor[1]}")
mensaje("Fin del programa")
