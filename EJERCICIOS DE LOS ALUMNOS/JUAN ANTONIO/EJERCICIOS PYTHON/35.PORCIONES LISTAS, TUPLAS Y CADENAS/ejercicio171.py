"""
Confeccionar una función que le enviemos un número de mes como parámetro y nos 
retorne una tupla con todos los nombres de meses que faltan hasta fin de año.
"""

# Función que devuelve los meses restantes del año a partir de un número dado
def obtener_meses_restantes(numero_mes):
    # Tupla con los nombres de todos los meses del año
    lista_meses = (
        'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
        'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'
    )

    # Retorna la porción de la tupla desde el mes indicado hasta el final
    return lista_meses[numero_mes:]


# Programa principal
print("Mostrar los meses que quedan hasta finalizar el año")

# Se solicita al usuario un número de mes (0 = enero, 11 = diciembre)
mes_ingresado = int(input("Introduce el número del mes: "))

# Llamamos a la función para obtener los meses restantes
restantes = obtener_meses_restantes(mes_ingresado)

# Mostramos el resultado
print(restantes)
