'''
Pide un texto y extrae todos los correos electrónicos válidos que aparezcan en él. 
Idea clave: Usa expresiones regulares
'''

import re 
 
texto = input("Texto: ") 

# El patrón básico de correo electrónico válido: (letras, números, puntos o guiones + )
patron = r"[\w.-]+@[\w.-]+\.\w+" 
correos = re.findall(patron, texto) 
print(correos) 
