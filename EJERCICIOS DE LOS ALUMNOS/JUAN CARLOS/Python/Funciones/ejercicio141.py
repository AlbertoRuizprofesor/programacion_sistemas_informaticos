"""
Cargar una lista de 10 enteros,
luego mostrarlos por pantalla a cada elemento separados por una coma.
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

def entradaDatos(numeroValores):
    listaValores = []
    for cnt in range(numeroValores):
        valor = int(input(f"Introduce el valor {cnt + 1}: "))
        listaValores.append(valor)
    return listaValores

def mostrarConComas(lista):
    print(','.join(map(str, lista)))


#Main
listaNumeros = entradaDatos(10)
mensaje("Lista con comas")
mostrarConComas(listaNumeros)
mensaje("Fin del programa")
