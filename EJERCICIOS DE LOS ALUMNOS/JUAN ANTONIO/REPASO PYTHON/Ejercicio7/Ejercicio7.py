# Ejercicio 7. Análisis de palabras

texto = input("Introduce una frase: ").lower()

for simbolo in ",.;:¿?¡!":
    texto = texto.replace(simbolo, "")

terminos = texto.split()

conteo = {}
for termino in terminos:
    conteo[termino] = conteo.get(termino, 0) + 1

mas_extensa = ""
for termino in terminos:
    if len(termino) > len(mas_extensa):
        mas_extensa = termino

print("Cantidad de palabras:", len(terminos))
print("Palabras únicas:", set(terminos))
print("Palabra más larga:", mas_extensa)
print("Frecuencias:", conteo)

