'''
Pide una frase y muestra: 
número de palabras, conjunto de palabras únicas, palabra más larga y frecuencia de cada palabra. 
Idea clave: Ignora signos de puntuación básicos y no distingas mayúsculas de minúsculas. 
'''

frase = input("Introduce una frase: ").strip().lower()

numeroPalabras = len(frase.split())
palabrasUnicas = set(frase.split())
palabraMasLarga = max(frase.split(), key=len)
frecuencia = {}
for palabra in frase.split():
    palabra = palabra.strip('.,!?";()')  # Eliminar signos de puntuación
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print(f"Número de palabras: {numeroPalabras} \
      \nConjunto de palabras únicas: {palabrasUnicas} \
      \nPalabra más larga: {palabraMasLarga} \
      \nFrecuencia de cada palabra: {frecuencia}")