print("Ejercicio 137")
print("")
print("")

# Confeccionar un programa que permita:
# 1) Cargar una lista de 10 elementos enteros.
# 2) Generar dos listas a partir de la primera.
#  En una guardar los valores positivos y en otra los negativos.
# 3) Imprimir las dos listas generadas.

def cargar_datos():
    numeros = []
    for n in range(10):
        numero = int(input(f"Ingrese el número {n+1}: "))
        numeros.append(numero)
    return numeros

def separar_numeros(lista):
    positivos = []
    negativos = []
    for numero in lista:
        if numero >= 0:
            positivos.append(numero)
        else:
            negativos.append(numero)
    return positivos, negativos

def mostrar_listas(positivos, negativos):
    print("Números positivos:")
    for num in positivos:
        print(num)
    print("Números negativos:")
    for num in negativos:
        print(num)

numeros = cargar_datos()
positivos, negativos = separar_numeros(numeros)
mostrar_listas(positivos, negativos)


print("Fin del programa")
