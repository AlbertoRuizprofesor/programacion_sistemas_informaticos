"""
Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne.
Una segunda función debe recibir una lista y mostrar todos los valores mayores a 10.
Desde el bloque principal del programa llamar a ambas funciones.
"""
#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

def entradaDatos(numeroValores):
    listaValores = []
    for cntValores in range (numeroValores):
        listaValores.append(int(input(f"Introduce el valor {cntValores + 1}: ")))
    return listaValores

def mostrarMayoresDiez(lista):
    print("Valores mayores a 10:")
    for cnt in lista:
        if cnt > 10:
            print(cnt)


#Main
listaNumeros = entradaDatos(5)
mensaje("Resultado")
mostrarMayoresDiez(listaNumeros)
mensaje("Fin del programa")
