# Crear un programa que me pida en una lista 5 edades,
# me haga la media de edad en una función
# y me diga el número de personas mayores de edad
# y menores de edad
# en otra función.


# FUNCIONES


def cargar_edad():
    edades = []
    for i in range(5):
        edad = float(input(f"Introduce la edad del sujeto {i+1}: "))
        edades.append(edad)
    return edades


def calcular_media(lista):
    med = sum(lista) / len(lista)
    return med


def mayores_y_menores(lista):
    m = 0
    n = 0

    for i in range(5):
        if lista[i] >= 18:
            m += 1
        else:
            n += 1
    return m, n


# BLOKE

# Carga de datos
edades_alumnos = cargar_edad()

# Invocar la función calcular_media
media = calcular_media(edades_alumnos)
print(f"\nLa media de las edades de los alumnos es: {media} años")

# Invocar la función mayores y menores
mayores, menores = mayores_y_menores(edades_alumnos)
print(f"\nHay {mayores} alumnos mayores de edad y {menores} menores")
