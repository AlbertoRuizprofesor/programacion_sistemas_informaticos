"""
Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera.
    En una guardar los valores positivos y en otra los negativos.
3) Imprimir las dos listas generadas.
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

def separarPositivosNegativos(lista):
    listaPositivos = []
    listaNegativos = []
    for cnt in lista:
        if cnt > 0:
            listaPositivos.append(cnt)
        elif cnt < 0:
            listaNegativos.append(cnt)
    return listaPositivos, listaNegativos

def imprimirListas(positivos, negativos):
    print("Lista positivos:")
    for cnt in positivos:
        print(cnt)
    print("Lista negativos:")
    for cnt in negativos:
        print(cnt)


#Main
listaOriginal = entradaDatos(10)
mensaje("1. Carga completada")

listaPositivos, listaNegativos = separarPositivosNegativos(listaOriginal)
mensaje("3. Listas generadas")
imprimirListas(listaPositivos, listaNegativos)

mensaje("Fin del programa")
