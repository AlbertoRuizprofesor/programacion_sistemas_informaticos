"""
Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float) 
Obtener el promedio de las mismas.
Contar cuántas personas son más altas que el promedio y cuántas más bajas.
"""

alturas = []
suma = 0

for x in range (5):
    valor = float(input("Introduce la altura: "))

    alturas.append(valor)
    suma = suma + valor

print("Las aluras son: ")
print(alturas)

media = suma / 5

print("El promedio de las alturas es: ")
print(media)

altas = 0
bajas = 0

for x in range (5):
    if alturas [x] > media:
        altas = altas + 1
    else:
        if alturas [x] < media:
            bajas = bajas + 1

print("Más altas que la media: ")
print(altas)

print("Más bajas que la media: ")
print(bajas)
