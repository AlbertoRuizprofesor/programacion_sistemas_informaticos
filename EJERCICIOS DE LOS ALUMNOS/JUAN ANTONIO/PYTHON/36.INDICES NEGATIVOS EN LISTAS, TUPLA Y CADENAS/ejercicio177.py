"""
Cargar una cadena de caracteres por teclado. Mostrar la cadena del final al principio utilizando subíndices negativos.
"""

# Se solicita una palabra al usuario
texto = input("Escribe una palabra: ")

# Variable que usaremos para recorrer la cadena desde el final
pos = -1

# Recorremos la palabra completa carácter por carácter
for i in range(len(texto)):
    # Imprimimos el carácter correspondiente desde el final
    print(texto[pos], end="")
    # Movemos el índice hacia atrás
    pos -= 1
