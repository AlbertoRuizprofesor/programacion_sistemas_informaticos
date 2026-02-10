#Confeccionar una función que reciba entre 2 y 5 enteros. 
#La misma nos debe retornar la suma de dichos valores. Debe tener tres parámetros por defecto.

# -----------------------------------------
# Función: sumar
# Recibe entre 2 y 5 valores numéricos.
# Los parámetros v3, v4 y v5 son opcionales
# y valen 0 si no se envían.
# Devuelve la suma total.
# -----------------------------------------

def sumar(num1, num2, num3=0, num4=0, num5=0):
    s = num1 + num2 + num3 + num4 + num5
    return s


# -----------------------------------------
# Bloque principal del programa
# Se realizan varias llamadas a la función
# para mostrar cómo funciona con distintos
# números de argumentos.
# -----------------------------------------

print("La suma de 5 + 6")
print(sumar(5, 6))  # Solo usa v1 y v2

print("La suma de 1 + 2 + 3")
print(sumar(1, 2, 3))  # Usa v1, v2 y v3

print("La suma de 1 + 2 + 3 + 4 + 5")
x = sumar(1, 2, 3, 4, 5)  # Usa todos los parámetros
print(x)
