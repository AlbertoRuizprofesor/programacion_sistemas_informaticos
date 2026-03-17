# Ejercicio 5. Estadísticas de una lista
# Dada una lista de números, crea funciones que devuelvan el mínimo,
# el máximo, la media y cuántos valores están por encima de la media.
# Ampliación: Evita usar min, max y sum en la primera versión.


def maximo(parametrosLista):
    maximo = parametrosLista[0]
    for dato in parametrosLista:
        if maximo < dato:
            maximo = dato
    return maximo

def minimo(parametrosLista):
    minimo = parametrosLista[0]
    for dato in parametrosLista:
        if minimo > dato:
            minimo = dato
    return minimo

def media(parametrosLista):
    suma = 0
    for dato in parametrosLista:
        suma += dato
    return suma / len(parametrosLista)

def contar_valores_mayores_media(parametrosLista):
    media_lista = media(parametrosLista)
    contador = 0
    for dato in parametrosLista:
        if dato > media_lista:
            contador += 1
    return contador

import random

# Generamos una lista de 10 números entre 1 y 50
lista = [random.randint(1, 50) for _ in range(10)]

# Agragamos 10 números aleatorios más usando bucle y .append()
for _ in range(10):
    # Genera un número entero entre 1 y 100
    num = random.randint(1, 100)
    lista.append(num)

print(f"Lista de trabajo con 20 números: {lista}")
print(f"Máximo Valor de la lista: {maximo(lista)}")
print(f"Mínimo Valor de la lista: {minimo(lista)}")
print(f"Media de la lista: {media(lista)}")
print(f"Cantidad de valores por encima de la media: {contar_valores_mayores_media(lista)}")
