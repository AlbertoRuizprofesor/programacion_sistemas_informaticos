#Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado y nos retorne su superficie.

# Definimos una función que recibe el valor del lado de un cuadrado
# y devuelve su superficie (lado * lado)
def retornar_superficie(lado):
    sup = lado * lado   # Calculamos la superficie
    return sup          # Devolvemos el resultado

# ---------------------------------------------------------
# BLOQUE PRINCIPAL DEL PROGRAMA
# ---------------------------------------------------------

# Pedimos al usuario que ingrese el valor del lado del cuadrado
va = int(input("Ingrese el valor del lado del cuadrado: "))

# Llamamos a la función para obtener la superficie
superficie = retornar_superficie(va)

# Mostramos el resultado por pantalla
print("La superficie del cuadrado es", superficie)
