# Ejercicio 5. Estadisticas de una lista
def minimo(lista):
    menor = lista[0]
    for num in lista:
        if num < menor:
            menor = num
    return menor

def maximo(lista):
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor

def media(lista):
    total = 0
    contador = 0
    for num in lista:
        total += num
        contador += 1
    return total / contador

def valores_por_encima(lista):
    m = media(lista)
    contador = 0
    for num in lista:
        if num > m:
            contador += 1
    return contador


# --- PRUEBA ---
numeros = [5, 8, 2, 10, 3, 25, 24, 12]

print("Mínimo:", minimo(numeros))
print("Máximo:", maximo(numeros))
print("Media:", media(numeros))
print("Valores por encima de la media:", valores_por_encima(numeros))
