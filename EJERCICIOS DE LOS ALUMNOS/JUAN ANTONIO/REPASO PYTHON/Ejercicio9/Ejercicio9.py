# Ejercicio 9. Contador de líneas y palabras

archivo = input("Introduce la ruta del fichero: ")

try:
    with open(archivo, "r", encoding="utf-8") as doc:
        texto = doc.read()

    filas = texto.splitlines()
    terminos = texto.split()

    print("Total de líneas:", len(filas))
    print("Total de palabras:", len(terminos))
    print("Total de caracteres:", len(texto))

except FileNotFoundError:
    print("No se ha encontrado el fichero indicado")

 