# Ejercicio 19. Lanzador de dados

import random

conteo = {n: 0 for n in range(2, 13)}

for _ in range(1000):
    resultado = random.randint(1, 6) + random.randint(1, 6)
    conteo[resultado] += 1

for suma, cantidad in conteo.items():
    print(suma, cantidad)


