ruta = input("Ruta del archivo: ")

try:
    with open(ruta, "r", encoding="utf-8") as f:
        contenido = f.read()

    lineas = contenido.splitlines()
    palabras = contenido.split()

    print("Líneas:", len(lineas))
    print("Palabras:", len(palabras))
    print("Caracteres:", len(contenido))
except FileNotFoundError:
    print("El archivo no existe")
