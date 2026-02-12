"""
Confeccionar una función que reciba entre 2 y n (siendo n = 2,3,4,5,6 etc.) valores enteros,
retornar la suma de dichos parámetros.
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

def sumar_multiplos(*args):
    suma = 0
    for cnt in args:
        suma += cnt
    return suma


#Main
print(f"Suma 2 nums: {sumar_multiplos(10, 20)}")
print(f"Suma 4 nums: {sumar_multiplos(1, 2, 3, 4)}")
print(f"Suma 6 nums: {sumar_multiplos(5, 10, 15, 20, 25, 30)}")
mensaje("Fin del programa")
