print("Ejercicio 125")
print("")
print("")

# Confeccionar una función que calcule la superficie de un rectángulo y la retorne,
# la función recibe como parámetros los valores de dos de sus lados: 
# En el bloque principal del programa cargar los lados de dos rectángulos 
# y luego mostrar cual de los dos tiene una superficie mayor.

def superficie(lado1, lado2):
    sup = lado1 * lado2
    return sup

lado1_rect1 = int(input("Ingrese el valor del primer lado del rectángulo 1: "))
lado2_rect1 = int(input("Ingrese el valor del segundo lado del rectángulo 1: "))
lado1_rect2 = int(input("Ingrese el valor del primer lado del rectángulo 2: "))
lado2_rect2 = int(input("Ingrese el valor del segundo lado del rectángulo 2: "))
sup_rect1 = superficie(lado1_rect1, lado2_rect1)
sup_rect2 = superficie(lado1_rect2, lado2_rect2)    
if sup_rect1 > sup_rect2:
    print("El rectángulo 1 tiene una superficie mayor:", sup_rect1)
elif sup_rect2 > sup_rect1:
    print("El rectángulo 2 tiene una superficie mayor:", sup_rect2)
else:
    print("Ambos rectángulos tienen la misma superficie.")

print("Fin del programa")

