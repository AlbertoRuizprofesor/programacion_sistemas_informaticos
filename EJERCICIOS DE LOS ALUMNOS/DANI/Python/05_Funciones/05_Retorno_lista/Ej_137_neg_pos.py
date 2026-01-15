# Confeccionar un programa que permita:
# 1) Cargar una lista de 10 elementos enteros.
def numeros():
    lista = []
    for x in range(10):
        numero = int(input("Inserta número: "))
        lista.append(numero)
    return lista

# 2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
def pos_neg(lista):
    positivos = []
    negativos = []
    
    for list in lista:
        if list >= 0:
            positivos.append(list)
        else:
            negativos.append(list)
    return positivos, negativos

# 3) Imprimir las dos listas generadas.
def impresion(positivos,negativos):
    print(f"Lista de negativos: {negativos}")
    print(f"Lista de positivos: {positivos}")

datos = numeros()
positivos, negativos = pos_neg(datos)
impresion(positivos, negativos)