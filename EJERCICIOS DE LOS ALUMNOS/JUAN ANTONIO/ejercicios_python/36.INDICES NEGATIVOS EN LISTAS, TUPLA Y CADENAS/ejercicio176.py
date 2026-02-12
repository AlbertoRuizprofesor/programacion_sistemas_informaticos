"""
Confeccionar una función que reciba una palabra y verifique si es capicúa 
(es decir que se lee igual de izquierda a derecha que de derecha a izquierda)
"""

# Función que verifica si una palabra es capicúa (palíndromo)
def es_palindromo(texto):
    pos = -1          # Índice que recorrerá la cadena desde el final
    coincidencias = 0 # Contador de letras iguales en posiciones simétricas

    # Recorremos solo la mitad de la cadena
    for i in range(0, len(texto) // 2):
        # Comparamos el carácter desde el inicio con el correspondiente desde el final
        if texto[i] == texto[pos]:
            coincidencias += 1
        pos -= 1  # Movemos el índice hacia atrás

    # Mostramos la cadena analizada
    print(texto)

    # Si todas las comparaciones coinciden, es palíndromo
    if coincidencias == (len(texto) // 2):
        print("Es capicua")
    else:
        print("No es capicua")


# Bloque principal del programa
es_palindromo("neuquen")
es_palindromo("casa")
