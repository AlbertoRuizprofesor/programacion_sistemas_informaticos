#Calculadora con funciones


# Pedimos dos números enteros al usuario
numero1 = int(input("Introduzca un número: "))
numero2 = int(input("Introduza un número: "))

# ---------------------------------------------------------
# FUNCIÓN SUMA
# Recibe dos números y devuelve su suma
# ---------------------------------------------------------
def suma(numero1, numero2):
    resultado_suma = numero1 + numero2
    return resultado_suma

# Mostramos el resultado de la suma usando la función
print(f"La suma de {numero1} + {numero2} es igual a {suma(numero1, numero2)}")

# ---------------------------------------------------------
# FUNCIÓN RESTA
# Devuelve la resta del primer número menos el segundo
# ---------------------------------------------------------
def resta(numero1, numero2):
    resultado_resta = numero1 - numero2
    return resultado_resta

# Mostramos el resultado de la resta
print(f"La resta de {numero1} - {numero2} es igual a {resta(numero1, numero2)}")

# ---------------------------------------------------------
# FUNCIÓN PRODUCTO
# Devuelve la multiplicación de ambos números
# ---------------------------------------------------------
def producto(numero1, numero2):
    resultado_producto = numero1 * numero2
    return resultado_producto

# Mostramos el resultado del producto
print(f"El producto de {numero1} * {numero2} es igual a {producto(numero1, numero2)}")

# ---------------------------------------------------------
# FUNCIÓN COCIENTE
# Devuelve la división formateada con dos decimales usando :f
# ---------------------------------------------------------
def cociente(numero1, numero2):
    resultado_cociente = numero1 / numero2
    return f"{resultado_cociente:.2f}"   # Formato con dos decimales

# Mostramos el resultado del cociente
print(f"El cociente de {numero1} / {numero2} es igual a {cociente(numero1, numero2)}")



