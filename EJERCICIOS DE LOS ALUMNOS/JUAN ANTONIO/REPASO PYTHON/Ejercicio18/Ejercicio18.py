# Ejercicio 18. Buscador de correos

import re

frase = input("Introduce un texto: ")
expresion = r"[\w.-]+@[\w.-]+\.\w+"

encontrados = re.findall(expresion, frase)

print(encontrados)
