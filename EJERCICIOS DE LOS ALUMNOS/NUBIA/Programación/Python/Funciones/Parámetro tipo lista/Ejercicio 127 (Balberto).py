# Crear un programa que me pida en una lista 5 edades, me haga la media de edad en una función 
# y me diga el número de personas mayores de edad y menores de edad en otra función.

edades = []
for n in range (5):
    edad = int(input(f"Introduce la edad {n+1}: "))
    edades.append(edad)

def media_edad():
    media = (sum(edades) / len(edades))
    return edades, media

def mayor():
    mayores = 0 
    for edad in edades:
        if edad >= 18:
            mayores = mayores + 1
    return mayores

def menor():
    menores = 0
    for edad in edades:
        if edad < 18:
            menores = menores + 1
    return menores

edades, media = media_edad()
print(f"La media de edad es: {media}")
print(f"Las personas mayores de edad son: {mayor()}")
print(f"Las personas menores de edad son: {menor()}")