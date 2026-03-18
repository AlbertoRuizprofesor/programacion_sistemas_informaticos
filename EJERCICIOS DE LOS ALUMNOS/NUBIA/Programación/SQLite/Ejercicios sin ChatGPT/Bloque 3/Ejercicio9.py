'''
Lee un archivo de texto y muestra cuántas líneas, palabras y caracteres contiene. 
Idea clave: Gestiona el caso en que el archivo no exista.
'''
# split() divide una cadena de texto (string) en una lista de subcadenas más pequeñas
# Si no se indican parámetros, divide la cadena por cualquier espacio en blanco y los elimina del resultado.

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