'''
Crea un archivo utilidades.py con funciones para calcular:
área de un círculo, perímetro de un rectángulo y conversión de grados a radianes. 
Luego impórtalo desde otro programa. 
'''

import utilidades

print(f"Área del círculo: {utilidades.area_circulo(6):.2f}") 
print(f"Perímetro del rectángulo: {utilidades.perimetro_rectangulo(2, 4):.2f}") 
print(f"Conversión de grados a radianes: {utilidades.grados_a_radianes(100):.2f}")
