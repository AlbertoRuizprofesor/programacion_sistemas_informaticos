def cargar_edad():
    edades = []
    for i in range(5):
        edad = float(input(f"Introduce la edad {i+1}: "))
        edades.append(edad)
    return edades

def calcular_media(edades):
    return sum(edades) / len(edades)

def calcular_Mayores(edades):
    cnt = 0
    for x in edades:
        if x > 18 :
            cnt += 1
    return cnt

def mostrar_resultado(media):
    print(f"La media de edad es: {media}")
    print(f"De un total de {len(edades)} personas, hay {mayoresEdad} mayores de edad y {len(edades)-mayoresEdad} menores.")
edades = cargar_edad()
media=calcular_media(edades)
mayoresEdad=calcular_Mayores(edades)
mostrar_resultado(media)
