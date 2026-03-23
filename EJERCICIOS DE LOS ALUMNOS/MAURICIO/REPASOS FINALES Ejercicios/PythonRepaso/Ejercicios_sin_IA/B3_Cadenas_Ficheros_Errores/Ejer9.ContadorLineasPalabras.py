ruta = "C:\\prueba\\python.txt"

try:
    lineas = 0
    palabras = 0
    caracteres = 0

    with open(
        ruta, "r", encoding="utf-8"
    ) as f:  # Abrimos el archivo con la codificación UTF-8
        for linea in f:  # Iteramos sobre cada línea del archivo
            lineas += 1  # Contamos las líneas
            print(linea)  # Imprimimos la línea actual
            caracteres += len(
                linea
            )  # Contamos los caracteres de la línea (incluyendo espacios)
            palabras += len(
                linea.split()
            )  # Contamos las palabras de la línea (separadas por espacios)

    # Los print también deben estar alineados con el 'with' o dentro de él
    print(f"Líneas: {lineas}")
    print(f"Palabras: {palabras}")
    print(f"Caracteres (con espacios): {caracteres}")

except FileNotFoundError:
    print("Error: No se encontró el archivo en la ruta especificada.")
except UnicodeDecodeError:
    print("Error: El archivo no tiene un formato UTF-8 válido.")
