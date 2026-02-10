"""
Confeccionar una función que reciba un string como parámetro y en forma opcional un segundo string con un caracter. 
La función debe mostrar el string subrayado con el caracter que indica el segundo parámetro
"""

# -----------------------------------------
# Función: titulo_subrayado
# Recibe un título y un carácter opcional.
# Imprime el título y una línea de subrayado
# del mismo largo usando el carácter elegido.
# -----------------------------------------

def titulo_subrayado(titulo, caracter="*"):
    print(titulo)                     # Muestra el título
    print(caracter * len(titulo))     # Subraya usando el carácter repetido


# -----------------------------------------
# Bloque principal del programa
# Aquí llamamos a la función con distintos
# parámetros para ver cómo funciona.
# -----------------------------------------

titulo_subrayado("Sistema de Administracion")   # Usa el carácter por defecto "*"
titulo_subrayado("Ventas", "-")                 # Usa "-" como subrayado

