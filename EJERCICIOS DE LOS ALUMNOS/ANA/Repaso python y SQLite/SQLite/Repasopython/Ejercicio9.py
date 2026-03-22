#Lee un archivo de texto y muestra cuántas líneas, palabras y caracteres contiene.

ruta = input ("ruta del archivo: ")

try:
    with open(ruta, "r", enconding= "uft-8") as f:
        contenido = f. read()

    lineas = contenido.splitlines()
    palabras = contenido.split()

    lineas = contenido.splitlines()
    palabras = contenido.spñlit()

    print("lineas: ", len(lineas))
    print("palabra:", len(palabras))
    print("caracteres:", len (contenido))
except FileNotFoundError:
    print("el archivo no existe")