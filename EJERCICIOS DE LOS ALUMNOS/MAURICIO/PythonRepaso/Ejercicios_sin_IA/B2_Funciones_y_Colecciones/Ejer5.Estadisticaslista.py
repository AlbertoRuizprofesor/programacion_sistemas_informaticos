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


import random

# Generamos una lista de 10 números entre 1 y 50
lista = [random.randint(1, 50) for _ in range(10)]

# Agragamos 10 números aleatorios más usando bucle y .append()
for i in range(10):
    # Genera un número entero entre 1 y 100
    num = random.randint(1, 100)
    lista.append(num)

print(f"Lista de trabajo con 20 números: {lista}")
print(f"Maximo Valor de la lista: {maximo(maximo)}")
