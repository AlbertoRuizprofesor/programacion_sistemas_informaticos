#Confeccionar una función que reciba entre 2 y n (siendo n = 2,3,4,5,6 etc.)
#valores enteros, retornar la suma de dichos parámetros.

# -----------------------------------------
# Función: sumar_valores
# Recibe al menos dos números obligatorios
# (a y b) y luego cualquier cantidad extra
# de valores gracias a *otros.
# Devuelve la suma total.
# -----------------------------------------

def sumar_valores(a, b, *otros):
    total = a + b                     # Suma mínima obligatoria

    for valor in otros:               # Recorre los valores adicionales
        total += valor                # Acumula cada número en 'total'

    return total                      # Devuelve el resultado final


# -----------------------------------------
# Bloque principal del programa
# Se prueban distintas llamadas a la función
# con diferente cantidad de argumentos.
# -----------------------------------------

print("La suma de 1 + 2")
print(sumar_valores(1, 2))            # Solo dos valores

print("La suma de 1 + 2 + 3 + 4")
print(sumar_valores(1, 2, 3, 4))      # Cuatro valores

print("La suma de 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10")
print(sumar_valores(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # Muchos valores
