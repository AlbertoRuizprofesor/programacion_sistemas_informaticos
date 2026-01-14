print("Ejercicio 127B")
print("")
print("")

#Crear un programa que me pida en una lista 5 edades,
# me haga la media de edad en una función y me diga el número de personas mayores 
# de edad y menores de edad en otra función.

def ingresar_edades():
    edades = []
    for i in range(5):
        edad = int(input(f"Ingrese la edad de la persona {i + 1}: "))
        edades.append(edad)
    return edades

def calcular_media(edades):
    return sum(edades) / len(edades)

def contar_mayores_menores(edades):
    mayores = sum(1 for edad in edades if edad >= 18)
    menores = len(edades) - mayores
    return mayores, menores

edades = ingresar_edades()
media = calcular_media(edades)
mayores, menores = contar_mayores_menores(edades)
print(f"La media de edad es: {media:.2f}")
print(f"Número de personas mayores de edad: {mayores}")
print(f"Número de personas menores de edad: {menores}")


print("Fin del programa")
