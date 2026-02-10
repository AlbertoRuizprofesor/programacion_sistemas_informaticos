"""
Confeccionar una función que reciba entre 2 y 5 enteros.
La misma nos debe retornar la suma de dichos valores. Debe tener tres parámetros por defecto.
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

def sumarEnteros(a, b, c=0, d=0, e=0):
    return a + b + c + d + e


#Main
resultado = sumarEnteros(10, 20)
print(f"Suma de 2: {resultado}")
mensaje("3 parámetros")
resultado = sumarEnteros(10, 20, 30)
print(f"Suma: {resultado}")
mensaje("5 parámetros")
resultado = sumarEnteros(1, 2, 3, 4, 5)
print(f"Suma: {resultado}")
mensaje("Fin del programa")
