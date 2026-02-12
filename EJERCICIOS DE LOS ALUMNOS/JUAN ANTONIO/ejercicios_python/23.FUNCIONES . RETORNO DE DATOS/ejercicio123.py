#Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos.

# Definimos una función que recibe tres valores y devuelve su promedio.
# Usamos // para hacer una división entera (sin decimales).
def retornar_promedio(v1, v2, v3):
    promedio = (v1 + v2 + v3) // 3   # Sumamos los tres valores y dividimos entre 3
    return promedio                  # Devolvemos el resultado

# ---------------------------------------------------------
# BLOQUE PRINCIPAL DEL PROGRAMA
# ---------------------------------------------------------

# Pedimos al usuario que ingrese tres valores enteros
valor1 = int(input("Ingrese primer valor:"))
valor2 = int(input("Ingrese segundo valor:"))
valor3 = int(input("Ingrese tercer valor:"))

# Llamamos a la función y mostramos el promedio calculado
print("Valor promedio de los tres numeros", retornar_promedio(valor1, valor2, valor3))
