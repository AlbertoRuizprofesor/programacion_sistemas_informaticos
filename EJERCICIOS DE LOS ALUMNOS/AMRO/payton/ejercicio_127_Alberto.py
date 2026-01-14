def cargar_edades():
    edades = []
    for i in range(5):
        edad = int(input(f"Introduce la edad {i+1}: "))
        edades.append(edad)
    return edades

def calcular_media(edades):
    return sum(edades) / len(edades)  

def contarmayores_y_menores(edades):
    mayores=0
    menores=0
    for edad in edades:
        if edad>=18:
            mayores=mayores+1
        else:
            menores=menores+1    
    
    print(f"Número de personas mayores de edad: {mayores}")    
    print(f"Número de personas menores de edad: {menores}")

#bloque main
edades = cargar_edades()
media = calcular_media(edades)

print(f"La media de edad es: {media:.2f}")
contarmayores_y_menores(edades) 