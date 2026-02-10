def pedir_edades():
    edades = []
    for i in range(5):
        edad = float(input(f"Introduce la edad {i+1}: "))
        edades.append(edad)
    return edades

def calcular_media(edades):
    return sum(edades) / len(edades)

def mayor(edades):
    may = edades[0]
    for x in range(1, len(edades)):
        if edades[x] > may:
            may = edades[x]
    return may

def menor(edades):
    men = edades[0]
    for x in range(1, len(edades)):
        if edades[x] < men:
            men = edades[x]
    return men

def contar_menores(edades):
    cont = 0
    for x in range(len(edades)):
        if edades[x] < 18:
            cont += 1
    return cont

def contar_mayores(edades):
    cont = 0
    for x in range(len(edades)):
        if edades[x] >= 18:
            cont += 1
    return cont

# Programa principal
edades = pedir_edades()

print("Lista:", edades)
print("Media:", calcular_media(edades))
print("Edad mayor:", mayor(edades))
print("Edad menor:", menor(edades))
print("Cantidad de menores:", contar_menores(edades))
print("Cantidad de mayores:", contar_mayores(edades))
