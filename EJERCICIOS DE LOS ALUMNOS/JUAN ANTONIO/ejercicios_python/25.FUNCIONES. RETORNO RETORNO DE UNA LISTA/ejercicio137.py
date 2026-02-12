#Confeccionar un programa que permita:
#1) Cargar una lista de 10 elementos enteros.
#2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
#3) Imprimir las dos listas generadas.


# ---------------------------------------------------------
# FUNCIÓN: cargar
# Solicita 10 valores enteros al usuario y los almacena en una lista.
# Devuelve la lista completa.
# ---------------------------------------------------------
def cargar():
    lista = []
    for x in range(10):
        valor = int(input("Ingrese valor:"))
        lista.append(valor)   # Agregamos cada valor ingresado
    return lista


# ---------------------------------------------------------
# FUNCIÓN: generar_listas
# Recibe una lista de números y genera dos listas nuevas:
#   - listanega: contiene los valores negativos
#   - listaposi: contiene los valores positivos
# Los ceros no se incluyen en ninguna lista.
# Devuelve ambas listas.
# ---------------------------------------------------------
def generar_listas(lista):
    listanega = []
    listaposi = []

    for x in range(len(lista)):
        if lista[x] < 0:              # Si es negativo, va a listanega
            listanega.append(lista[x])
        else:
            if lista[x] > 0:          # Si es positivo, va a listaposi
                listaposi.append(lista[x])
            # Si es 0, simplemente no se agrega a ninguna lista

    return [listanega, listaposi]


# ---------------------------------------------------------
# FUNCIÓN: imprimir
# Muestra todos los elementos de una lista, uno por línea.
# ---------------------------------------------------------
def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x])


# ---------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------

lista = cargar()                          # Cargamos los 10 valores
listanega, listaposi = generar_listas(lista)  # Generamos listas separadas

print("Lista con los valores negativos")
imprimir(listanega)

print("Lista con los valores positivos")
imprimir(listaposi)
