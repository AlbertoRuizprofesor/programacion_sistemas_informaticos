"""
Confeccionar una función que calcule la superficie de un rectángulo y la retorne, 
la función recibe como parámetros los valores de dos de sus lados: En el bloque principal 
del programa cargar los lados de dos rectángulos y luego mostrar cual de los dos tiene una superficie mayor.
"""


# Definimos una función que recibe dos lados de un rectángulo
# y devuelve su superficie multiplicando lado menor por lado mayor.
def retornar_superficie(lado1, lado2):
    superficie = lado1 * lado2   # Fórmula de la superficie del rectángulo
    return superficie            # Devolvemos el resultado

# ---------------------------------------------------------
# BLOQUE PRINCIPAL DEL PROGRAMA
# ---------------------------------------------------------

# Pedimos los datos del primer rectángulo
print("Primer rectangulo")
lado1 = int(input("Ingrese lado menor del rectangulo:"))
lado2 = int(input("Ingrese lado mayor del rectangulo:"))

# Pedimos los datos del segundo rectángulo
print("Segundo rectangulo")
lado3 = int(input("Ingrese lado menor del rectangulo:"))
lado4 = int(input("Ingrese lado mayor del rectangulo:"))

# Comparamos las superficies de ambos rectángulos
if retornar_superficie(lado1, lado2) == retornar_superficie(lado3, lado4):
    print("Los dos rectangulos tienen la misma superficie")
else:
    # Si no son iguales, verificamos cuál es mayor
    if retornar_superficie(lado1, lado2) > retornar_superficie(lado3, lado4):
        print("El primer rectangulo tiene una superficie mayor")
    else:
        print("El segundo rectangulo tiene una superficie mayor")
