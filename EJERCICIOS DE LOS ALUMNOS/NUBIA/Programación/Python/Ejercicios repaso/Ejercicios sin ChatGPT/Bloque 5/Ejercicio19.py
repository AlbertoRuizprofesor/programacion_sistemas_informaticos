'''
Simula 1000 lanzamientos de dos dados y muestra cuántas veces aparece cada suma. 
Idea clave: Usa random y una estructura adecuada para contar frecuencias. 
'''

import random 
 
frecuencias = {numero: 0 for numero in range(2, 13)} 
 
for _ in range(1000): 
    suma = random.randint(1, 6) + random.randint(1, 6) 
    frecuencias[suma] += 1 
 
for suma, veces in frecuencias.items(): 
    print(f"El número {suma} aparece {veces} veces.") 