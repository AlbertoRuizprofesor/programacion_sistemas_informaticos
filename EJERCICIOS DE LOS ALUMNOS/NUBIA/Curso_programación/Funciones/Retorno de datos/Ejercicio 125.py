# Confeccionar una función que calcule la superficie de un rectángulo y la retorne,
# la función recibe como parámetros los valores de dos de sus lados: 
# En el bloque principal del programa cargar los lados de dos rectángulos 
# y luego mostrar cual de los dos tiene una superficie mayor.

def retornar_superficie(lado1,lado2):
    superficie = lado1*lado2
    return superficie

print("Primer rectángulo")
lado1=int(input("Ingrese el lado menor del rectángulo: "))
lado2=int(input("Ingrese el lado mayor del rectángulo: "))

print("----------------------------------------------")

print("Segundo rectángulo")
lado3=int(input("Ingrese el lado menor del rectángulo: "))
lado4=int(input("Ingrese el lado mayor del rectángulo: "))

print("----------------------------------------------")

if retornar_superficie(lado1,lado2) == retornar_superficie(lado3,lado4):
    print("Los dos retángulos tiene la misma superficie")
else:
    if retornar_superficie(lado1,lado2) > retornar_superficie(lado3,lado4):
        print("El primer rectángulo tiene una superficie mayor")
    else:
        print("El segundo rectángulo tiene una superficie mayor")
