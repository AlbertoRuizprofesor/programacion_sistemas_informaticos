# Ejercicio 20. Mini módulo matemático

# mimodulo.py
import math

def area_circunferencia(r):
    return math.pi * r ** 2

def borde_rectangulo(ancho, largo):
    return 2 * (ancho + largo)

def grados_a_rad(gr):
    return math.radians(gr)
