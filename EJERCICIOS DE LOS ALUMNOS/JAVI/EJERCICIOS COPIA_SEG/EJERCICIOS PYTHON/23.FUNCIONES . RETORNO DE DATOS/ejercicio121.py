#Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.


# Definimos una función que recibe dos valores y devuelve el mayor de ellos
def retornar_mayor(v1, v2):
    # Comparamos ambos valores
    if v1 > v2:
        mayor = v1      # Si v1 es mayor, lo guardamos en 'mayor'
    else:
        mayor = v2      # Si no, v2 es el mayor
    return mayor         # Devolvemos el valor mayor

# ---------------------------------------------------------
# BLOQUE PRINCIPAL DEL PROGRAMA
# ---------------------------------------------------------

# Pedimos al usuario que ingrese dos valores enteros
valor1 = int(input("Ingrese el primer valor:"))
valor2 = int(input("Ingrese el segundo valor:"))

# Llamamos a la función y mostramos el resultado
print(retornar_mayor(valor1, valor2))
