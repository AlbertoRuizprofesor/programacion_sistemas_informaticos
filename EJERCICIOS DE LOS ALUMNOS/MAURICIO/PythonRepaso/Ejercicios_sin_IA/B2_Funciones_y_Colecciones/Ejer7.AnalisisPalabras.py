# Pide una frase y muestra: número de palabras,
# conjunto de palabras únicas, palabra más larga y frecuencia de cada palabra.
# Ampliación: Ignora signos de puntuación básicos y no distingas mayúsculas de minúsculas.

import string
from collections import Counter # Para frecuencia de palabras pro con Counter(lista_palabras)

frase = input("Introduzca su frase: ")

# 1. Creamos la tabla para quitar signos y números
caracteres_a_quitar = string.punctuation + string.digits + "¿¡"
tabla = str.maketrans("", "", caracteres_a_quitar)

# 2. Limpiamos signos, pasamos a minúsculas y quitamos espacios de los extremos
frase = frase.translate(tabla).lower().strip()

# 3. Creamos una lista de palabras
lista_palabras = frase.split()

# 4. Creamos una frase limpia de caraceteres inadecuados
frase_limpia = " ".join(lista_palabras)

# 5. Calculamos el numero de palabras usando la longitud de la lista
numero_palabras = len(lista_palabras)

# 6. Hayamos la palabra más larga de la lista
palabra_mas_larga = lista_palabras[0]
for palabra in lista_palabras[1:]:
    if len(palabra_mas_larga) < len(palabra):
        palabra_mas_larga = palabra

# 7. Palabra más larca con max(lista,key=)
palabra_mas_larga2 = max(lista_palabras, key=len)

# 8. Lista de Palabras Unicas set(lista)
unicas = set(lista_palabras) # Elimina duplicados

# 9. Frecuencia de cada palabra
frecuencias = {} # Creamos un dicionario
for palabra in lista_palabras:
    # Si la clave no tiene asignado valor, .get devuelve 0 y le suma 1. clave:0+1
    # Si la ya tiene asignado un valor, .get devuelve el valor actual y le suma 1
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

# 10.Frecuencias de cada palabra Pro
frecuencias2 = Counter(lista_palabras)


print(f"Frase Limpia: '{frase_limpia}'")
print(f"Número total de palabras: {numero_palabras}")
print(f"La palabra más larga método 1 es: {palabra_mas_larga}")
print(f"La palabra más larga método PRO es: {palabra_mas_larga2}")
print(f"Palabras únicas: {unicas}")
print(f"Frecuencias de palabras método 1: {frecuencias}")
print(f"Frecuencias de palabras método PRO: {frecuencias2}")


