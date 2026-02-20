"""
Confeccionar una función que reciba una cadena de caracteres y nos devuelva los tres primeros.

En el bloque principal del programa definir una tupla con los nombres de meses. Mostrar por pantalla 
los primeros tres caracteres de cada mes.
"""
# Función que devuelve los primeros tres caracteres de una cadena
def extraer_inicio(texto):
    # Usamos slicing para obtener solo las tres primeras letras
    return texto[:3]


# Programa principal

# Tupla con todos los meses del año
lista_meses = (
    'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
    'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'
)

# Recorremos cada mes y mostramos sus primeras tres letras
for mes in lista_meses:
    print(extraer_inicio(mes))

