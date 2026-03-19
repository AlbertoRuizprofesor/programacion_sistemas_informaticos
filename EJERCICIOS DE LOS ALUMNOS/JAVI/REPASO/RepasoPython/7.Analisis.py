frase = input("Frase: ").lower()
for signo in ",.;:¿?¡!":
    frase = frase.replace(signo, "")

palabras = frase.split()
frecuencias = {}
for palabra in palabras:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

mas_larga = ""
for palabra in palabras:
    if len(palabra) > len(mas_larga):
        mas_larga = palabra

print("Número de palabras:", len(palabras))
print("Únicas:", set(palabras))
print("Más larga:", mas_larga)
print("Frecuencias:", frecuencias)
