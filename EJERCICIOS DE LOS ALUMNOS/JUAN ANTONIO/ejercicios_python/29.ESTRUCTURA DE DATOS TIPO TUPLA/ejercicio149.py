"""
Confeccionar un programa con las siguientes funciones:
1) Cargar una lista de 5 enteros.
2) Retornar el mayor y menor valor de la lista mediante una tupla. 
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.
"""

# -----------------------------------------
# Función: cargar_valores
# Solicita 5 números al usuario y los guarda
# en una lista. Devuelve la lista completa.
# -----------------------------------------

def cargar_valores():
    numeros = []                               # Lista vacía

    for i in range(5):                          # Se repite 5 veces
        valor = int(input("Ingrese un valor: "))
        numeros.append(valor)                   # Agrega el número a la lista

    return numeros                              # Devuelve la lista cargada


# -----------------------------------------
# Función: obtener_mayor_menor
# Recibe una lista de números y determina
# cuál es el mayor y cuál es el menor.
# Devuelve ambos dentro de una tupla.
# -----------------------------------------

def obtener_mayor_menor(numeros):
    mayor = numeros[0]                          # Inicializa con el primer valor
    menor = numeros[0]

    for i in range(1, len(numeros)):            # Recorre desde el segundo elemento
        if numeros[i] > mayor:                  # Si encuentra un número mayor
            mayor = numeros[i]
        elif numeros[i] < menor:                # Si encuentra un número menor
            menor = numeros[i]

    return (mayor, menor)                       # Devuelve ambos valores


# -----------------------------------------
# Bloque principal del programa
# -----------------------------------------

lista_numeros = cargar_valores()                # Carga los valores desde teclado
mayor, menor = obtener_mayor_menor(lista_numeros)

print("Mayor valor de la lista:", mayor)
print("Menor valor de la lista:", menor)

